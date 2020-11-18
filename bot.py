import rate_artifact as ra

import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='-')

calls = 0

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to {[guild.name for guild in bot.guilds]}')

opt_to_key = {'hp': 'HP', 'atk': 'ATK', 'atk%': 'ATK%', 'er': 'Energy Recharge%', 'em': 'Elemental Mastery',
			  'phys': 'Physical DMG%', 'cr': 'CRIT Rate%', 'cd': 'CRIT DMG%', 'elem': 'Elemental DMG%',
			  'hp%': 'HP%', 'def%': 'DEF%', 'heal': 'Healing%', 'def': 'DEF', 'lvl': 'Level'}

@bot.command(name='rate')
async def rate(ctx):
	'''
	Rate an artifact against an optimal 5* artifact. Put the command and image in the same message.

	-rate <image> [lvl=<level>] [<stat>=<weight> ...]

	Default weights

	ATK%, DMG%, Crit - 1
	ATK, EM, Recharge - 0.5
	Everything else - 0

	Options

	lvl: Compare to specified artifact level (default: 20)
	-rate lvl=0

	<stat>: Set custom weights (valued between 0 and 1)
	-rate atk=1 er=0 atk%=0.5

	<stat> = HP, HP%, ATK, ATK%, ER (Recharge), EM, PHYS, CR (Crit Rate), CD (Crit Damage), ELEM (Elemental DMG%), Heal, DEF, DEF%
	'''
	if not ctx.message.attachments:
		return
	options = ctx.message.content.split()[1:]
	options = {opt_to_key[option.split('=')[0].lower()] : float(option.split('=')[1]) for option in options}
	url = ctx.message.attachments[0].url
	suc, text = await ra.ocr(url)
	global calls
	calls += 1
	print(f'Calls: {calls}')
	if suc:
		results = ra.parse(text)
		score, main_score, sub_score = ra.rate(results, options)
		msg = f'Parsed Image: {results}\nGear Score: {score:.2f}% (main {main_score:.2f}%, sub {sub_score:.2f}%)'
	else:
		msg = f'OCR failed. Error: {text}'
		if 'Timed out' in text:
			msg += ', please try again in a few minutes'
	await ctx.send(msg)

bot.run(TOKEN)
