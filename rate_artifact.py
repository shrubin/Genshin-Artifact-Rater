from cv2 import cv2
from fuzzywuzzy import fuzz, process
import numpy as np
import pytesseract
import re

def rate_artifact(img):
	choices = ['HP', 'Healing Bonus', 'DEF', 'Energy Recharge', 'Elemental', 'ATK', 'DMG', 'CRIT Rate']
	elements = ['Anemo', 'Electro', 'Pyro', 'Hydro', 'Cryo', 'Geo', 'Dendro']
	dmg_choices = elements + ['CRIT', 'Physical']

	reg = re.compile(r'(?:[IntS\d]+,)?[IntS\d]*\d[IntS\d]*(?:\.[IntS\d]+)?')

	out = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	out = cv2.threshold(out, 170, 255, cv2.THRESH_BINARY_INV)[1]

	cv2.imwrite('out.png', out)

	custom_config = r'--oem 3 --psm 11'
	text = pytesseract.image_to_string(out, config=custom_config)

	cur_stat = None
	results = []
	for line in text.splitlines():
		if line:
			if fuzz.partial_ratio(line, 'Piece Set') > 60:
				break
			# print(line)
			extract = process.extractOne(line, choices, scorer=fuzz.partial_ratio)
			# print(process.extract(line, choices, scorer=fuzz.partial_ratio))
			if (extract[1] > 80) or cur_stat:
				print(line)
				if cur_stat:
					stat = cur_stat
				else:
					stat = extract[0]
					if extract[0] == 'DMG':
						extract_dmg = process.extractOne(line, dmg_choices, scorer=fuzz.partial_ratio)
						if extract_dmg[1] <= 80:
							continue
						stat = extract_dmg[0] + ' DMG'
				value = reg.findall(line)
				if not value:
					cur_stat = None if cur_stat else stat
					continue
				cur_stat = None
				value = max(value, key=len)
				comma = '.' if len(value) < 5 else ''
				value = value.replace(',',comma).replace('I','1').replace('n','11').replace('t','1').replace('S','5')
				if value.isdigit():
					value = int(value)
				else:
					value = float(value)
					stat += '%'
				results += [[stat, value]]
				if len(results) == 5:
					break

	max_mains = {'ATK': 311.0, 'ATK%': 46.6, 'Energy Recharge%': 51.8, 'Elemental': 187.0, 'Physical DMG%': 58.3,
				 'CRIT Rate%': 31.1, 'CRIT DMG%': 62.2, 'Elem DMG%': 46.6}
	multiplier = 2
	max_subs = {'ATK': 19.0 * multiplier, 'Elemental': 23.0 * multiplier, 'Energy Recharge%': 6.5 * multiplier,
				'ATK%': 5.8, 'CRIT Rate%': 3.9, 'CRIT DMG%': 7.8}

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
	return final_pct, results

if __name__ == '__main__':
	img = cv2.imread('test.jpg')
	rate_artifact(img)