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
	await ctx.send(msg)

bot.run(TOKEN)
