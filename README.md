Discord bot that rates artifacts

### Setup
```
python3.8 -m pip install -r requirements.txt
```
Store env variables for OCR Space and Discord in `.env`

### Run the bot
```
python3.8 bot.py
```

### Run one-off
Edit `url` in `rate_artifact.py`
```
python3.8 rate_artifact.py
```

### Options
#### Level
Compare to specified artifact level (default: 20)
```
-rate lvl=<level>
```

#### Weights
Set custom weights
```
-rate hp=<weight>
```
Options: HP, HP%, ATK, ATK%, ER (Recharge), EM, PHYS, CR (Crit Rate), CD (Crit Damage), ELEM (Elemental DMG%), Heal, DEF, DEF%
