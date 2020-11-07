from rate_artifact import rate_artifact_char, rate_artifact_arti

import os
import requests
from cv2 import cv2
from discord.ext import commands
from dotenv import load_dotenv
import numpy as np

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='-')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

async def get_image(ctx):
	try:
		url = ctx.message.attachments[0].url
		resp = requests.get(url, stream=True).raw
		img = np.asarray(bytearray(resp.read()), dtype="uint8")
		img = cv2.imdecode(img, cv2.IMREAD_COLOR)
		return img
	except Exception as err:
		print("Error: {0}".format(err))
		await ctx.send('Error trying to fetch image')

@bot.command(name='char')
async def char(ctx):
	img = await get_image(ctx)
	final_pct, results = rate_artifact_char(img)
	msg = 'Parsed Image: ' + str(results) + '\nGear Score: {0:.2f}%'.format(final_pct * 100)
	await ctx.send(msg)

@bot.command(name='arti')
async def arti(ctx):
	img = await get_image(ctx)
	final_pct, results = rate_artifact_arti(img)
	msg = 'Parsed Image: ' + str(results) + '\nGear Score: {0:.2f}%'.format(final_pct * 100)
	await ctx.send(msg)

bot.run(TOKEN)
