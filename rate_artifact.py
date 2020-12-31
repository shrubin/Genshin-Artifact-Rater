import translations as tr

import aiohttp
import asyncio
import os
import re
import sys
import time
import numpy as np

from cv2 import cv2
from dotenv import load_dotenv
from fuzzywuzzy import fuzz, process
from unidecode import unidecode

load_dotenv()
OCR_API_KEY = os.getenv('OCR_SPACE_API_KEY')

reg = re.compile(r'\d+(?:[.,]\d+)?')
hp_reg = re.compile(r'\d[.,]\d{3}')
lvl_reg = re.compile(r'^\+\d\d?$')
bad_lvl_reg_1 = re.compile(r'^\+?\d\d?$')
bad_lvl_reg_2 = re.compile(r'^\d{4}\d*$')

async def ocr(url, num, lang=tr.en()):
	if not OCR_API_KEY:
		print('Error: OCR_SPACE_API_KEY not found')
		return False, 'Error: OCR_SPACE_API_KEY not found'
	async with aiohttp.ClientSession() as session:
		async with session.get(url) as r:
			size = int(r.headers['Content-length'])
			if size > 5e6:
				img = np.asarray(bytearray(await r.read()), dtype="uint8")
				flag = cv2.IMREAD_GRAYSCALE
				if size > 8e6 or os.path.splitext(url)[1] == '.jpg':
					flag = cv2.IMREAD_REDUCED_GRAYSCALE_2
				img = cv2.imdecode(img, flag)
				_, img = cv2.imencode('.png', img)
				data = aiohttp.FormData()
				data.add_field('apikey', OCR_API_KEY)
				if lang.supported:
					data.add_field('OCREngine', '2')
				else:
					data.add_field('language', lang.code)
				data.add_field('file', img.tobytes(), content_type='image/png', filename='image.png')
				ocr_url = f'https://apipro{num}.ocr.space/parse/image'
				async with session.post(ocr_url, data=data) as r:
					json = await r.json()
			else:
				ocr_url = f'https://apipro{num}.ocr.space/parse/imageurl?apikey={OCR_API_KEY}&url={url}'
				if lang.supported:
					ocr_url += '&OCREngine=2'
				else:
					ocr_url += f'&language={lang.code}'
				async with session.get(ocr_url) as r:
					json = await r.json()
			print(f'OCR Response: {json}')
			if json['OCRExitCode'] != 1:
				return False, f'{lang.err}: ' + '. '.join(json['ErrorMessage'])
			if 'ParsedResults' not in json:
				return False, lang.err_unknown_ocr
			return True, json['ParsedResults'][0]['ParsedText']

def parse(text, lang=tr.en()):
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

		for k,v in lang.replace.items():
			line = line.replace(k,v)
		line = unidecode(line).lower()
		line = line.replace(':','.').replace('-','').replace('0/0','%')
		if line.replace(' ','') in lang.ignore:
			continue
		if  fuzz.partial_ratio(line, unidecode(lang.piece_set).lower()) > 80 and len(line) > 4:
			break

		value = lvl_reg.search(line.replace(' ',''))
		if value:
			if level == None or (len(results) == 1 and not stat):
				print('1', line)
				level = int(value[0].replace('+',''))
			continue

		value = hp_reg.search(line.replace(' ',''))
		if value:
			print('2', line)
			value = int(value[0].replace(',','').replace('.',''))
			results += [[lang.hp, value]]
			stat = None
			continue

		extract = process.extractOne(line, list(choices))
		if extract[1] <= 80:
			extract = process.extractOne(line, list(choices), scorer=fuzz.partial_ratio)

		if ((extract[1] > 80) and len(line.replace(' ','')) > 1) or stat:
			print('3', line)
			if (extract[1] > 80):
				stat = choices[extract[0]]
			value = reg.findall(line.replace(' ','').replace(',','.'))
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

		value = bad_lvl_reg_1.search(line.replace(' ','')) or bad_lvl_reg_2.search(line.replace(' ','').replace('+',''))
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


min_mains_np = np.array([ 47.0,  7.0,  9.3,  4.7,  8.7,  28.0,  7.8,  717.0,  7.0,  7.0,  5.4,  8.7])
max_mains_np = np.array([311.0, 46.6, 62.2, 31.1, 58.3, 187.0, 51.8, 4780.0, 46.6, 46.6, 35.9, 58.3])
sub_rolls = np.array([[14, 16, 18, 19], [4.1, 4.7, 5.3, 5.8], [5.4, 6.2, 7.0, 7.8], [2.7, 3.1, 3.5, 3.9],
		      [5.1, 5.8, 6.6, 7.3], [16, 19, 21, 23], [4.5, 5.2, 5.8, 6.5], [209, 239, 269, 299],
		      [4.1, 4.7, 5.3, 5.8], [16, 19, 21, 23]])
sub_pct = np.array([15,10,8,8,10,10,10,15,10,15])

def sim(artifact, ct):
	rolls_left = (20 - artifact[0] + 3) // 4
	relevant_substats = np.repeat((artifact[13:] != 0).astype(int) * sub_pct, 4)
	relevant_substats = relevant_substats/np.sum(relevant_substats)

	sub_matrix = np.zeros((10,40))
	for i in range(0,10):
		sub_matrix[i,(i*4):((i+1)*4)] = sub_rolls[i]
	sub_matrix = np.transpose(sub_matrix)

	rolls = np.random.multinomial(rolls_left, relevant_substats, size=ct)
	rolled_substats = np.add(np.matmul(rolls, sub_matrix), artifact[13:])

	max_main = np.append([20], (artifact[1:13] != 0).astype(int) * max_mains_np)
	artifacts = np.append(np.tile(max_main, (ct, 1)), rolled_substats, axis=1)
	return np.vstack((artifact, artifacts))

def indices(lang=tr.en()):
	elements = [lang.anemo, lang.elec, lang.pyro, lang.hydro, lang.cryo, lang.geo, lang.dend]
	main_indices = {lang.atk: 1, f'{lang.atk}%': 2, f'{lang.cd}%': 3, f'{lang.cr}%': 4, f'{lang.df}%': 5, 
			lang.em: 6, f'{lang.er}%': 7, lang.hp: 8, f'{lang.hp}%': 9,
			f'{lang.elem}%': 10, f'{lang.heal}%': 11, f'{lang.phys}%': 12}
	sub_indices = {lang.atk: 13, f'{lang.atk}%': 14, f'{lang.cd}%': 15, f'{lang.cr}%': 16, f'{lang.df}%': 17,
		       lang.em: 18, f'{lang.er}%': 19, lang.hp: 20, f'{lang.hp}%': 21,
		       lang.df: 22}
	return elements, main_indices, sub_indices

def to_np(level, results, options = {}, lang=tr.en()):
	elements, main_indices, sub_indices = indices(lang)

	# we represent an artifact as a 23-element array
	# index 0 = the level
	# index 1-12 = the main stat, atk atk% cd% cr% df% em er% hp hp% elem% heal% phys% only one of these should be nonzero
	# index 13-22 = the substats, atk atk% cd% cr% df% em er% hp hp% df upto four of these should be nonzero
	# note that these are ordered such that for stats that appear in main and substats, sub index = main index + 12
	artifact = np.zeros(23)
	artifact[0] = level
	main_key = results[0][0] if results[0][0][:-1] not in elements else f'{lang.elem}%'
	main_i = main_indices[main_key]-1
	main_max = max_mains_np[main_i] - (max_mains_np[main_i] - min_mains_np[main_i]) * (1 - level / 20.0)
	artifact[main_indices[main_key]] = validate(results[0][1], main_max, '%' in main_key)
	for substat in results[1:]:
		sub_key = substat[0]
		sub_i = sub_indices[sub_key]-13
		artifact[sub_indices[sub_key]] = validate(substat[1], sub_rolls[sub_i,3]*6, '%' in sub_key)

	# weights is similarly a 23-element array
	# index 0 is unused
	# index 1-12 = weights for main stats, in the order above
	# index 13-22 = weights for substats, in the order above
	weight_obj = {lang.hp: 0, lang.atk: 0.5, f'{lang.atk}%': 1, f'{lang.er}%': 0.5, lang.em: 0.5,
		      f'{lang.phys}%': 1, f'{lang.cr}%': 1, f'{lang.cd}%': 1, f'{lang.elem}%': 1,
		      f'{lang.hp}%': 0, f'{lang.df}%': 0, lang.df: 0, f'{lang.heal}%': 0}
	weight_obj = {**weight_obj, **options}
	weights = np.zeros(23)
	for k,v in main_indices.items():
		weights[v] = weight_obj[k]
	for k,v in sub_indices.items():
		weights[v] = weight_obj[k]

	return artifact, weights

def rate_broadcastable(artifacts, weights):
	artifacts = np.array(artifacts)
	ct = np.shape(artifacts)[0]

	levels = artifacts[:,0]
	mains = artifacts[:,1:13]
	subs = artifacts[:,13:]
	main_weights = weights[1:13]
	sub_weights = weights[13:]
	level_weighting = 3 + levels // 4

	main_pts = level_weighting * ((mains / max_mains_np) @ main_weights)
	# for atk and hp main stat (i.e., feather and flower) you can't do better than that main stat
	main_max_pts = level_weighting * ((mains != 0).astype(int) @ [weights[1], 1, 1, 1, 1, 1, 1, weights[8], 1, 1, 1, 1])

	sub_pts = (subs / sub_rolls[:,3]) @ weights[13:]
	# we don't want to count the existing main stat when calculating the maximal substat weighting
	mask_main_stat = np.append((mains[:,0:9] == 0).astype(int), np.ones((ct, 1), np.int8), axis=1)
	max_weights = np.sort(mask_main_stat * sub_weights)[:,-4:]
	max_rolls = np.append(np.ones((ct, 3), np.int8), np.reshape(1 + levels // 4, (ct, 1)), axis=1)
	sub_max_pts = np.sum(max_weights * max_rolls, axis=1)

	def pct(a, b):
		return (np.divide(100*a, b, out=(100*np.ones_like(b)), where=b!=0))

	score = pct(main_pts + sub_pts, main_max_pts + sub_max_pts)
	main_score = pct(main_pts, main_max_pts)
	sub_score = pct(sub_pts, sub_max_pts)
	return score, main_score, main_max_pts, sub_score, sub_max_pts

# for now we only run sims for artifacts that have four substats already
# it's _possible_ to sim new substats as well but it's significantly more annoying
def rate_np(level, results, options={}, lang=tr.en()):
	artifact, weights = to_np(level, results, options, lang)
	if (np.count_nonzero(artifact[13:]) == 4):
		simulated = sim(artifact, 10000)
		score, main_score, main_weight, sub_score, sub_weight = rate_broadcastable(simulated, weights)
		score_percentile = np.percentile(score[1:], 60)
		substat_percentiles_arr = np.percentile(simulated[1:,13:], 60, axis=0)
		_, _, sub_indices = indices(lang)
		substat_percentiles = {}
		for k,v in sub_indices.items():
			item = substat_percentiles_arr[v-13]
			if item != 0:
				substat_percentiles[k] = item
		return score[0], main_score[0], main_weight[0], sub_score[0], sub_weight[0], score_percentile, substat_percentiles
	else:
		score, main_score, main_weight, sub_score, sub_weight = rate_broadcastable([artifact], weights)
		return score[0], main_score[0], main_weight[0], sub_score[0], sub_weight[0], None, None

def rate(level, results, options={}, lang=tr.en()):
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
	return score, main_score, main_weight, sub_score, sub_weight

if __name__ == '__main__':
	if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):
		asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
	url = 'https://cdn.discordapp.com/attachments/790417874409750549/793035090035867678/unknown.png'
	lang = tr.de()
	suc, text = asyncio.run(ocr(url, 2, lang))
	# lang = tr.en()
	# suc, text = True, 'Bard\'s Arrow Feather\nATK\n161\n+10\nHP+239\nDEF+4.7%\nCRIT DMG+5.0%\nDEF+30'#asyncio.run(ocr(url, 2, lang))
	print(text)
	if suc:
		level, results = parse(text, lang)
		if level == None:
			level = 20
		start = time.time_ns()
		score, main_score, main_weight, sub_score, sub_weight, score_percentiles, substat_percentiles = rate_np(level, results, {}, lang)
		print(f'Gear Score: {score:.2f}% (main {main_score:.2f}% {main_weight}, sub {sub_score:.2f}% {sub_weight})')
		print(f'Gear Score 40%ile at l20: {score_percentiles:.2f}, substat 40%iles: {substat_percentiles}')
		print(f'compute took {time.time_ns() - start}ns')