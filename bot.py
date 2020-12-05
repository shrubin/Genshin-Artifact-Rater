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

	If you have any issues or want to use the bot in your private server, contact shrubin#1866 on discord.
	Source code available at https://github.com/shrubin/Genshin-Artifact-Rater

	Default weights

	ATK%, DMG%, Crit - 1
	ATK, EM, Recharge - 0.5
	Everything else - 0

	Options

	lvl: Compare to specified artifact level (default: <artifact_level>)
	-rate lvl=20

	<stat>: Set custom weights (valued between 0 and 1)
	-rate atk=1 er=0 atk%=0.5

	<stat> is any of HP, HP%, ATK, ATK%, ER (Recharge), EM, PHYS, CR (Crit Rate), CD (Crit Damage), ELEM (Elemental DMG%), Heal, DEF, DEF%
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
		level, results  = ra.parse(text)
		if not('Level' in options.keys()):
			options = {**options, 'Level': level}
		score, main_score, sub_score, grade_score = ra.rate(results, options)

		main_score_msg = f'Main Stat: {main_score:.2f}%'
		sub_score_msg = f'Sub Stat: {sub_score:.2f}%'
		score_msg = f'Overall: {score:.2f}% ({grade_score})'
		separator_msg = f'---------------------------'
		parsed_msg = 'OCR Result: {results}'
		msg = f'OCR Result: {results}\n**Gear Score**\n{separator_msg}\n{main_score_msg}\n{sub_score_msg}\n{separator_msg}\n**{score_msg}**'
	else:
		msg = f'OCR failed. Error: {text}'
		if 'Timed out' in text:
			msg += ', please try again in a few minutes'
	await ctx.send(msg)

bot.run(TOKEN)
