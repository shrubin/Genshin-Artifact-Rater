import rate_artifact as ra

import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='-')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='rate')
async def rate(ctx):
	if not ctx.message.attachments:
		return
	url = ctx.message.attachments[0].url
	text = ra.ocr(url)
	if text:
		results = ra.parse(text)
		score = ra.rate(results)
		msg = 'Parsed Image: ' + str(results) + '\nGear Score: {0:.2f}%'.format(score * 100)
	else:
		msg = 'OCR failed, please try taking a new screenshot'
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
