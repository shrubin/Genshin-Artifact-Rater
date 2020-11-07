from rate_artifact import rate_artifact

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

@bot.command(name='rate')
async def rate(ctx):
	try:
		url = ctx.message.attachments[0].url
		resp = requests.get(url, stream=True).raw
		img = np.asarray(bytearray(resp.read()), dtype="uint8")
		img = cv2.imdecode(img, cv2.IMREAD_COLOR)
		final_pct, results = rate_artifact(img)
		msg = 'Parsed Image: ' + str(results) + '\nGear Score: {0:.2f}%'.format(final_pct * 100)
	except Exception as err:
		msg = 'Error trying to fetch image'
		print("Error: {0}".format(err))
	await ctx.send(msg)

bot.run(TOKEN)
