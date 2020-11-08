import os
import re
import requests
import numpy as np
from cv2 import cv2
from dotenv import load_dotenv
from fuzzywuzzy import fuzz, process

load_dotenv()
API_KEY = os.getenv('OCR_SPACE_API_KEY')

choices = ['HP', 'Healing Bonus', 'DEF', 'Energy Recharge', 'Elemental Mastery', 'ATK', 'CRIT DMG', 'CRIT Rate', 'Physical DMG Bonus']
elements = ['Anemo', 'Electro', 'Pyro', 'Hydro', 'Cryo', 'Geo', 'Dendro']
choices += [element + ' DMG Bonus' for element in elements]

reg = re.compile(r'\d+(?:\.\d+)?')
hp_reg = re.compile(r'\d,\d\d\d')

max_mains = {'ATK': [311.0, 1], 'ATK%': [46.6, 1], 'Energy Recharge%': [51.8, 0.5], 'Elemental Mastery': [187.0, 0.5],
			 'Physical DMG Bonus%': [58.3, 1], 'CRIT Rate%': [31.1, 1], 'CRIT DMG%': [62.2, 1], 'Elemental DMG Bonus%': [46.6, 1]}
max_subs = {'ATK': [19.0, 0.5], 'Elemental Mastery': [23.0, 0.5], 'Energy Recharge%': [6.5, 0.5],
			'ATK%': [5.8, 1], 'CRIT Rate%': [3.9, 1], 'CRIT DMG%': [7.8, 1]}

def ocr(url):
	size = int(requests.get(url, stream=True).headers['Content-length'])
	if size > 1e6:
		resp = requests.get(url, stream=True).raw
		img = np.asarray(bytearray(resp.read()), dtype="uint8")
		img = cv2.imdecode(img, cv2.IMREAD_GRAYSCALE)
		_, img = cv2.imencode('.png', img)
		file = {'file': ('image.png', img.tostring(), 'image/png', {'Expires': '0'})}
		ocr_url = 'https://api.ocr.space/parse/image'
		data = {'apikey': API_KEY, 'OCREngine': 2}
		resp = requests.post(ocr_url, data=data, files=file)
	else:
		ocr_url = 'https://api.ocr.space/parse/imageurl?apikey={0}&OCREngine=2&url={1}'.format(API_KEY, url)
		resp = requests.get(ocr_url)
	return resp.json()['ParsedResults'][0]['ParsedText']

def parse(text):
	# print(text)
	stat = None
	results = []
	for line in text.splitlines():
		if not line:
			continue
		line = line.replace(':','.')
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
		extract = process.extractOne(line, choices, scorer=fuzz.partial_ratio)
		# print(process.extract(line, choices, scorer=fuzz.partial_ratio))
		if ((extract[1] > 80) and len(line) > 1) or stat:
			print(line)
			if (extract[1] > 80):
				stat = extract[0]
			value = reg.findall(line)
			if not value:
				continue
			value = max(value, key=len).replace(',','')
			if len(value) < 2:
				continue
			if value.isdigit():
				value = int(value)
			else:
				value = float(value)
				stat += '%'
			results += [[stat, value]]
			stat = None
			if len(results) == 5:
				break
	return results

def rate(results):
	main = True
	score = 0.0
	total_weight = 16.5
	main_weight = 8
	for result in results:
		print(result)
		stat, value = result
		if main:
			main = False
			key = stat if stat.split()[0] not in elements else 'Elemental DMG Bonus%'
			if key == 'HP':
				total_weight -= main_weight
			elif key in ['ATK%', 'CRIT Rate%', 'CRIT DMG%']:
				total_weight -= 0.5
			if key in max_mains:
				score += value / max_mains[key][0] * max_mains[key][1] * main_weight
		else:
			if stat in max_subs:
				score += value / max_subs[stat][0] * max_subs[stat][1]
	score = score / total_weight
	print('Gear Score: {0:.2f}%'.format(score * 100))
	return score

if __name__ == '__main__':
	url = 'https://cdn.discordapp.com/attachments/769162931303743549/774689718293757952/image0.png'
	text = ocr(url)
	results = parse(text)
	score = rate(results)
