import rate_artifact as ra
import translations as tr

import asyncio
import discord
import os
import sys
import traceback
import validators
import math

from discord.ext import commands, tasks
from dotenv import load_dotenv
from signal import SIGINT, SIGTERM

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
AUTHOR_ID = int(os.getenv('AUTHOR_ID', 0))
CHANNEL_ID = int(os.getenv('CHANNEL_ID', 0))
DEV_CHANNEL_ID = int(os.getenv('DEV_CHANNEL_ID', 0))
ERR_CHANNEL_ID = int(os.getenv('ERR_CHANNEL_ID', 0))
DEVELOPMENT = os.getenv('DEVELOPMENT', 'False') == 'True'
HEROKU_API_KEY = os.getenv('HEROKU_API_KEY')
HEROKU_APP_ID = os.getenv('HEROKU_APP_ID')
DATABASE_URL = os.getenv('DATABASE_URL')

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
SHARDS = 10

calls = 0
crashes = 0

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

bot = commands.AutoShardedBot(command_prefix=prefix, shard_count=SHARDS, activity=discord.Game(name='-help'), help_command=None)

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
	await send_internal(f'{bot.user.name} has connected to {len(bot.guilds)} servers')
	count.start()

@bot.event
async def on_resumed():
	await send_internal(f'{bot.user.name} reconnected')

@bot.event
async def on_disconnect():
	try:
		await send_internal(f'{bot.user.name} disconnected')
	except:
		pass

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
	elif dev_only:
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

@bot.command()
@commands.cooldown(RATE_LIMIT_N, RATE_LIMIT_TIME, commands.BucketType.user)
async def sets(ctx):
	if DEVELOPMENT and not (ctx.channel and ctx.channel.id == DEV_CHANNEL_ID):
		return
	if not DATABASE_URL:
		return
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
		await send(ctx, embed=embed)

def create_opt_to_key(lang):
	return {'hp': lang.hp, 'atk': lang.atk, 'atk%': f'{lang.atk}%', 'er': f'{lang.er}%', 'em': lang.em,
			'phys': f'{lang.phys}%', 'cr': f'{lang.cr}%', 'cd': f'{lang.cd}%', 'elem': f'{lang.elem}%',
			'hp%': f'{lang.hp}%', 'def%': f'{lang.df}%', 'heal': f'{lang.heal}%', 'def': lang.df, 'lvl': lang.lvl}


async def parse_url(ctx, lang):
	presets = get_presets(ctx) or []
	presets = {preset.name: preset.command for preset in presets}

	url = None
	if ctx.message.attachments:
		url = ctx.message.attachments[0].url

	msg = ctx.message.content.split()[1:]
	options = []
	for word in msg:
		if not url and validators.url(word):
			url = word
			if '.' not in url.split('?')[0].split('/')[-1]:
				if '?' in url:
					url = '.png?'.join(url.split('?'))
				else:
					url += '.png'
		elif word in presets:
			options += presets[word].split()
		elif '=' in word:
			options.append(word)
		else:
			print(f'Error: Could not parse "{ctx.message.content}"')
			await send(ctx, msg=lang.err_parse)
			return

	if not url:
		await send(ctx, msg=lang.err_not_found)
		return

	return url, options


async def parse_options(ctx, options, lang):
	opt_to_key = create_opt_to_key(lang)
	try:
		options = {opt_to_key[option.split('=')[0].lower()] : float(option.split('=')[1]) for option in options}
	except:
		print(f'Error: Could not parse "{ctx.message.content}"')
		await send(ctx, msg=lang.err_parse)
		return
	return options


async def image_to_text(ctx, url, lang):
	global crashes

	print(url)
	for i in range(RETRIES + 1):
		try:
			suc, text = await ra.ocr(url, i + 1, lang)

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
				return suc, None
			else:
				return suc, text

		except Exception:
			print(f'Uncaught exception\n{traceback.format_exc()}')
			if i < RETRIES:
				continue
			await send(ctx, msg=lang.err_unknown)
			if ERR_CHANNEL_ID:
				channel = bot.get_channel(ERR_CHANNEL_ID)
				await channel.send(f'Uncaught exception in {ctx.guild} #{ctx.channel}\n{ctx.message.content}\n{url}\n{traceback.format_exc()}')
			crashes += 1
			if crashes >= MAX_CRASHES and HEROKU_API_KEY and HEROKU_APP_ID:
				print(f'Crashed {MAX_CRASHES} times, restarting')
				app.restart()
			return False, None


async def parse_level(ctx, url, suc, text, options, lang):
	global crashes

	for i in range(RETRIES + 1):
		try:
			if not suc:
				return
			else:
				level, results = ra.parse(text, lang)
				if lang.lvl in options:
					level = int(options[lang.lvl])
				elif level == None:
					level = 20
				return level, results

		except Exception:
			print(f'Uncaught exception\n{traceback.format_exc()}')
			if i < RETRIES:
				continue
			await send(ctx, msg=lang.err_unknown)
			if ERR_CHANNEL_ID:
				channel = bot.get_channel(ERR_CHANNEL_ID)
				await channel.send(f'Uncaught exception in {ctx.guild} #{ctx.channel}\n{ctx.message.content}\n{url}\n{traceback.format_exc()}')
			crashes += 1
			if crashes >= MAX_CRASHES and HEROKU_API_KEY and HEROKU_APP_ID:
				print(f'Crashed {MAX_CRASHES} times, restarting')
				app.restart()
			return


async def rate_helper(ctx, lang, url, options, level, stats, main):
	global calls, crashes

	for i in range(RETRIES + 1):
		try:
			calls += 1
			score, main_score, main_weight, sub_score, sub_weight = ra.rate(level, stats, main, options, lang)
			crashes = 0
			break

		except Exception:
			print(f'Uncaught exception\n{traceback.format_exc()}')
			if i < RETRIES:
				continue
			await send(ctx, msg=lang.err_unknown)
			if ERR_CHANNEL_ID:
				channel = bot.get_channel(ERR_CHANNEL_ID)
				await channel.send(f'Uncaught exception in {ctx.guild} #{ctx.channel}\n{ctx.message.content}\n{url}\n{traceback.format_exc()}')
			crashes += 1
			if crashes >= MAX_CRASHES and HEROKU_API_KEY and HEROKU_APP_ID:
				print(f'Crashed {MAX_CRASHES} times, restarting')
				app.restart()
			return
	return score, main_weight, sub_weight, main_score, sub_score


@bot.command()
@commands.cooldown(RATE_LIMIT_N, RATE_LIMIT_TIME, commands.BucketType.user)
async def rate(ctx):
	if DEVELOPMENT and not (ctx.channel and ctx.channel.id == DEV_CHANNEL_ID):
		return

	lang = get_lang(ctx)

	try:
		url, options = await parse_url(ctx, lang)
		options = await parse_options(ctx, options, lang)
		suc, text = await image_to_text(ctx, url, lang)
		level, results = await parse_level(ctx, url, suc, text, options, lang)
		stats, main = ra.convert_results_to_stats(results, lang)
		score, main_weight, sub_weight, main_score, sub_score = await rate_helper(ctx, lang, url, options, level, stats, main)
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
	except Exception as e:
		print(e)
		return

	await send(ctx, embed=embed)
	if not DEVELOPMENT and ERR_CHANNEL_ID:
		channel = bot.get_channel(ERR_CHANNEL_ID)
		await channel.send(embed=embed)

@bot.command()
@commands.cooldown(RATE_LIMIT_N, RATE_LIMIT_TIME, commands.BucketType.user)
async def potential(ctx):
	if DEVELOPMENT and not (ctx.channel and ctx.channel.id == DEV_CHANNEL_ID):
		return

	lang = get_lang(ctx)

	url, options = await parse_url(ctx, lang)
	options = await parse_options(ctx, options, lang)
	suc, text = await image_to_text(ctx, url, lang)
	level, results = await parse_level(ctx, url, suc, text, options, lang)
	stats, main = ra.convert_results_to_stats(results, lang)
	del stats[main]

	lvl_remaining = 20 - level
	if lvl_remaining == 0:
		await ctx.channel.send("Artifact already at level 20!")
		return

	weights = {lang.hp: 0, lang.atk: 0.5, f'{lang.atk}%': 1, f'{lang.er}%': 0.5, lang.em: 0.5,
			   f'{lang.phys}%': 1, f'{lang.cr}%': 1, f'{lang.cd}%': 1, f'{lang.elem}%': 1,
			   f'{lang.hp}%': 0, f'{lang.df}%': 0, lang.df: 0, f'{lang.heal}%': 0}
	max_subs = {lang.atk: 19.0, lang.em: 23.0, f'{lang.er}%': 6.5, f'{lang.atk}%': 5.8,
				f'{lang.cr}%': 3.9, f'{lang.cd}%': 7.8, lang.df: 23.0, lang.hp: 299.0, f'{lang.df}%': 7.3, f'{lang.hp}%': 5.8}
	worst_stat_ratio = [f'{lang.er}%', lang.hp, f'{lang.df}%', f'{lang.cr}%', f'{lang.cd}%', lang.df, lang.em, f'{lang.hp}%', f'{lang.atk}%', lang.atk]

	# Replaces weights with options
	weights = {**weights, **options}

	num_upgrades_remaining = math.ceil(lvl_remaining/4)
	try:
		if len(results) <= 4:
			selection = max_subs.copy()
			for stat in stats:
				del selection[stat]
			max_sub = await find_highest_weighted_stat_from_selection(selection, weights, worst_stat_ratio)
			min_sub = await find_lowest_weighted_stat_from_selection(selection, weights, worst_stat_ratio)
			good_stats = dict(stats.copy(), **{max_sub: 0})
			bad_stats = dict(stats.copy(), **{min_sub: 0})
			good_stats, bad_stats, m = await calculate_potential_stats(max_sub, min_sub, 1, good_stats, bad_stats, main, lang)
			num_upgrades_remaining -= 1
			max_sub = await find_highest_weighted_stat_from_selection(good_stats, weights, worst_stat_ratio)
			min_sub = await find_lowest_weighted_stat_from_selection(bad_stats, weights, worst_stat_ratio)
		else:
			selection = stats
			max_sub = await find_highest_weighted_stat_from_selection(selection, weights, worst_stat_ratio)
			min_sub = await find_lowest_weighted_stat_from_selection(selection, weights, worst_stat_ratio)
			good_stats = stats
			bad_stats = stats

		best_stats, worst_stats, main_stat = await calculate_potential_stats(max_sub, min_sub, num_upgrades_remaining, good_stats, bad_stats, main, lang)

		max_score, main_weight, sub_weight, main_score, sub_score = await rate_helper(ctx, lang, url, options, 20, dict(best_stats, **{main: main_stat[main]}), main)
		msg = f'**Best Potential Stats**\n**{main}: {main_stat[main]}**'
		for k, v in best_stats.items():
			msg += f'\n{k}: {v}'
		msg += f'\n\n**{lang.score}: {int(max_score * (main_weight + sub_weight))} ({max_score:.2f}%)**'
		msg += f'\n{lang.main_score}: {int(main_score * main_weight)} ({main_score:.2f}%)'
		msg += f'\n{lang.sub_score}: {int(sub_score * sub_weight)} ({sub_score:.2f}%)\n\n'

		min_score, main_weight, sub_weight, main_score, sub_score = await rate_helper(ctx, lang, url, options, 20, dict(worst_stats, **{main: main_stat[main]}), main)
		msg += f'**Worst Potential Stats**\n**{main}: {main_stat[main]}**'
		for k, v in worst_stats.items():
			msg += f'\n{k}: {v}'
		msg += f'\n\n**{lang.score}: {int(min_score * (main_weight + sub_weight))} ({min_score:.2f}%)**'
		msg += f'\n{lang.main_score}: {int(main_score * main_weight)} ({main_score:.2f}%)'
		msg += f'\n{lang.sub_score}: {int(sub_score * sub_weight)} ({sub_score:.2f}%)'
		msg += f'\n\n{lang.join}'

	except Exception as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		print(exc_type, fname, exc_tb.tb_lineno)
		return

	embed = discord.Embed(color=discord.Color.dark_green())
	embed.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
	embed.add_field(name=f'{lang.art_level}: {level}', value=msg)

	await send(ctx, embed=embed)
	if not DEVELOPMENT and ERR_CHANNEL_ID:
		channel = bot.get_channel(ERR_CHANNEL_ID)
		await channel.send(embed=embed)


# Get one type of stat with the highest weighting from a selection of dictionary[stat, value]
# PARAMETERS:
# selection: Dictionary[stat, value] to find highest weighted stat from
# weights: Dictionary[stat, value] weighting to use
# ratio: List[stat] list of stats sorted from lowest score ratio to highest score ratio
# RETURN
# max_weighted_stat: stat from selection with highest weight
async def find_highest_weighted_stat_from_selection(selection: dict, weights: dict, ratio: list):
	ratio_ = ratio.copy()
	ratio_.reverse()
	stats = selection.copy()
	max_weighted_stat = stats.popitem()[0]

	for key in stats:
		if weights[key] > weights[max_weighted_stat]:
			max_weighted_stat = key
		elif weights[key] == weights[max_weighted_stat] and ratio_.index(key) > ratio_.index(max_weighted_stat):
			max_weighted_stat = key
	return max_weighted_stat


# Get one type of stat with the lowest weighting from a selection of dictionary[stat, value]
# PARAMETERS:
# selection: Dictionary[stat, value] to find lowest weighted stat from
# weights: Dictionary[Stat, value] weighting to use
# ratio: List[stat] list of stats sorted from lowest score ratio to highest score ratio
# RETURN:
# min_weighted_stat: stat from selection with lowest weight
async def find_lowest_weighted_stat_from_selection(selection: dict, weights: dict, ratio: list):
	stats = selection.copy()
	min_weighted_stat = stats.popitem()[0]

	for key in stats:
		if weights[key] < weights[min_weighted_stat]:
			min_weighted_stat = key
		elif weights[key] == weights[min_weighted_stat] and ratio.index(key) < ratio.index(min_weighted_stat):
			min_weighted_stat = key
	return min_weighted_stat


# PARAMETERS:
# max_weighted_stat: stat on artifact with highest weighting
# min_weighted_stat: stat on artifact with lowest weighting
# num_upgrades_reminaing: number of stat upgrades from current level to lvl 20
# good_stats: Dictionary[stat, value] of potential good stats artifact has
# bad_stats: Dictionary[stat, value] of potential bad stats artifact has
# main: main stat type
# RETURN:
# max_stats: Dictionary[stat, value] that would yield the highest score
# min_stats: Dictionary[stat, value] that would yield the lowest score
# main_stats: Dictionary[main stat, main stat value]
async def calculate_potential_stats(max_weighted_stat, min_weighted_stat, num_upgrades_remaining, good_stats, bad_stats, main, lang):
	tier4_sub = {lang.hp: 299, lang.atk: 19, f'{lang.atk}%': 5.8, f'{lang.er}%': 6.5, lang.em: 23,
			   f'{lang.phys}%': 0, f'{lang.cr}%': 3.9, f'{lang.cd}%': 7.8, f'{lang.elem}%': 0,
			   f'{lang.hp}%': 5.8, f'{lang.df}%': 7.3, lang.df: 23, f'{lang.heal}%': 0}
	tier1_sub = {lang.hp: 167, lang.atk: 11, f'{lang.atk}%': 3.3, f'{lang.er}%': 3.6, lang.em: 13,
			   f'{lang.phys}%': 0, f'{lang.cr}%': 2.2, f'{lang.cd}%': 4.4, f'{lang.elem}%': 0,
			   f'{lang.hp}%': 3.3, f'{lang.df}%': 4.1, lang.df: 13, f'{lang.heal}%': 0}
	max_mains = {lang.hp: 4780, lang.atk: 311.0, f'{lang.atk}%': 46.6, f'{lang.er}%': 51.8, lang.em: 187.0,
				 f'{lang.phys}%': 58.3, f'{lang.cr}%': 31.1, f'{lang.cd}%': 62.2, f'{lang.elem}%': 46.6,
				 f'{lang.hp}%': 46.6, f'{lang.df}%': 58.3, f'{lang.heal}%': 35.9}

	main_value = max_mains[main]

	best_sub_amt = round(good_stats[max_weighted_stat] + (tier4_sub[max_weighted_stat] * num_upgrades_remaining), 1)
	worst_sub_amt = round(bad_stats[min_weighted_stat] + (tier1_sub[min_weighted_stat] * num_upgrades_remaining), 1)

	max_stats = dict(good_stats, **{max_weighted_stat: best_sub_amt})
	min_stats = dict(bad_stats, **{min_weighted_stat: worst_sub_amt})
	return max_stats, min_stats, {main: main_value}


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

	try:
		loop.add_signal_handler(SIGINT, interrupt)
		loop.add_signal_handler(SIGTERM, interrupt)
	except NotImplementedError:
		pass

	try:
		loop.run_until_complete(bot.start(TOKEN))
	except KeyboardInterrupt:
		pass
	finally:
		loop.run_until_complete(bot.on_termination())
		loop.run_until_complete(bot.logout())
