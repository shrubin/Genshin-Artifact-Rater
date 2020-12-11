import rate_artifact as ra

import os
import sys
import validators
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID', 0))
DEVELOPMENT = os.getenv('DEVELOPMENT', 'False') == 'True'

calls = 0

bot = commands.Bot(command_prefix='-')

@bot.event
async def on_ready():
	msg = f'{bot.user.name} has connected to {len(bot.guilds)} servers'
	print(msg)
	if CHANNEL_ID:
		channel = bot.get_channel(CHANNEL_ID)
		await channel.send(msg)

@bot.event
async def on_disconnect():
	if CHANNEL_ID:
		channel = bot.get_channel(CHANNEL_ID)
		await channel.send(user, f'{bot.user.name} disconnected after {calls} calls')

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

	lvl: Compare to specified artifact level (default: 20)
	-rate lvl=0

	<stat>: Set custom weights (valued between 0 and 1)
	-rate atk=1 er=0 atk%=0.5

	<stat> is any of HP, HP%, ATK, ATK%, ER (Recharge), EM, PHYS, CR (Crit Rate), CD (Crit Damage), ELEM (Elemental DMG%), Heal, DEF, DEF%
	'''
	global calls
	options = ctx.message.content.split()[1:]
	if options and validators.url(options[0]):
		url = options[0]
		options = options[1:]
	elif ctx.message.attachments:
		url = ctx.message.attachments[0].url
	else:
		return
	options = {opt_to_key[option.split('=')[0].lower()] : float(option.split('=')[1]) for option in options}
	suc, text = await ra.ocr(url)
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
	if not DEVELOPMENT:
		await ctx.send(msg)

if TOKEN:
	bot.run(TOKEN)
else:
	print('Error: DISCORD_TOKEN not found')
