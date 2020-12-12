import rate_artifact as ra
import translations as tr

import os
import sys

import discord
import traceback
import validators
from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID', 0))
DEVELOPMENT = os.getenv('DEVELOPMENT', 'False') == 'True'

bot = commands.Bot(command_prefix='-')

async def send(msg):
	print(msg)
	if CHANNEL_ID:
		channel = bot.get_channel(CHANNEL_ID)
		await channel.send(msg)

@bot.event
async def on_ready():
	global calls
	calls = 0
	await send(f'{bot.user.name} has connected to {len(bot.guilds)} servers')
	count.start()

@bot.event
async def on_resumed():
	await send(f'{bot.user.name} reconnected')

@bot.event
async def on_disconnect():
	await send(f'{bot.user.name} disconnected after {calls} calls')

@bot.event
async def on_error(event, *args, **kwargs):
	await send(f'{bot.user.name} raised an exception in {event}\n' + traceback.format_exc())

@tasks.loop(hours=24.0)
async def count():
	global calls
	if calls != 0:
		await send(f'{bot.user.name} has been called {calls} times in the past day')
	calls = 0

def create_opt_to_key(lang):
	return {lang.hp_opt: lang.hp, lang.atk_opt: lang.atk, f'{lang.atk_opt}%': f'{lang.atk}%',
			lang.er_opt: f'{lang.er}%', lang.em_opt: lang.em, lang.phys_opt: f'{lang.phys} {lang.dmg}%',
			lang.cr_opt: f'{lang.cr}%', lang.cd_opt: f'{lang.cd}%', lang.elem_opt: f'{lang.elem} {lang.dmg}%',
			f'{lang.hp_opt}%': f'{lang.hp}%', f'{lang.df_opt}%': f'{lang.df}%',
			lang.heal_opt: f'{lang.heal}%', lang.df_opt: lang.df, lang.lvl_opt: lang.lvl}

async def rate(ctx, lang):
	global calls

	options = ctx.message.content.split()[1:]
	if options and validators.url(options[0]):
		url = options[0]
		options = options[1:]
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
	suc, text = await ra.ocr(url, lang)

	if not suc:
		msg = f'{lang.err}: {text}'
		if 'Timed out' in text:
			msg += f', {lang.err_try_again}'
		print(msg)
		if not DEVELOPMENT:
			await ctx.send(msg)

	level, results = ra.parse(text, lang)
	if lang.lvl in options:
		level = int(options[lang.lvl])
		del options[lang.lvl]
	elif level == None:
		level = 20
	score, main_score, sub_score = ra.rate(level, results, options, lang)

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

	embed = discord.Embed(color=color)
	embed.add_field(name=f'{lang.art_level}: {level}', value=msg)
	embed.set_footer(text=lang.requested % ctx.message.author, icon_url=ctx.message.author.avatar_url)

	if not DEVELOPMENT:
		await ctx.send(embed=embed)
	elif CHANNEL_ID:
		channel = bot.get_channel(CHANNEL_ID)
		await channel.send(embed=embed)

@bot.command(name='rate')
async def rate_en(ctx):
	'''
	Rate an artifact against an optimal 5* artifact. Put the command and image in the same message.

	If you would like to add it to your private server use the link:
	https://discord.com/api/oauth2/authorize?client_id=774612459692621834&permissions=3072&scope=bot

	You can also use the bot by sending the command in a DM to Artifact Rater#6924.

	-rate <image/url> [lvl=<level>] [<stat>=<weight> ...]

	If you have any issues, please contact shrubin#1866 on discord or use the -feedback command.
	Source code available at https://github.com/shrubin/Genshin-Artifact-Rater

	Default weights

	ATK%, DMG%, Crit - 1
	ATK, EM, Recharge - 0.5
	Everything else - 0

	Options

	lvl: Compare to specified artifact level (default: <artifact_level>)
	-rate lvl=20

	<stat>: Set custom weights (valued between 0 and 1)
	-rate atk=1 er=0 atk%=0.5

	<stat> is any of HP, HP%, ATK, ATK%, ER (Recharge), EM, PHYS, CR (Crit Rate), CD (Crit Damage), ELEM (Elemental DMG%), Heal, DEF, DEF%
	'''
	await rate(ctx, tr.en)

@bot.command(name='rate_es')
async def rate_es(ctx):
	'''
	Rate in Spanish
	Translations provided by NeRooN#1104
	'''
	await rate(ctx, tr.es)

@bot.command(name='feedback')
async def feedback(ctx):
	'''
	Send feedback with issues or ideas for the bot. Up to one image can be sent.

	-feedback <message> [image]
	'''
	if not DEVELOPMENT:
		await ctx.send('Feedback received, please contact shrubin#1866 if you\'d like to add more details')
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

if TOKEN:
	bot.run(TOKEN)
else:
	print('Error: DISCORD_TOKEN not found')
