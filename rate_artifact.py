import translations as tr

import aiohttp
import asyncio
import os
import re
import sys
import numpy as np
from cv2 import cv2
from dotenv import load_dotenv
from fuzzywuzzy import fuzz, process
from unidecode import unidecode

load_dotenv()
API_KEY = os.getenv('OCR_SPACE_API_KEY')

reg = re.compile(r'\d+(?:\.\d+)?')
hp_reg = re.compile(r'\d,\d{3}')
lvl_reg = re.compile(r'^\+\d\d?$')
bad_lvl_reg = re.compile(r'^\+?\d\d?$')

async def ocr(url, lang=tr.en):
	if not API_KEY:
		print('Error: OCR_SPACE_API_KEY not found')
		return False, 'Error: OCR_SPACE_API_KEY not found'
	async with aiohttp.ClientSession() as session:
		async with session.get(url) as r:
			size = int(r.headers['Content-length'])
			if size > 1e6:
				img = np.asarray(bytearray(await r.read()), dtype="uint8")
				flag = cv2.IMREAD_GRAYSCALE
				if size > 2e6 or os.path.splitext(url)[1] == '.jpg':
					flag = cv2.IMREAD_REDUCED_GRAYSCALE_2
				img = cv2.imdecode(img, flag)
				_, img = cv2.imencode('.png', img)
				data = aiohttp.FormData()
				data.add_field('apikey', API_KEY)
				if lang.supported:
					data.add_field('OCREngine', '2')
				else:
					data.add_field('language', lang.code)
				data.add_field('file', img.tobytes(), content_type='image/png', filename='image.png')
				ocr_url = 'https://api.ocr.space/parse/image'
				async with session.post(ocr_url, data=data) as r:
					json = await r.json()
			else:
				ocr_url = f'https://api.ocr.space/parse/imageurl?apikey={API_KEY}&url={url}'
				if lang.supported:
					ocr_url += '&OCREngine=2'
				else:
					ocr_url += f'&language={lang.code}'
				async with session.get(ocr_url) as r:
					json = await r.json()
			if json['OCRExitCode'] != 1:
				return False, f'{lang.err}: ' + '. '.join(json['ErrorMessage'])
			if 'ParsedResults' not in json:
				return False, lang.err_unknown_ocr
			return True, json['ParsedResults'][0]['ParsedText']

def parse(text, lang=tr.en):
	stat = None
	results = []
	level = None
	prev = None
	del_prev = True

	elements = [lang.anemo, lang.elec, lang.pyro, lang.hydro, lang.cryo, lang.geo, lang.dend]
	choices = elements + [lang.hp, lang.heal, lang.df, lang.er, lang.em, lang.atk, lang.cd, lang.cr, lang.phys]
	choices = {unidecode(choice).lower(): choice for choice in choices}

	for line in text.splitlines():
		if not line:
			continue

		if del_prev:
			prev = None
		del_prev = True

		line = unidecode(line).lower()
		line = line.replace(':','.').replace('-','').replace('0/0','%')
		if line.replace(' ','') in lang.ignore or (fuzz.partial_ratio(line, unidecode(lang.piece_set).lower()) > 80 and len(line) > 4):
			break

		value = lvl_reg.search(line.replace(' ',''))
		if value:
			if level == None:
				print('1', line)
				level = int(value[0].replace('+', ''))
			continue

		value = hp_reg.search(line.replace(' ',''))
		if value:
			print('2', line)
			value = int(value[0].replace(',', ''))
			results += [[lang.hp, value]]
			stat = None
			continue

		extract = process.extractOne(line, list(choices), scorer=fuzz.partial_ratio)
		if ((extract[1] > 80) and len(line.replace(' ','')) > 1) or stat:
			print('3', line)
			if (extract[1] > 80):
				stat = choices[extract[0]]
			line = line.replace(',','')
			value = reg.findall(line.replace(' ',''))
			if not value:
				if not prev:
					continue
				print('4', prev)
				value = prev
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
			continue

		value = bad_lvl_reg.search(line.replace(' ',''))
		if not value:
			line = line.replace(',','')
			prev = reg.findall(line.replace(' ',''))
			del_prev = False

	print(level, results)
	return level, results

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

def rate(level, results, options={}, lang=tr.en):
	main = True
	main_score = 0.0
	sub_score = 0.0
	sub_weight = 0
	main_weight = 3 + level / 4

	elements = [lang.anemo, lang.elec, lang.pyro, lang.hydro, lang.cryo, lang.geo, lang.dend]

	min_mains = {lang.hp: 717.0, lang.atk: 47.0, f'{lang.atk}%': 7.0, f'{lang.er}%': 7.8, lang.em: 28.0,
				 f'{lang.phys}%': 8.7, f'{lang.cr}%': 4.7, f'{lang.cd}%': 9.3, f'{lang.elem}%': 7.0,
				 f'{lang.hp}%': 7.0, f'{lang.df}%': 8.7, f'{lang.heal}%': 5.4}
	max_mains = {lang.hp: 4780, lang.atk: 311.0, f'{lang.atk}%': 46.6, f'{lang.er}%': 51.8, lang.em: 187.0,
				 f'{lang.phys}%': 58.3, f'{lang.cr}%': 31.1, f'{lang.cd}%': 62.2, f'{lang.elem}%': 46.6,
				 f'{lang.hp}%': 46.6, f'{lang.df}%': 58.3, f'{lang.heal}%': 35.9}
	max_subs = {lang.atk: 19.0, lang.em: 23.0, f'{lang.er}%': 6.5, f'{lang.atk}%': 5.8,
				f'{lang.cr}%': 3.9, f'{lang.cd}%': 7.8, lang.df: 23.0, lang.hp: 299.0, f'{lang.df}%': 7.3, f'{lang.hp}%': 5.8}
	weights = {lang.hp: 0, lang.atk: 0.5, f'{lang.atk}%': 1, f'{lang.er}%': 0.5, lang.em: 0.5,
			   f'{lang.phys}%': 1, f'{lang.cr}%': 1, f'{lang.cd}%': 1, f'{lang.elem}%': 1,
			   f'{lang.hp}%': 0, f'{lang.df}%': 0, lang.df: 0, f'{lang.heal}%': 0}

	# Replaces weights with options
	weights = {**weights, **options}

	for result in results:
		stat, value = result
		key = stat if stat[:-1] not in elements else f'{lang.elem}%'
		if main:
			main = False
			max_main = max_mains[key] - (max_mains[key] - min_mains[key]) * (1 - level / 20.0)
			value = validate(value, max_main, '%' in key)
			main_score = value / max_main * weights[key] * main_weight
			if key in [lang.atk, lang.hp]:
				main_weight *= weights[key]
			count = 0
			for k,v in sorted(weights.items(), reverse=True, key=lambda item: item[1]):
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
			sub_score += value / max_subs[key] * weights[key]
		result[1] = value

	score = (main_score + sub_score) / (main_weight + sub_weight) * 100 if main_weight + sub_weight > 0 else 100
	main_score = main_score / main_weight * 100 if main_weight > 0 else 100
	main_score = 100 if main_score > 99 else main_score
	sub_score = sub_score / sub_weight * 100 if sub_weight > 0 else 100
	print(f'Gear Score: {score:.2f}% (main {main_score:.2f}% {main_weight}, sub {sub_score:.2f}% {sub_weight})')
	return score, main_score, sub_score

if __name__ == '__main__':
	if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):
		asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
	url = 'https://imgur.com/pBDmcoY'
	lang = tr.en
	suc, text = asyncio.run(ocr(url, lang))
	print(text)
	if suc:
		level, results = parse(text, lang)
		rate(level, results, {}, lang)
