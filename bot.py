import rate_artifact as ra
import translations as tr

import asyncio
import discord
import heroku3
import os
import sys
import traceback
import validators

from discord.ext import commands, tasks
from dotenv import load_dotenv
from signal import SIGINT, SIGTERM

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID', 0))
DEVELOPMENT = os.getenv('DEVELOPMENT', 'False') == 'True'
HEROKU_API_KEY = os.getenv('HEROKU_API_KEY')
HEROKU_APP_ID = os.getenv('HEROKU_APP_ID')

if HEROKU_API_KEY and HEROKU_APP_ID:
	heroku_conn = heroku3.from_key(HEROKU_API_KEY)
	app = heroku_conn.apps()[HEROKU_APP_ID]

RETRIES = 1
MAX_CRASHES = 10
RATE_LIMIT_N = 5
RATE_LIMIT_TIME = 10

calls = 0
crashes = 0

bot = commands.Bot(command_prefix='-', activity=discord.Game(name='Genshin Impact | -help'))

async def send(msg):
	print(msg)
	if CHANNEL_ID:
		channel = bot.get_channel(CHANNEL_ID)
		await channel.send(msg)

@bot.event
async def on_ready():
	await send(f'{bot.user.name} has connected to {len(bot.guilds)} servers')
	count.start()

@bot.event
async def on_resumed():
	await send(f'{bot.user.name} reconnected')

@bot.event
async def on_disconnect():
	print(f'{bot.user.name} disconnected')

@bot.event
async def on_error(event, *args, **kwargs):
	await send(f'{bot.user.name} raised an exception in {event}\n' + traceback.format_exc())

@bot.event
async def on_termination():
	await send(f'{bot.user.name} terminated after {calls} calls')

@tasks.loop(hours=24.0)
async def count():
	global calls
	if calls != 0:
		await send(f'{bot.user.name} has been called {calls} times in the past day')
	calls = 0

def create_opt_to_key(lang):
	return {lang.hp_opt: lang.hp, lang.atk_opt: lang.atk, f'{lang.atk_opt}%': f'{lang.atk}%',
			lang.er_opt: f'{lang.er}%', lang.em_opt: lang.em, lang.phys_opt: f'{lang.phys}%',
			lang.cr_opt: f'{lang.cr}%', lang.cd_opt: f'{lang.cd}%', lang.elem_opt: f'{lang.elem}%',
			f'{lang.hp_opt}%': f'{lang.hp}%', f'{lang.df_opt}%': f'{lang.df}%',
			lang.heal_opt: f'{lang.heal}%', lang.df_opt: lang.df, lang.lvl_opt: lang.lvl}

async def rate(ctx, lang):
	global calls, crashes

	options = ctx.message.content.split()[1:]
	if options and validators.url(options[0]):
		url = options[0]
		options = options[1:]
		if '.' not in url.split('?')[0].split('/')[-1]:
			if '?' in url:
				url = '.png?'.join(url.split('?'))
			else:
				url += '.png'
	elif ctx.message.attachments:
		url = ctx.message.attachments[0].url
	else:
		print(f'Error: Could not parse "{ctx.message.content}"')
		if not DEVELOPMENT:
			await ctx.send(lang.err_not_found)
		return

	opt_to_key = create_opt_to_key(lang)
	try:
		options = {opt_to_key[option.split('=')[0].lower()] : float(option.split('=')[1]) for option in options}
	except:
		print(f'Error: Could not parse "{ctx.message.content}"')
		if not DEVELOPMENT:
			await ctx.send(lang.err_parse)
		return

	calls += 1
	print(url)
	for i in range(RETRIES + 1):
		try:
			suc, text = await ra.ocr(url, lang)

			if not suc:
				if 'Timed out' in text:
					text += f', {lang.err_try_again}'
				print(text)
				if i < RETRIES:
					continue
				if not DEVELOPMENT:
					await ctx.send(text)
				crashes += 1
				if crashes >= MAX_CRASHES and HEROKU_API_KEY and HEROKU_APP_ID:
					print(f'Crashed {MAX_CRASHES} times, restarting')
					app.restart()
				return

			level, results = ra.parse(text, lang)
			if lang.lvl in options:
				level = int(options[lang.lvl])
			elif level == None:
				level = 20
			score, main_score, sub_score = ra.rate(level, results, options, lang)
			crashes = 0
			break

		except Exception:
			print(f'Uncaught exception\n{traceback.format_exc()}')
			if i < RETRIES:
				continue
			if not DEVELOPMENT:
				await ctx.send(lang.err_unknown)
			if CHANNEL_ID:
				channel = bot.get_channel(CHANNEL_ID)
				await channel.send(f'Uncaught exception in {ctx.guild} #{ctx.channel}\n{ctx.message.content}\n{url}\n{traceback.format_exc()}')
			crashes += 1
			if crashes >= MAX_CRASHES and HEROKU_API_KEY and HEROKU_APP_ID:
				print(f'Crashed {MAX_CRASHES} times, restarting')
				app.restart()
			return

	if score <= 50:
		color = discord.Color.blue()
	elif score > 50 and score <= 75:
		color = discord.Color.purple()
	else:
		color = discord.Color.orange()

	msg = f'\n\n**{results[0][0]}: {results[0][1]}**'
	for result in results[1:]:
		msg += f'\n{result[0]}: {result[1]}'
	msg += f'\n\n**{lang.score}: {score:.2f}%**'
	msg += f'\n{lang.main_score}: {main_score:.2f}%'
	msg += f'\n{lang.sub_score}: {sub_score:.2f}%'
	msg += f'\n\n{lang.join % "(https://discord.gg/SyGmBxds3M)"}'

	embed = discord.Embed(color=color)
	embed.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
	embed.add_field(name=f'{lang.art_level}: {level}', value=msg)

	if not DEVELOPMENT:
		await ctx.send(embed=embed)
	elif CHANNEL_ID:
		channel = bot.get_channel(CHANNEL_ID)
		await channel.send(embed=embed)

async def feedback(ctx, lang):
	if not DEVELOPMENT:
		await ctx.send(lang.feedback)
	if CHANNEL_ID:
		channel = bot.get_channel(CHANNEL_ID)
		embed = discord.Embed()
		if ctx.message.attachments:
			embed.set_image(url=ctx.message.attachments[0].url)
		elif ctx.message.embeds:
			embed.set_image(url=ctx.message.embeds[0].url)
		else:
			embed = None
		await channel.send(f'{ctx.message.author}: {ctx.message.content}', embed=embed)

def make_f(cb, lang):
	suffix = f'_{lang.uid}' if lang.uid != 'en' else ''
	@bot.command(name=f'{cb.__name__}{suffix}')
	@commands.cooldown(RATE_LIMIT_N, RATE_LIMIT_TIME, commands.BucketType.user)
	async def _f(ctx):
		await cb(ctx, lang)
	return _f

for lang in tr.languages:
	_rate = make_f(rate, lang)
	_rate.help = lang.help_rate
	_rate.brief = lang.help_rate.split('\n')[0]

	_feedback = make_f(feedback, lang)
	_feedback.help = lang.help_feedback
	_feedback.brief = lang.help_feedback.split('\n')[0]

if __name__ == '__main__':
	if not TOKEN:
		print('Error: DISCORD_TOKEN not found')
		sys.exit(1)

	loop = asyncio.get_event_loop()

	def interrupt():
		raise KeyboardInterrupt

	loop.add_signal_handler(SIGINT, interrupt)
	loop.add_signal_handler(SIGTERM, interrupt)

	try:
		loop.run_until_complete(bot.start(TOKEN))
	except KeyboardInterrupt:
		pass
	finally:
		loop.run_until_complete(bot.on_termination())
		loop.run_until_complete(bot.logout())
