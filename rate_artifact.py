import aiohttp
import asyncio
import os
import re
import sys
import numpy as np
from cv2 import cv2
from dotenv import load_dotenv
from fuzzywuzzy import fuzz, process

load_dotenv()
API_KEY = os.getenv('OCR_SPACE_API_KEY')

choices = ['HP', 'Healing', 'DEF', 'Energy Recharge', 'Elemental Mastery', 'ATK', 'CRIT DMG', 'CRIT Rate', 'Physical DMG']
elements = ['Anemo', 'Electro', 'Pyro', 'Hydro', 'Cryo', 'Geo', 'Dendro']
choices += [f'{element} DMG' for element in elements]

reg = re.compile(r'\d+(?:\.\d+)?')
hp_reg = re.compile(r'\d,\d{3}')
lvl_reg = re.compile(r'^[+][0-9]*$')

min_mains = {'HP': 717.0, 'ATK': 47.0, 'ATK%': 7.0, 'Energy Recharge%': 7.8, 'Elemental Mastery': 28.0,
			 'Physical DMG%': 8.7, 'CRIT Rate%': 4.7, 'CRIT DMG%': 9.3, 'Elemental DMG%': 7.0,
			 'HP%': 7.0, 'DEF%': 8.7, 'Healing%': 5.4}
max_mains = {'HP': 4780, 'ATK': 311.0, 'ATK%': 46.6, 'Energy Recharge%': 51.8, 'Elemental Mastery': 187.0,
			 'Physical DMG%': 58.3, 'CRIT Rate%': 31.1, 'CRIT DMG%': 62.2, 'Elemental DMG%': 46.6,
			 'HP%': 46.6, 'DEF%': 58.3, 'Healing%': 35.9}
max_subs = {'ATK': 19.0, 'Elemental Mastery': 23.0, 'Energy Recharge%': 6.5, 'ATK%': 5.8,
			'CRIT Rate%': 3.9, 'CRIT DMG%': 7.8, 'DEF': 23.0, 'HP': 299.0, 'DEF%': 7.3, 'HP%': 5.8}
weights = {'HP': 0, 'ATK': 0.5, 'ATK%': 1, 'Energy Recharge%': 0.5, 'Elemental Mastery': 0.5,
		   'Physical DMG%': 1, 'CRIT Rate%': 1, 'CRIT DMG%': 1, 'Elemental DMG%': 1,
		   'HP%': 0, 'DEF%': 0, 'DEF': 0, 'Healing%': 0}

async def ocr(url):
	if not API_KEY:
		print('Error: OCR_SPACE_API_KEY not found')
		return
	async with aiohttp.ClientSession() as session:
		async with session.get(url) as r:
			size = int(r.headers['Content-length'])
			if size > 1e6:
				img = np.asarray(bytearray(await r.read()), dtype="uint8")
				flag = cv2.IMREAD_GRAYSCALE
				if size > 2e6:
					flag = cv2.IMREAD_REDUCED_GRAYSCALE_2
				img = cv2.imdecode(img, flag)
				_, img = cv2.imencode(os.path.splitext(url)[1], img)
				data = aiohttp.FormData()
				data.add_field('apikey', API_KEY)
				data.add_field('OCREngine', '2')
				data.add_field('file', img.tobytes(), content_type='image/png', filename='image.png')
				ocr_url = 'https://api.ocr.space/parse/image'
				async with session.post(ocr_url, data=data) as r:
					json = await r.json()
			else:
				ocr_url = f'https://api.ocr.space/parse/imageurl?apikey={API_KEY}&OCREngine=2&url={url}'
				async with session.get(ocr_url) as r:
					json = await r.json()
			if json['OCRExitCode'] != 1:
				return False, '.'.join(json['ErrorMessage'])
			return True, json['ParsedResults'][0]['ParsedText']

def parse(text):
	stat = None
	results = []
	results_str = ''
	level = None
	for line in text.splitlines():
		if not line or line.lower() == 'in':
			continue
		line = line.replace(':','.').replace('-','').replace('0/0','%')
		if fuzz.partial_ratio(line, 'Piece Set') > 80 and len(line) > 4:
			break
		if not(level) and level !=0:
			level = lvl_reg.findall(line)
			if level:
				level = int(level[0].replace('+', ''))
		value = hp_reg.search(line)
		if value:
			value = int(value[0].replace(',', ''))
			results += [['HP', value]]
			if len(results) == 1:
				results_str += str(f'**{stat}: {value}**\n')
			else:
				results_str += str(f'{stat}: {value}\n')
			stat = None
			continue
		extract = process.extractOne(line, choices, scorer=fuzz.partial_ratio)
		if ((extract[1] > 80) and len(line) > 1) or stat:
			if (extract[1] > 80):
				stat = extract[0]
			line = line.replace(',','')
			value = reg.findall(line)
			if not value:
				continue
			value = max(value, key=len)
			if len(value) < 2:
				continue
			if line.find('%', line.find(value)) != -1 and '.' not in value:
				value = value[:-1] + '.' + value[-1]
			if '.' in value:
				value = float(value)
				stat += '%'
			else:
				value = int(value)
			results += [[stat, value]]
			if len(results) == 1:
				results_str += str(f'**{stat}: {value}**\n')
			else:
				results_str += str(f'{stat}: {value}\n')
			stat = None
			if len(results) == 5:
				break
	return level, results, results_str

def validate(value, max_stat, percent):
	while value > max_stat * 1.05:
		value = str(value)
		removed = False
		for i in reversed(range(1, len(value))):
			if value[i] == value[i-1]:
				value = value[:i-1] + value[i:]
				removed = True
				break
		if not removed:
			if percent:
				pos = value.find('.')
				value = value[:pos-1] + value[pos:]
			else:
				value = value[:-1]
		value = float(value) if percent else int(value)
	if int(value) == 1:
		value += 10
	return value

def grade(score):
	if score >= 0 and score <= 50:
		return 1
	elif score > 50 and score < 75:
		return 2
	else:
		return 3

def rate(results, options={}):
	main = True
	main_score = 0.0
	sub_score = 0.0
	sub_weight = 0
	main_weight = 8
	level = 20
	if 'Level' in options:
		level = int(options['Level'])
		main_weight -= (5 - level / 4)
		del options['Level']
	# Replaces weights with options
	adj_weights = {**weights, **options}
	for result in results:
		stat, value = result
		key = stat if stat.split()[0] not in elements else 'Elemental DMG%'
		if main:
			main = False
			max_main = max_mains[key] - (max_mains[key] - min_mains[key]) * (1 - level / 20.0)
			value = validate(value, max_main, '%' in key)
			main_score = value / max_main * adj_weights[key] * main_weight
			if key in ['ATK', 'HP']:
				main_weight *= adj_weights[key]
			count = 0
			for k,v in sorted(adj_weights.items(), reverse=True, key=lambda item: item[1]):
				if k == key or k not in max_subs:
					continue
				if count == 0:
					sub_weight += v * (1 + level / 4)
				else:
					sub_weight += v
				count += 1
				if count == 4:
					break
		else:
			value = validate(value, max_subs[key] * 6, '%' in key)
			sub_score += value / max_subs[key] * adj_weights[key]
		result[1] = value

	score = (main_score + sub_score) / (main_weight + sub_weight) * 100 if main_weight + sub_weight > 0 else 100
	main_score = main_score / main_weight * 100 if main_weight > 0 else 100
	main_score = 100 if main_score > 99 else main_score
	sub_score = sub_score / sub_weight * 100 if sub_weight > 0 else 100
	grade_score = grade(score)
	print(f'Gear Score: {score:.2f}% (main {main_score:.2f}% {main_weight}, sub {sub_score:.2f}% {sub_weight})')
	print(grade_score)
	return score, main_score, sub_score, grade_score

if __name__ == '__main__':
	if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):
		asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
	url = 'https://i.redd.it/qjzqzrzmgpz51.png'
	suc, text = asyncio.run(ocr(url))
	if suc:
		level, results, results_str = parse(text)
		print(level)
		print(results)
		print(results_str)
		rate(results, {'Level': level})
