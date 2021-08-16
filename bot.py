import rate_artifact as ra
import translations as tr

import asyncio
import discord
import os
import sys
import traceback
import validators

from discord.ext import commands, tasks
from dotenv import load_dotenv
from signal import SIGINT, SIGTERM

import toml

config = toml.load(open("config.toml"))

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
AUTHOR_ID = int(os.getenv('AUTHOR_ID', 0))
CHANNEL_ID = int(os.getenv('CHANNEL_ID', 0))
SHARD_CHANNEL_ID = int(os.getenv('SHARD_CHANNEL_ID', 0))
DEV_CHANNEL_ID = int(os.getenv('DEV_CHANNEL_ID', 0))
ERR_CHANNEL_ID = int(os.getenv('ERR_CHANNEL_ID', 0))
DEVELOPMENT = os.getenv('DEVELOPMENT', 'False') == 'True'
HEROKU_API_KEY = os.getenv('HEROKU_API_KEY')
HEROKU_APP_ID = os.getenv('HEROKU_APP_ID')
DATABASE_URL = os.getenv('DATABASE_URL')
SHARDS = int(os.getenv('SHARDS', 1))

if HEROKU_API_KEY and HEROKU_APP_ID:
	import heroku3
	heroku_conn = heroku3.from_key(HEROKU_API_KEY)
	app = heroku_conn.apps()[HEROKU_APP_ID]

if DATABASE_URL:
	import database as db

RETRIES = 1
MAX_CRASHES = 10
RATE_LIMIT_N = 5
RATE_LIMIT_TIME = 10

calls = 0
crashes = 0
started = False
running = False

def get_lang(ctx):
	if DATABASE_URL:
		guild_id = ctx.guild.id if ctx.guild else None
		lang = db.get_lang(ctx.message.author.id, guild_id)
		if lang:
			return tr.languages[lang]
	return tr.en()

def get_presets(ctx):
	if DATABASE_URL:
		guild_id = ctx.guild.id if ctx.guild else None
		presets = []
		for preset in db.get_presets(ctx.message.author.id, guild_id):
			if presets and preset.name == presets[-1].name:
				if preset.entry_id == ctx.message.author.id:
					presets[-1] = preset
				elif presets[-1].entry_id != ctx.message.author.id and preset.entry_id == guild_id:
					presets[-1] = preset
			else:
				presets.append(preset)
		return presets

def prefix(bot, message):
	if DATABASE_URL and message.guild and any(name in message.content for name in command_names):
		prefix = db.get_prefix(message.guild.id)
		if prefix:
			return prefix
	return '-'

bot = commands.AutoShardedBot(command_prefix=prefix, shard_count=SHARDS, max_messages=None, help_command=None)

async def send_internal(msg, channel_id=CHANNEL_ID):
	print(msg)
	if DEVELOPMENT:
		if DEV_CHANNEL_ID:
			channel = bot.get_channel(DEV_CHANNEL_ID)
			await channel.send(msg)
	elif channel_id:
		channel = bot.get_channel(channel_id)
		await channel.send(msg)



@bot.event
async def on_ready():
	global started, running
	if not running:
		await send_internal(f'{bot.user.name} has connected to {len(bot.guilds)} servers')
		running = True
	if not started:
		count.start()
		started = True

for cogs in config['cogs']:
	try:
		bot.load_extension(cogs)
		print(f'[Loaded] {cogs}')
	except Exception as e:
		print(f'[Error] {cogs} | {e}')








@bot.event
async def on_resumed():
	global running
	if not running:
		await send_internal(f'{bot.user.name} reconnected')
		running = True

@bot.event
async def on_disconnect():
	global running
	if running:
		try:
			await send_internal(f'{bot.user.name} disconnected')
		finally:
			running = False

@bot.event
async def on_shard_connect(shard_id):

	print(f"[Shard] {shard_id+1} Connected")



@bot.event
async def on_shard_disconnect(shard_id):
	print(f"[Shard] {shard_id+1} Disconnected")




@bot.event
async def on_shard_ready(shard_id):
	print(f"[Shard] {shard_id+1} Ready")





	

@bot.event
async def on_error(event, *args, **kwargs):
	await send_internal(f'{bot.user.name} raised an exception in {event}\n' + traceback.format_exc(), ERR_CHANNEL_ID)

@bot.event
async def on_termination():
	await send_internal(f'{bot.user.name} terminated after {calls} calls')

@tasks.loop(hours=24.0)
async def count():
	global calls
	if calls > 100:
		await send_internal(f'{bot.user.name} has been called {calls} times in the past day')
	calls = 0

async def send(ctx, msg=None, embed=None):
	dev_only = ctx.channel and ctx.channel.id == DEV_CHANNEL_ID
	if not DEVELOPMENT and not dev_only:
		return await ctx.send(msg, embed=embed)
	elif DEVELOPMENT and dev_only:
		channel = bot.get_channel(DEV_CHANNEL_ID)
		return await channel.send(msg, embed=embed)



@bot.command(name='user', aliases=['server'])
@commands.cooldown(RATE_LIMIT_N, RATE_LIMIT_TIME, commands.BucketType.user)
async def config(ctx):
	if DEVELOPMENT and not (ctx.channel and ctx.channel.id == DEV_CHANNEL_ID):
		return
	if not DATABASE_URL:
		return

	lang = get_lang(ctx)

	msg = ctx.message.content.split()
	if len(msg) < 3 or (msg[1] == 'preset' and len(msg) < 4) or (msg[1] == 'prefix' and len(msg) > 3):
		await send(ctx, msg=lang.err_parse)
		return

	is_server = 'server' in msg[0]
	attr = msg[1]
	val = ' '.join(msg[2:])
	id = ctx.guild.id if is_server else ctx.message.author.id

	if is_server and not ctx.message.author.guild_permissions.administrator:
		await send(ctx, msg=lang.err_admin_only)
		return

	if attr == 'lang':
		if val not in tr.languages:
			await send(ctx, msg=lang.err_parse)
			return
		db.set_lang(id, val)
		lang = tr.languages[val]
		await send(ctx, msg=lang.set_lang)

	elif attr == 'prefix':
		if not is_server:
			await send(ctx, msg=lang.err_server_only)
			return
		db.set_prefix(id, val)
		await send(ctx, msg=lang.set_prefix % val)

	elif attr == 'preset':
		val = val.split()
		if val[0] == 'delete':
			deleted = []
			for name in val[1:]:
				if db.del_preset(id, name):
					deleted.append(name)
			if not deleted:
				await send(ctx, msg=lang.no_presets)
				return
			await send(ctx, msg=lang.del_preset % ", ".join(deleted))
		else:
			name = val[0]
			command = ' '.join(val[1:])
			for option in command.split():
				if '=' not in option:
					await send(ctx, msg=lang.err_parse)
					return
			db.set_preset(id, name, command)
			await send(ctx, msg=lang.set_preset % (name, command))

@bot.command(aliases=['presets'])
@commands.cooldown(RATE_LIMIT_N, RATE_LIMIT_TIME, commands.BucketType.user)
async def sets(ctx):
	if DEVELOPMENT and not (ctx.channel and ctx.channel.id == DEV_CHANNEL_ID):
		return
	if not DATABASE_URL:
		return

	lang = get_lang(ctx)
	presets = get_presets(ctx)

	if not presets:
		await send(ctx, msg=lang.no_presets)
		return

	embed = discord.Embed(title='Presets', colour=discord.Colour.blue())
	for preset in presets:
		if preset.entry_id == ctx.message.author.id:
			source = ctx.message.author.display_name
		elif ctx.guild and preset.entry_id == ctx.guild.id:
			source = ctx.guild.name
		else:
			source = 'Artifact Rater'
		embed.add_field(name=f'{preset.name} - {source}', value=preset.command, inline=False)
	await send(ctx, embed=embed)

def create_embed(lang):
	embed = discord.Embed(title=lang.help_title, description=lang.help_description, colour=discord.Colour.red())
	embed.add_field(name=lang.source, value=lang.github)
	embed.add_field(name=lang.invite, value=lang.discord)
	embed.add_field(name=lang.support, value=lang.server)
	embed.set_footer(text=lang.help_footer)
	return embed

@bot.command()
@commands.cooldown(RATE_LIMIT_N, RATE_LIMIT_TIME, commands.BucketType.user)
async def help(ctx):
	if DEVELOPMENT and not (ctx.channel and ctx.channel.id == DEV_CHANNEL_ID):
		return

	lang = get_lang(ctx)

	command = ctx.message.content.split()
	if len(command) > 2 or len(command) == 2 and command[1] not in lang.help_commands:
		await send(ctx, msg=lang.err_parse)
		return

	if len(command) == 1:
		embed = create_embed(lang)
		msg = await send(ctx, embed=embed)

		flags = {}
		for lang in tr.languages.values():
			for flag in lang.flags:
				flags[flag] = lang

		def check(reaction, user):
			return user == ctx.message.author and str(reaction.emoji) in flags

		for flag in flags:
			await msg.add_reaction(flag)

		while True:
			try:
				reaction, user = await bot.wait_for('reaction_add', check=check, timeout=120)
			except asyncio.TimeoutError:
				break

			lang = flags[str(reaction.emoji)]
			db.set_lang(ctx.message.author.id, lang.id)
			embed = create_embed(lang)
			msg.id = reaction.message.id
			await msg.edit(embed=embed)

	elif len(command) == 2:
		help_command = lang.help_commands[command[1]]
		embed = discord.Embed(title=f'`{help_command[0]}`', description=help_command[1], colour=discord.Colour.red())
		embed.set_footer(text=f"Created by Shrubin#1866 & Chizy#0303")
		await send(ctx, embed=embed)

def create_opt_to_key(lang):
	return {'hp': lang.hp, 'atk': lang.atk, 'atk%': f'{lang.atk}%', 'er': f'{lang.er}%', 'em': lang.em,
			'phys': f'{lang.phys}%', 'cr': f'{lang.cr}%', 'cd': f'{lang.cd}%', 'elem': f'{lang.elem}%',
			'hp%': f'{lang.hp}%', 'def%': f'{lang.df}%', 'heal': f'{lang.heal}%', 'def': lang.df, 'lvl': lang.lvl}

@bot.command()
@commands.cooldown(RATE_LIMIT_N, RATE_LIMIT_TIME, commands.BucketType.user)
async def rate(ctx):
	global calls, crashes

	if DEVELOPMENT and not (ctx.channel and ctx.channel.id == DEV_CHANNEL_ID):
		return

	lang = get_lang(ctx)
	presets = get_presets(ctx) or []
	presets = {preset.name: preset.command for preset in presets}

	url = None
	if ctx.message.attachments:
		url = ctx.message.attachments[0].url

	msg = ctx.message.content.split()[1:]
	options = []
	preset = None
	for word in msg:
		if not url and validators.url(word):
			url = word
			if '.' not in url.split('?')[0].split('/')[-1]:
				if '?' in url:
					url = '.png?'.join(url.split('?'))
				else:
					url += '.png'
		elif word in presets:
			preset = word
		elif '=' in word:
			options.append(word)
		else:
			print(f'Error: Could not parse "{ctx.message.content}"')
			await send(ctx, msg=lang.err_parse)
			return

	if not url:
		await send(ctx, msg=lang.err_not_found)
		return

	if preset:
		options = presets[preset].split() + options

	opt_to_key = create_opt_to_key(lang)
	try:
		options = {opt_to_key[option.split('=')[0].lower()] : float(option.split('=')[1]) for option in options}
	except:
		print(f'Error: Could not parse "{ctx.message.content}"')
		await send(ctx, msg=lang.err_parse)
		return

	print(url)
	for i in range(RETRIES + 1):
		try:
			calls += 1
			suc, text = await ra.ocr(url, i+1, lang)

			if not suc:
				if 'Timed out' in text:
					text += f', {lang.err_try_again}'
				print(text)
				if i < RETRIES:
					continue
				await send(ctx, msg=text)
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
			score, main_score, main_weight, sub_score, sub_weight = ra.rate(level, results, options, lang)
			crashes = 0
			break

		except Exception:
			print(f'Uncaught exception\n{traceback.format_exc()}')
			if i < RETRIES:
				continue
			await send(ctx, msg=lang.err_unknown)
			if ERR_CHANNEL_ID:
				channel = bot.get_channel(ERR_CHANNEL_ID)
				emb = discord.Embed(title=f"Uncaught exception in {ctx.guild} #{ctx.channel}",description=f"""```{ctx.author} [{ctx.author.id}] • {ctx.message.content}\n\n{traceback.format_exc()}```""", color=discord.Colour.from_rgb(133, 149, 255))
				await channel.send(embed=emb)
				await channel.send(f"URL: {url}")
			crashes += 1
			if crashes >= MAX_CRASHES and HEROKU_API_KEY and HEROKU_APP_ID:
				print(f'Crashed {MAX_CRASHES} times, restarting')
				app.restart()
			return

	if not results:
		await send(ctx, msg=lang.err_unknown)
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
	msg += f'\n\n**{lang.score}: {int(score * (main_weight + sub_weight))} ({score:.2f}%)**'
	msg += f'\n{lang.main_score}: {int(main_score * main_weight)} ({main_score:.2f}%)'
	msg += f'\n{lang.sub_score}: {int(sub_score * sub_weight)} ({sub_score:.2f}%)'
	msg += f'\n\n{lang.join}'

	embed = discord.Embed(color=color)
	embed.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
	embed.add_field(name=f'{lang.art_level}: {level}', value=msg)

	await send(ctx, embed=embed)

@bot.command()
@commands.cooldown(RATE_LIMIT_N, RATE_LIMIT_TIME, commands.BucketType.user)
async def feedback(ctx):
	if DEVELOPMENT and not (ctx.channel and ctx.channel.id == DEV_CHANNEL_ID):
		return

	lang = get_lang(ctx)

	await send(ctx, msg=lang.feedback)
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

def make_f(name, lang):
	suffix = f'_{lang.id}'
	@bot.command(name=f'{name}{suffix}')
	@commands.cooldown(RATE_LIMIT_N, RATE_LIMIT_TIME, commands.BucketType.user)
	async def _f(ctx):
		await send(ctx, msg=lang.deprecated)
	return _f

# deprecated
for lang in tr.languages.values():
	_rate = make_f('rate', lang)
	_feedback = make_f('feedback', lang)

command_names = [command.name for command in bot.commands] + [alias for command in bot.commands for alias in command.aliases]

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
		loop.run_until_complete(bot.close())