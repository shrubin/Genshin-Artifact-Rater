# Genshin Artifact Rater

Discord bot that rates an artifact against an optimal 5* artifact. Put the command and image in the same message.

If you would like to add it to your private server use the link: \
https://discord.com/api/oauth2/authorize?client_id=774612459692621834&permissions=19456&scope=bot

You can also use the bot by sending the command in a DM to Artifact Rater#6924.

If you have any issues, please contact shrubin#1866 on discord or use the `-feedback` command.

## Join the support server: https://discord.gg/SyGmBxds3M



## Usage

```
-rate <image/url> [lvl=<level>] [<stat>=<weight> ...]
```

#### Default Weights

ATK%, DMG%, Crit - 1 \
ATK, EM, Recharge - 0.5 \
Everything else - 0

### Options
#### Level
Compare to specified artifact level (defaults to parsed artifact level)
```
-rate lvl=20
```

#### Weights
Set custom weights (valued between 0 and 1)
```
-rate atk=1 er=0 atk%=0.5
```
\<stat> is any of HP, HP%, ATK, ATK%, ER (Recharge), EM, PHYS, CR (Crit Rate), CD (Crit Damage), ELEM (Elemental DMG%), Heal, DEF, DEF%

## Development
If you need help or want to contribute, feel free to DM shrubin#1866 or join https://discord.gg/SyGmBxds3M

### Setup
```
python3.8 -m pip install -r requirements.txt
```

Set up a bot on the Discord Developer Portal \
Go to https://ocr.space and get an API key

Store environment variables for OCR Space and Discord in `.env`
```
DISCORD_TOKEN=<token>
OCR_SPACE_API_KEY=<key>

```

## Cogs
To load cogs, make sure to create a config.toml and put the cogs in a list.
```
cogs = ["<cog name>"]
```

Optional: \
Set a Discord `CHANNEL_ID=<id>` to receive messages when the bot goes up/down \
Set `DEVELOPMENT=True` to divert all messages to `CHANNEL_ID`

### Run the bot
```
python3.8 bot.py
```

### Run one-off
Edit `url` in `rate_artifact.py`
```
python3.8 rate_artifact.py
```
