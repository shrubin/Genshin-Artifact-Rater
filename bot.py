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

retries = 1
calls = 0

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
			lang.er_opt: f'{lang.er}%', lang.em_opt: lang.em, lang.phys_opt: f'{lang.phys}%',
			lang.cr_opt: f'{lang.cr}%', lang.cd_opt: f'{lang.cd}%', lang.elem_opt: f'{lang.elem}%',
			f'{lang.hp_opt}%': f'{lang.hp}%', f'{lang.df_opt}%': f'{lang.df}%',
			lang.heal_opt: f'{lang.heal}%', lang.df_opt: lang.df, lang.lvl_opt: lang.lvl}

async def rate(ctx, lang):
	global calls

	options = ctx.message.content.split()[1:]
	if options and validators.url(options[0]):
		url = options[0]
		options = options[1:]
		if 'imgur' in url and '.' not in url.split('/')[-1]:
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
	for i in range(retries + 1):
		try:
			suc, text = await ra.ocr(url, lang)

			if not suc:
				if 'Timed out' in text:
					text += f', {lang.err_try_again}'
				print(text)
				if i < retries:
					continue
				if not DEVELOPMENT:
					await ctx.send(text)
				return

			level, results = ra.parse(text, lang)
			if lang.lvl in options:
				level = int(options[lang.lvl])
			elif level == None:
				level = 20
			score, main_score, sub_score = ra.rate(level, results, options, lang)
			break

		except Exception:
			print(f'Uncaught exception\n{traceback.format_exc()}')
			if i < retries:
				continue
			if not DEVELOPMENT:
				await ctx.send(lang.err_unknown)
			if CHANNEL_ID:
				channel = bot.get_channel(CHANNEL_ID)
				await channel.send(f'Uncaught exception in {ctx.guild} #{ctx.channel}\n{ctx.message.content}\n{url}\n{traceback.format_exc()}')
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

@bot.command(name='rate')
async def rate_en(ctx):
	'''
	Rate an artifact against an optimal 5* artifact. Put the command and image in the same message.

	If you are using Windows 10, you can use Shift + Windows + S and drag your cursor over the artifact, then go to discord and paste it with Ctrl+V.

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
	Valora un artefacto comparándolo con los posibles stats de un 5*. Simplemente pon el comando y adjunta la imagen en el mismo mensaje.

	Si estás usando windows 10, puedes usar Shift + Windows + S y seleccionar el artefacto, después ir a discord y pegarlo con Ctrl + V.

	Si quieres, puedes invitar al bot a tu propio servidor de discord con este link:
	https://discord.com/api/oauth2/authorize?client_id=774612459692621834&permissions=3072&scope=bot

	También puedes hablarle al bot por privado y enviarle el artefacto por ahí Artifact Rater#6924.

	-rate_es <imagen/url> [lvl=<level>] [<stat>=<valoración> ...]

	Si tienes algún problema, por favor, contacta con shrubin#1866 (inglés) en discord o usa el comando -feedback
	El código del bot lo puedes encontrar aquí https://github.com/shrubin/Genshin-Artifact-Rater
	Valores por defecto

	ATQ%, DMG%, Crit -1
	ATK, EM, Recharge - 0.5
	Lo demás - 0

	Opciones

	lvl: lo compara con el nivel especificado (por defecto: <nivel_artefacto>)
	-rate_es lvl=20

	<stat>: Te permite introducir el valor deseado (entre 0 y 1)
	-rate_es def%=1 hp%=1 atk=0

	<stat> puedes introducir: HP, HP%, ATK, ATK%, ER (recarga de energía), EM (maestría elemental), CR (prob. crit), CD (daño crit),  PHYS (daño físico), ELEM (daño elemental %), Heal, DEF, DEF%

	Translated by NeRooN#1104 | Traducción hecha por NeRooN#1104
	'''
	await rate(ctx, tr.es)

@bot.command(name='rate_de')
async def rate_de(ctx):
	'''
	Bewerten sie ein Artefakt anhand eines 5* Artefakt mit optimalen Stats.
	Fügen sie den Befehl und das Bild in die selbe Nachicht ein.

	Wenn Sie Windows 10 verwenden, können Sie Umschalt + Windows + S(Shift+Windows+S) verwenden und den Cursor über das Artefakt ziehen.
	Gehen Sie dann zu Discord und fügen Sie es mit Strg + V ein.
	
	Wenn sie den Bot auf ihrem privaten Discord Server nutzen wollen verwenden sie diesen Link:
	https://discord.com/api/oauth2/authorize?client_id=774612459692621834&permissions=3072&scope=bot
	
	Sie können den Bot auch direkt eine private Nachicht schicken mit dem Befehl an Artifact Rater#6924
	
	Befehle:	
	rate_de_de <Bild / Url> [lvl=<level>][stat=stat...]
	
	Wenn sie irgendwelche Probleme haben wenden sie sich bitte an shrubin#1866 oder benutzen sie den Befehl: -feedback ( in englisch bitte )
	
	Quellcode ist vorhanden auf Github unter:
	https://github.com/shrubin/Genshin-Artifact-Rater
	
	Standardstats:
	ANG%, DMG%, Crit -1, 
	ANG, Aufladerate, Elementarkunde 0,5
	Alles andere -0
	
	Optionen:
	
	lvl: Vergleiche mit dem angegebenen Artefaktlevel (Standard: <actifact_level>) -rate_de lvl=20
	
	<stat>: Legen sie benutzerdefinierte Stats fest (Wert zwischen 0 und 1)
	-rate_de ang=1 aufladerate=0 ang%=0,5
	<stat> ist LP, LP%, ANG, ANG%, Aufladerate, Elementarkunde, Physischbonus, KT, KSCH, Elementarbonus,  
	Heilungsbonus, VTD, VTD%
	
	Beispiel:
	-rate_de <bild/url> lvl=20
	
	Translated by NekoNeko#0440 | Übersetzung von NekoNeko#0440
	'''
	await rate(ctx, tr.de)

@bot.command(name='rate_fr')
async def rate_fr(ctx):
	'''
	Évaluez votre artefact grâce à un artefact optimal de 5 étoiles. Entrez la commande avec l’image dans le même message.

	Si vous utilisez Windows 10 vous pouvez utiliser utiliser shift + Windows +S et vous pouvez passer votre curseur par-dessus l'artefact, puis allez sur discord et le coller avec Ctrl+V.

	Si vous voulez vous joindre à notre serveur privé, utilisez ce lien :
	https://discord.com/api/oauth2/authorize?client_id=774612459692621834&permissions=3072&scope=bot
	Vous pouvez aussi utiliser le bot en envoyant un MP à Artifact Rater#6924.

	-rate_fr <image/url>  [lvl=<niveau>][<stat>=<valeur par défaut> ...]

	Si vous rencontrez un problème, merci de contacter shrubin#1866 sur discord ou d’utiliser la commande –feedback
	Code source disponible sur https://github.com/shrubin/Genshin-Artifact-Rater

	Valeur par défaut :
	ATQ%, DMG%, Crit - 1
	ATK, EM, Recharge - 0.5
	Les autres stats – 0

	Options :
	lvl: Compare à un niveau d’artefact spécifique(Défaut: < artifact_level >)
	-rate_fr lvl=20

	<stat> : Personnalise la valeur par défaut (valeur entre 0 et 1)
	-rate_fr def%=1 hp%=1 atk=0

	<stat> peut être utilisé sur toutes les statistiques : PV, PV%, ATQ, ATQ%, RE (Recharge d’énergie), ME (Maîtrise élémentaire), %CRT (Taux Critique), CRTDMG (DGT Critique),  PHYS (DGT Physique), ELEM (DGT élémentaire%), Soins, DEF, DEF%

	Translated by Miloki#3998 | Traduit par Miloki#3998
	'''
	await rate(ctx, tr.fr)

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

@bot.command(name='feedback')
async def feedback_en(ctx):
	'''
	Send feedback with issues or ideas for the bot. Up to one image can be sent.

	-feedback <message> [image]
	'''
	await feedback(ctx, tr.en)

@bot.command(name='feedback_es')
async def feedback_es(ctx):
	'''
	Envía feedback con los problemas o sugerencias para el bot. Puedes adjuntar solo una imagen.

	-feedback <mensaje> [imagen]
	'''
	await feedback(ctx, tr.es)

@bot.command(name='feedback_de')
async def feedback_de(ctx):
	'''
	Senden Sie Feedback mit Problemen oder Ideen für den Bot. Du kannst ein Bild anhängen.

	-feeback <Nachicht> [Bild]
	'''
	await feedback(ctx, tr.de)

@bot.command(name='feedback_fr')
async def feedback_fr(ctx):
	'''
	Envoyez un feedback avec les problèmes ou les idées pour le bot. Il peut être envoyé jusqu'à une image à la fois.

	-feedback <message> [image]
	'''
	await feedback(ctx, tr.fr)

if TOKEN:
	bot.run(TOKEN)
else:
	print('Error: DISCORD_TOKEN not found')
