import os
import re
import requests
import numpy as np
from cv2 import cv2
from dotenv import load_dotenv
from fuzzywuzzy import fuzz, process

load_dotenv()
API_KEY = os.getenv('OCR_SPACE_API_KEY')

choices = ['HP', 'Healing', 'DEF', 'Energy Recharge', 'Elemental Mastery', 'ATK', 'CRIT DMG', 'CRIT Rate', 'Physical DMG']
elements = ['Anemo', 'Electro', 'Pyro', 'Hydro', 'Cryo', 'Geo', 'Dendro']
choices += [element + ' DMG' for element in elements]

reg = re.compile(r'\d+(?:\.\d+)?')
hp_reg = re.compile(r'\d,\d{3}')

max_mains = {'HP': [4780, 0], 'ATK': [311.0, 0.5], 'ATK%': [46.6, 1], 'Energy Recharge%': [51.8, 0.5], 'Elemental Mastery': [187.0, 0.5],
			 'Physical DMG%': [58.3, 1], 'CRIT Rate%': [31.1, 1], 'CRIT DMG%': [62.2, 1], 'Elemental DMG%': [46.6, 1],
			 'HP%': [46.6, 0], 'DEF%': [58.3, 0], 'Healing%': [35.9, 0]}
max_subs = {'ATK': [19.0, 0.5], 'Elemental Mastery': [23.0, 0.5], 'Energy Recharge%': [6.5, 0.5], 'ATK%': [5.8, 1],
			'CRIT Rate%': [3.9, 1], 'CRIT DMG%': [7.8, 1], 'DEF': [23.0, 0], 'HP': [299.0, 0], 'DEF%': [7.3, 0], 'HP%': [5.8, 0]}

def ocr(url):
	size = int(requests.get(url, stream=True).headers['Content-length'])
	if size > 1e6:
		resp = requests.get(url, stream=True).raw
		img = np.asarray(bytearray(resp.read()), dtype="uint8")
		flag = cv2.IMREAD_GRAYSCALE
		if size > 4e6:
			flag = cv2.IMREAD_REDUCED_GRAYSCALE_2
		img = cv2.imdecode(img, flag)
		_, img = cv2.imencode('.png', img)
		file = {'file': ('image.png', img.tostring(), 'image/png', {'Expires': '0'})}
		ocr_url = 'https://api.ocr.space/parse/image'
		data = {'apikey': API_KEY, 'OCREngine': 2}
		resp = requests.post(ocr_url, data=data, files=file)
	else:
		ocr_url = 'https://api.ocr.space/parse/imageurl?apikey={0}&OCREngine=2&url={1}'.format(API_KEY, url)
		resp = requests.get(ocr_url)
	if resp.json()['OCRExitCode'] != 1:
		return False, resp.json()['ErrorMessage']
	return True, resp.json()['ParsedResults'][0]['ParsedText']

def parse(text):
	# print(text)
	stat = None
	results = []
	for line in text.splitlines():
		if not line:
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

def rate(results):
	main = True
	score = 0.0
	total_weight = 16.5
	main_weight = 8
	for result in results:
		stat, value = result
		if main:
			main = False
			key = stat if stat.split()[0] not in elements else 'Elemental DMG%'
			if key in ['ATK%', 'CRIT Rate%', 'CRIT DMG%']:
				total_weight -= 0.5
			elif key in ['ATK', 'HP']:
				total_weight -= main_weight * (1 - max_mains[key][1])
			if key in max_mains:
				value = validate(value, max_mains[key][0], '%' in stat)
				score += value / max_mains[key][0] * max_mains[key][1] * main_weight
		elif stat in max_subs:
			value = validate(value, max_subs[stat][0] * 6, '%' in stat)
			score += value / max_subs[stat][0] * max_subs[stat][1]
		result[1] = value
		print(result)
	score = score / total_weight
	print('Gear Score: {0:.2f}%'.format(score * 100))
	return score

if __name__ == '__main__':
	url = 'https://media.discordapp.net/attachments/774633095160397836/775836631794057296/unknown.png'
	suc, text = ocr(url)
	if suc:
		results = parse(text)
		score = rate(results)