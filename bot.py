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

@bot.command(name='rate')
async def rate(ctx):
	if not ctx.message.attachments:
		return
	url = ctx.message.attachments[0].url
	suc, text = await ra.ocr(url)
	global calls
	calls += 1
	print(f'Calls: {calls}')
	if suc:
		results = ra.parse(text)
		score = ra.rate(results)
		msg = f'Parsed Image: {results}\nGear Score: {score*100 : .2f}%'
	else:
		msg = f'OCR failed. Error: {text}'
	await ctx.send(msg)

@bot.command(name='char')
async def char(ctx):
	msg = 'Deprecated, please use -rate'
	await ctx.send(msg)

@bot.command(name='arti')
async def arti(ctx):
	msg = 'Deprecated, please use -rate'
	await ctx.send(msg)

bot.run(TOKEN)
