import rate_artifact as ra

import os
import requests
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
API_KEY = os.getenv('OCR_SPACE_API_KEY')

ocr_url = 'https://api.ocr.space/parse/imageurl?apikey={0}&url={1}'

bot = commands.Bot(command_prefix='-')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='rate')
async def rate(ctx):
	url = ctx.message.attachments[0].url
	resp = requests.get(ocr_url.format(API_KEY, url))
	text = resp.json()['ParsedResults'][0]['ParsedText']
	results = ra.parse(text)
	score = ra.rate(results)
	msg = 'Parsed Image: ' + str(results) + '\nGear Score: {0:.2f}%'.format(score * 100)
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
