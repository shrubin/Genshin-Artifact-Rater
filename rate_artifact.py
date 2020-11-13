import aiohttp
import asyncio
import os
import re
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
				return False, json['ErrorMessage']
			return True, json['ParsedResults'][0]['ParsedText']

def parse(text):
	# print(text)
	stat = None
	results = []
	for line in text.splitlines():
		if not line or line.lower() == 'in':
			continue
		line = line.replace(':','.').replace('-','').replace('0/0','%')
		# print(line, fuzz.partial_ratio(line, 'Piece Set'))
		if fuzz.partial_ratio(line, 'Piece Set') > 80 and len(line) > 4:
			break
		value = hp_reg.search(line)
		if value:
			print(line)
			value = int(value[0].replace(',', ''))
			results += [['HP', value]]
			stat = None
			continue
		# print(line)
		extract = process.extractOne(line, choices, scorer=fuzz.partial_ratio)
		# print(process.extract(line, choices, scorer=fuzz.partial_ratio))
		if ((extract[1] > 80) and len(line) > 1) or stat:
			print(line)
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
			stat = None
			if len(results) == 5:
				break
	return results

def validate(value, max_stat, percent):
	while value > max_stat:
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

def rate(results, options={}):
	main = True
	main_score = 0.0
	sub_score = 0.0
	sub_weight = 8.5
	main_weight = 8
	level = None
	if 'Level' in options:
		level = int(options['Level'])
		sub_weight -= (5 - level / 4)
		main_weight -= (5 - level / 4)
	for result in results:
		stat, value = result
		key = stat if stat.split()[0] not in elements else 'Elemental DMG%'
		weight = options[key] if key in options else weights[key]
		if main:
			main = False
			if key in ['ATK%', 'CRIT Rate%', 'CRIT DMG%']:
				sub_weight -= 0.5
			elif key in ['ATK', 'HP']:
				main_weight *= weight
			max_main = max_mains[key]
			if level is not None:
				max_main -= (max_main - min_mains[key]) * (1 - level / 20.0)
			value = validate(value, max_mains[key], '%' in key)
			main_score = value / max_main * weight * main_weight
		else:
			value = validate(value, max_subs[key] * 6, '%' in key)
			sub_score += value / max_subs[key] * weight
		result[1] = value
		print(result)
	score = (main_score + sub_score) / (main_weight + sub_weight) * 100
	main_score = main_score / main_weight * 100 if main_weight > 0 else 0
	sub_score = sub_score / sub_weight * 100
	print(f'Gear Score: {score:.2f}% (main {main_score:.2f}%, sub {sub_score:.2f}%)')
	return score, main_score, sub_score

if __name__ == '__main__':
	url = 'https://cdn.discordapp.com/attachments/774633095160397836/776848767533056010/Screenshot_20201111-111041.png'
	suc, text = asyncio.run(ocr(url))
	print(text)
	if suc:
		results = parse(text)
		rate(results)
