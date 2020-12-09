import rate_artifact as ra

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='-')

calls = 0

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to {[guild.name for guild in bot.guilds]}')

opt_to_key = {'hp': 'HP', 'atk': 'ATK', 'atk%': 'ATK%', 'er': 'Energy Recharge%', 'em': 'Elemental Mastery',
              'phys': 'Physical DMG%', 'cr': 'CRIT Rate%', 'cd': 'CRIT DMG%', 'elem': 'Elemental DMG%',
              'hp%': 'HP%', 'def%': 'DEF%', 'heal': 'Healing%', 'def': 'DEF', 'lvl': 'Level'}

@bot.command(name='rate')
async def rate(ctx):
    '''
    Rate an artifact against an optimal 5* artifact. Put the command and image in the same message.

    -rate <image> [lvl=<level>] [<stat>=<weight> ...]

    If you have any issues or want to use the bot in your private server, contact shrubin#1866 on discord.
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
    if not ctx.message.attachments:
        return
    options = ctx.message.content.split()[1:]
    options = {opt_to_key[option.split('=')[0].lower()] : float(option.split('=')[1]) for option in options}
    url = ctx.message.attachments[0].url
    suc, text = await ra.ocr(url)
    global calls
    calls += 1
    print(f'Calls: {calls}')
    if suc:
        level, results, results_str  = ra.parse(text)
        if not('Level' in options.keys()):
            if isinstance(level, list):
                level = 20
            options = {**options, 'Level': level}
        else:
            level = int(options['Level'])
        score, main_score, sub_score, grade_score = ra.rate(results, options)
        score_msg = f'**Rating:** {score:.2f}% ({grade_score})'
        embed = discord.Embed(color=discord.Color.blue())
        embed.add_field(name=f'Parsed Stats | Level {level}', value=f'{results_str}{score_msg}')
        embed.set_footer(text=f'Requested by {ctx.message.author}', icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        msg = f'OCR failed. Error: {text}'
        if 'Timed out' in text:
            msg += ', please try again in a few minutes'
        await ctx.send(msg)

bot.run(TOKEN)
