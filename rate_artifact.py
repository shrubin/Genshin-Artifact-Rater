from cv2 import cv2
from fuzzywuzzy import fuzz, process
import numpy as np
import pytesseract
import re

custom_config = r'--oem 3 --psm 11'

choices = ['HP', 'Healing', 'DEF', 'Recharge', 'Elemental', 'ATK', 'DMG', 'CRIT Rate']
elements = ['Anemo', 'Electro', 'Pyro', 'Hydro', 'Cryo', 'Geo', 'Dendro']
dmg_choices = elements + ['CRIT', 'Physical']

reg = re.compile(r'(?:[IntS/\?\]\d]+,)?[IntS/\?\]\d]*\d[IntS/\?\]\d]*(?:,?\.,?[IntS/\?\]\d]+)?')
backup = re.compile(r'[IntS/\?\]\d]*[IntS/\?\]]\.[IntS/\?\]\d]+')

max_mains = {'ATK': 311.0, 'ATK%': 46.6, 'Energy Recharge%': 51.8, 'Elemental': 187.0, 'Physical DMG%': 58.3,
			 'CRIT Rate%': 31.1, 'CRIT DMG%': 62.2, 'Elem DMG%': 46.6}
multiplier = 2
max_subs = {'ATK': 19.0 * multiplier, 'Elemental': 23.0 * multiplier, 'Energy Recharge%': 6.5 * multiplier,
			'ATK%': 5.8, 'CRIT Rate%': 3.9, 'CRIT DMG%': 7.8}

def prepare_image(img):
	out = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	out = cv2.threshold(out, 170, 255, cv2.THRESH_BINARY_INV)[1]
	out = cv2.resize(out, (int(out.shape[1] * 3), int(out.shape[0] * 3)))
	return out

def parse_artifact(img, num_results):
	text = pytesseract.image_to_string(img, config=custom_config)
	# print(text)

	cur_stat = None
	count = 0
	results = []
	for line in text.splitlines():
		line = line.replace(' ','')
		if line and len(line) > 1:
			# print(line, fuzz.partial_ratio(line, 'Piece'))
			if fuzz.partial_ratio(line, 'Piece') > 80 and len(line) > 3:
				break
			# print(line)
			extract = process.extractOne(line, choices, scorer=fuzz.partial_ratio)
			# print(process.extract(line, choices, scorer=fuzz.partial_ratio))
			if ((extract[1] > 80) and len(line) > len(extract[0])-2) or count > 0:
				# print(line)
				if (extract[1] > 80):
					count = 0
					stat = extract[0]
					if extract[0] == 'DMG':
						extract_dmg = process.extractOne(line, dmg_choices, scorer=fuzz.partial_ratio)
						if extract_dmg[1] <= 80:
							continue
						stat = extract_dmg[0] + ' DMG'
				else:
					stat = cur_stat
				value = reg.findall(line)
				if not value or len(max(value, key=len)) < 2:
					value = backup.findall(line)
					if not value or len(max(value, key=len)) < 2:
						count -= 1
						if count < 0:
							cur_stat = stat
							count = 2
						continue
				count = 0
				value = max(value, key=len)
				value = value.replace('I','1').replace('n','11').replace('t','1').replace('S','5').replace(
									  '/','7').replace('?','7').replace(']','1')
				num_digits = sum(v.isdigit() for v in value)
				if num_digits > 3:
					value = value.replace(',','').replace('.','')
				elif value[-2] == ',':
					value = value.replace(',','').replace('.','')
					value = value[:-1] + '.' + value[-1]
				else:
					value = value.replace(',','')
				if value.isdigit():
					value = int(value)
				else:
					value = float(value)
					stat += '%'
				if any(stat in result[0] for result in results):
					continue
				results += [[stat, value]]
				if len(results) == num_results:
					break
	return results

def rate_artifact(results):
	main = True
	pct = 0.0
	total_weight = 16.5
	main_weight = 8
	half_weight = ['ATK', 'Elemental', 'Energy Recharge%']
	for result in results:
		print(result)
		stat, value = result
		if main:
			main = False
			key = stat if stat.split()[0] not in elements else 'Elem DMG%'
			if key == 'HP':
				total_weight -= main_weight
			elif key in ['ATK%', 'CRIT Rate%', 'CRIT DMG%']:
				total_weight -= 0.5
			if key in max_mains:
				pct += value / max_mains[key] * main_weight
		else:
			if stat in max_subs:
				pct += value / max_subs[stat]

	final_pct = pct / total_weight
	print(final_pct)
	return final_pct

def rate_artifact_char(img):
	out = prepare_image(img)
	cv2.imwrite('out.png', out)
	results = parse_artifact(out, 5)
	final_pct = rate_artifact(results)
	return final_pct, results

def rate_artifact_arti(img):
	out = prepare_image(img)

	contours = cv2.findContours(out, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2]
	c = max(contours, key = cv2.contourArea)
	_,_,_,h = cv2.boundingRect(c)

	out1 = out[:h,:]
	cv2.imwrite('out1.png', out1)
	results = parse_artifact(out1, 1)

	out2 = cv2.bitwise_not(out[h:,:])
	cv2.imwrite('out2.png', out2)
	results += parse_artifact(out2, 4)

	final_pct = rate_artifact(results)
	return final_pct, results

if __name__ == '__main__':
	img = cv2.imread('test.png')
	rate_artifact_arti(img)