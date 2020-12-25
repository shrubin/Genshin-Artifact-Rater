class translation:
	def __init__(self):
		# 2-digit language code
		self.id = 'en'
		# 3-digit language code
		self.code = 'eng'
		# Unicode flag
		self.flags = ['🇺🇸']
		# Supported by OCR Engine 2
		self.supported = True

		self.SERVER_URL = 'https://discord.gg/SyGmBxds3M'
		self.BOT_URL = 'https://discord.com/api/oauth2/authorize?client_id=774612459692621834&permissions=19456&scope=bot'
		self.GITHUB_URL = 'https://github.com/shrubin/Genshin-Artifact-Rater'
		self.SAMPLE_URL = 'https://cdn.discordapp.com/attachments/787533173004173343/790751503475802122/unknown.png'

		# stats as they appear in-game
		self.hp = 'HP'
		self.heal = 'Healing'
		self.df = 'DEF'
		self.er = 'Energy Recharge'
		self.em = 'Elemental Mastery'
		self.atk = 'ATK'
		self.cd = 'CRIT DMG'
		self.cr = 'CRIT Rate'
		self.phys = 'Physical DMG'
		self.elem = 'Elemental DMG'
		self.anemo = 'Anemo DMG'
		self.elec = 'Electro DMG'
		self.pyro = 'Pyro DMG'
		self.hydro = 'Hydro DMG'
		self.cryo = 'Cryo DMG'
		self.geo = 'Geo DMG'
		self.dend = 'Dendro DMG'

		# text that appears below artifact stats (2-piece set)
		self.piece_set = 'Piece Set'

		# lines will be ignored if they're an exact match
		self.ignore = ['in']
		self.replace = {}

		# text for bot messages
		self.lvl = 'Level'
		self.score = 'Gear Score'
		self.main_score = 'Main Stat Rating'
		self.sub_score = 'Substat Rating'
		self.art_level = 'Artifact Level'
		self.join = f'For issues, join the [Artifact Rater Server]({self.SERVER_URL})'
		self.feedback = f'Feedback received, please join {self.SERVER_URL} if you\'d like to add more details'
		self.deprecated = 'Deprecated, please use the `-user lang <lang>` command to set your language'
		self.set_lang = 'Language set to English'
		self.set_prefix = 'Prefix set to %s'
		self.del_preset = 'Preset %s deleted'
		self.set_preset = 'Preset %s set to %s'
		self.no_presets = 'No presets found'

		# text for bot errors
		self.err = 'Error'
		self.err_not_found = 'Error: No image or url found, please make sure they were sent in the same message'
		self.err_parse = 'Error: Command cannot be parsed, please double check the format and spelling'
		self.err_try_again = 'please try again in a few minutes'
		self.err_unknown_ocr = 'Error: OCR failed with unknown error'
		self.err_unknown = 'Unknown error, try using an image from the inventory\'s artifact page'
		self.err_admin_only = 'Error: Only server admins can perform this action'
		self.err_server_only = 'Error: This action can only be performed on servers'

		# help text
		self.help_stats = '`stat` can be one of `hp`, `hp%`, `def`, `def%`, `atk`, `atk%`, `er` (Energy Recharge), `em` (Elemental Mastery), `phys` (Physical DMG), `elem` (Elemental DMG), `cr` (Crit Rate), `cd` (Crit Damage), `heal` (Healing Bonus).'

		self.help_commands = {
			'rate': [
				'-rate <image/url> [preset] [lvl=<level>] [weights]',
				f'''
				Rate an artifact against an optimal 5* artifact. Put the command and image in the same message. Try to use a clear screenshot for the best results.
				If you are on Windows 10, you can use Shift + Windows + S, drag your cursor over the artifact stats and then paste it on discord with Ctrl + V.
				This bot will use default weights (see below) unless you specify your own or select a preset. You can also specify the level you want to compare your artifact to.

				**Default weights**
				ATK%, DMG%, Crit - 1
				ATK, EM, Recharge – 0.5
				Everything else - 0

				**Parameters**
				`image/url`
				The image to be rated, either attached as a file or by putting the url in the message. [Sample]({self.SAMPLE_URL})

				`preset`
				The preset selection of weights to use. See `-presets` for which presets are available, or `-help` for how to set your own.

				`lvl`
				The level of the artifact to compare against, from 0 to 20. Sometimes the auto-detection for level is wrong, use this to correct it.

				`weights`
				The weights to use for rating this artifact. Each weight is of the format `<stat>=<value>`, where `value` is a number between 0 and 1.
				{self.help_stats}

				**Examples**
				`-rate <image> atk%=0 hp=1 er=0.5`
				`-rate <url> support lvl=4`
				'''
			],

			'feedback': [
				'-feedback <message> [image]',
				'Send direct feedback with up to one image. Use this to send ideas or report errors to help us improve the bot.'
			],

			'sets': [
				'-sets',
				'''
				View all available presets. Includes personal, server, and default presets.
				This command will display a list containing the name of the preset, where it's from, and the weights it has set.
				'''
			],

			'lang': [
				'-[user/server] lang <lang>',
				'''
				Set your language for all commands to the 2 letter language code `lang`.
				Artifact Rater will use this language for the images you send in the `-rate` command.

				Languages: English (en), Spanish (es), German (de), French (fr), Portuguese (pt), Polish (pl), Italian (it), Russian (ru), Indonesian (id), Vietnamese (vi), Japanese (ja), Traditional Chinese (tw), Simplified Chinese (cn)
				'''
			],

			'prefix': [
				'-server prefix <prefix>',
				'Change the bot\'s prefix for this server.'
			],

			'preset': [
				'-[user/server] preset <name> <weights>',
				f'''
				Create a preset called `name` to use when rating artifacts.
				If you want to check multiple artifacts with the same set of weights, you can use this command to create a preset with the desired weights.
				`weights` will be used in the `-rate` command when the preset is used. `weights` should be in the format `<stat>=<value>`, where `value` is a number between 0 and 1.
				{self.help_stats}

				**Example**
				`-user preset healer hp=0.5 hp%=1 atk%=0`
				`-rate <image> healer`

				`-[user/server] preset delete <names>`

				Delete the presets in `names` (separated by spaces).
				'''
			]
		}

		self.help_title = 'Artifact Rater Help'

		self.help_description = f'''
		**Commands**

		`{self.help_commands['rate'][0]}`
		Rate your artifact by sending an image of it. See `-help rate` for more details.

		`{self.help_commands['feedback'][0]}`
		{self.help_commands['feedback'][1]}

		`{self.help_commands['sets'][0]}`
		View all available presets.

		`-help <command>`
		Show the help message for that command. Commands: {', '.join([f'`{command}`' for command in self.help_commands])}.

		**Config**

		`-user` changes your personal config. Overrides server default settings.
		`-server` admin-only, changes the server default.

		`{self.help_commands['prefix'][0]}`
		{self.help_commands['prefix'][1]}

		`{self.help_commands['lang'][0]}`
		Set your language for all commands to the 2 letter language code `lang`. You can also use the flag reactions to change languages.

		`{self.help_commands['preset'][0]}`
		Create a preset to be used when rating artifacts. `weights` will be used in the `-rate` command when the preset is used.

		`-[user/server] preset delete <names>`
		Delete presets.
		'''

		self.source = 'Source Code'
		self.invite = 'Bot Invite'
		self.support = 'Support'
		self.github = f'[GitHub]({self.GITHUB_URL})'
		self.discord = f'[Link]({self.BOT_URL})'
		self.server = f'[Discord]({self.SERVER_URL})'

		self.help_footer = 'To change languages click on the corresponding flag below'

class en(translation):
	pass

class es(translation):
	def __init__(self):
		super().__init__()

		self.id = 'es'
		self.code = 'spa'
		self.flags = ['🇪🇸']
		self.supported = True

		self.hp = 'Vida'
		self.heal = 'Curación'
		self.df = 'DEF'
		self.er = 'Recarga de Energía'
		self.em = 'Maestría Elemental'
		self.atk = 'ATQ'
		self.cd = 'Daño CRIT'
		self.cr = 'Prob. CRIT'
		self.phys = 'Físico'
		self.elem = 'Elemental'
		self.anemo = 'Anemo'
		self.elec = 'Electro'
		self.pyro = 'Pyro'
		self.hydro = 'Hydro'
		self.cryo = 'Cryo'
		self.geo = 'Geo'
		self.dend = 'Dendro'

		self.piece_set = 'Conjunto'

		self.lvl = 'Nivel'
		self.score = 'Gear Score'
		self.main_score = 'Stat Principal'
		self.sub_score = 'Substat'
		self.art_level = 'Nivel de artefacto'
		self.join = f'Si tienes algún problema, [únete al servidor]({self.SERVER_URL})'
		self.feedback = f'Feedback recibido, por favor, únete {self.SERVER_URL} si deseas añadir más detalles'
		self.deprecated = 'Comando obsoleto, usa el comando `-user lang <idioma>` para establecer tu idioma'
		self.set_lang = 'Idioma establecido en Español'
		self.set_prefix = 'Prefijo cambiado a %s'
		self.del_preset = 'Preset %s eliminado'
		self.set_preset = 'Preset %s establecido con %s'
		self.no_presets = 'No se encuentran presets'

		self.err = 'Error'
		self.err_not_found = 'Error: No se ha encontrado ningún link o imagen, asegúrate de adjuntarla en el mismo mensaje.'
		self.err_parse = 'Error: No se reconoce el comando, asegúrate de escribirlo bien'
		self.err_try_again = 'intenta de nuevo más tarde'
		self.err_unknown_ocr = 'Error: El OCR ha fallado con un error desconocido'
		self.err_unknown = 'Error desconocido, prueba a enviar una imagen del inventario de artefactos completo.'
		self.err_admin_only = 'Error: Solo los admins del servidor pueden usar este comando'
		self.err_server_only = 'Error: Este comando solo se puede usar en servers.'

		self.help_stats = '`stat` puede ser cualquier entre: `hp`, `hp%`, `def`, `def%`, `atk`, `atk%`, `er` (Recarga de Energía), `em` (Maestría Elemental), `phys` (Daño Físico), `elem` (Daño Elemental), `cr` (Prob. Crit), `cd` (Daño Crit), `heal` (Bono de Curación).'

		self.help_commands = {
			'rate': [
				'-rate <imagen/url> [preset] [lvl=<level>] [valores]',
				f'''
				Valora un artefacto comparándolo con los posibles stats de un 5*. Pon el comando y adjunta la imagen en el mismo mensaje. Usa una imagen con la mejor calidad posible.
				Si estás usando windows 10, puedes usar Shift + Windows + S y seleccionar el artefacto, después ir a discord y pegarlo con Ctrl + V.
				El bot usará unos valores por defecto (ver abajo) excepto si le especificas tus propios valores o utilizas un preset. También puedes especificar el nivel para compararlo con uno de ese nivel.

				**Valores por defecto**
				ATK%, DMG%, Crit - 1
				ATK, EM, Recharge – 0.5
				Everything else - 0

				**Parámetros**
				`imagen/url`
				La imagen a valorar, puede ser una imagen adjunta o un link en el mismo mensaje. [Ejemplo]({self.SAMPLE_URL})

				`preset`
				La seleccion de valores para el preset a utilizar. Utiliza `-presets` para saber cuales hay disponibles o `-help` para saber como crear tu propio preset.

				`lvl`
				El nivel del artefacto con el que quieres compararlo, de 0 a 20. A veces la detección automática para el nivel falla, usa este comando para corregirlo.

				`valores`
				Los valores que quieres usar para valorar tu artefacto. Cada valor tiene que llevar el formato `<stat>=<valor>`, donde `value` es un número entre 0 y 1.
				{self.help_stats}

				**Ejemplos**
				`-rate <imagen> atk%=0 hp=1 er=0.5`
				`-rate <url> support lvl=4`
				'''
			],

			'feedback': [
				'-feedback <mensaje> [imagen]',
				'Envía feedback directo con hasta una imagen. Usa este comando para enviar ideas o reportes que nos ayuden a mejorar el bot.'
			],

			'sets': [
				'-sets',
				'''
				Te muestra una lista de todos los presets disponibles. Incluye los personales, los del servidor y los default.
				Este comando mostrará una lista con el nombre del preset, su procedencia y los valores establecidos.
				'''
			],

			'lang': [
				'-[user/server] lang <idioma>',
				'''
				Establece tu idioma para todos los comandos utilizando su código de dos letras `idioma`.
				El bot utilizará este idioma para analizar las imágenes que le envíes con el comando `-rate`.

				Idiomas: Inglés (en), Español (es), Alemán (de), Francés (fr), Portugués (pt), Polaco (pl), Italiano (it), Ruso (ru), Indonesio (id), Vietnamita (vi), Japanés (ja), Chino Tradicional (tw), Chino Simplificado(cn)
				'''
			],

			'prefix': [
				'-server prefix <prefijo>',
				'Cambia el prefijo del bot para este servidor.'
			],

			'preset': [
				'-[user/server] preset <nombre> <valores>',
				f'''
				Crea un preset `nombre` para usarlo cuando valores tus artefactos.
				Si quieres comprobar varios artefactos con los mismos valores, puedes usar este comando para crear un preset con los valores deseados.
				Se usarán los `valores` en el comando `-rate` cuando se use el preset. Los `valores` deben estar en el formato `<stat>=<valor>`, donde `valor` es un número entre 0 y 1.
				{self.help_stats}

				**Ejemplo**
				`-user preset healer hp=0.5 hp%=1 atk%=0`
				`-rate <imagen> healer`

				`-[user/server] preset delete <nombres>`

				Elimina los presets `nombres` (separado por espacios).
				'''
			]
		}

		self.help_description = f'''
		**Comandos**

		`{self.help_commands['rate'][0]}`
		Valora tu artefacto al envíar una imagen del artefacto. Utiliza `-help rate` para más detalles.

		`{self.help_commands['feedback'][0]}`
		{self.help_commands['feedback'][1]}

		`{self.help_commands['sets'][0]}`
		Te muestra una lista de todos los presets disponibles.

		`-help <comando>`
		Muestra la ayuda para el comando especificado. Comandos: {', '.join([f'`{command}`' for command in self.help_commands])}.

		**Config**

		`-user` cambia la configuración personal. Sobreescribe la configuración del servidor.
		`-server` solo para admins, cambia la configuración por defecto del servidor.

		`{self.help_commands['prefix'][0]}`
		{self.help_commands['prefix'][1]}

		`{self.help_commands['lang'][0]}`
		Establece tu idioma para todos los comandos con el código de `idioma`. También puedes usar las banderas para cambiar el idioma.

		`{self.help_commands['preset'][0]}`
		Crea un preset que se utilizará para valorar artefactos. Los `valores` se usarán en el comando `-rate` cuando se use el preset.

		`-[user/server] preset delete <nombres>`
		Eliminar presets.
		'''

		self.source = 'Código fuente'
		self.invite = 'Invitar al bot'
		self.support = 'Support'
		self.github = f'[GitHub]({self.GITHUB_URL})'
		self.discord = f'[Link]({self.BOT_URL})'
		self.server = f'[Discord]({self.SERVER_URL})'

		self.help_footer = 'Pulsa sobre la bandera correspondiente para cambiar el idioma'

class de(translation):
	def __init__(self):
		super().__init__()

		self.id = 'de'
		self.code = 'ger'
		self.flags = ['🇩🇪']
		self.supported = True

		self.hp = 'LP'
		self.heal = 'Heilungsbonus'
		self.df = 'VTD'
		self.er = 'Aufladerate'
		self.em = 'Elementarkunde'
		self.atk = 'ANG'
		self.cd = 'KSCH'
		self.cr = 'KT'
		self.phys = 'Physischer SCH-Bonus'
		self.elem = 'Elementarer Schaden'
		self.anemo = 'Anemo SCH-Bonus'
		self.elec = 'Elek SCH-Bonus'
		self.pyro = 'Pyro SCH-Bonus'
		self.hydro = 'Hydro SCH-Bonus'
		self.cryo = 'Cryo SCH-Bonus'
		self.geo = 'Geo SCH-Bonus'
		self.dend = 'Dendro SCH-Bonus'

		self.piece_set = 'Set mit 2 Teilen'

		self.lvl = 'Level'
		self.score = 'Gear Bewertung'
		self.main_score = 'Haupt-Stat'
		self.sub_score = 'Unter-Stat'
		self.art_level = 'Artifakt Level'
		self.join = f'Bei Problemen join dem Discord [Artifact Rater Server]({self.SERVER_URL})'
		self.feedback = f'Feedback erhalten, bitte joine {self.SERVER_URL} wenn du weitere Details hinzufügen möchtest'
		self.title = 'Artifact Rater Bot Hilfe'
		self.change = 'Um die Sprache zu ändern klick auf die dazugehörige Flagge unten.'
		self.deprecated = 'Veraltet, verwenden Sie bitte den Befehl `-user lang <lang>`, um Ihre Sprache festzulegen'
		self.set_lang = 'Sprache geändert auf Deutsch'
		self.set_prefix = 'Voreinstellung geändert zu %s'
		self.del_preset = 'Voreinstellung %s gelöscht'
		self.set_preset = 'Voreinstellung %s geändert zu %s'
		self.no_presets = 'Keine Voreinstellung gefunden'

		self.err = 'Fehler'
		self.err_not_found = 'Fehler: Kein Bild oder URL gefunden, bitte stelle sicher das sich das Bild in der selben Nachicht befindet'
		self.err_parse = 'Fehler: Kein Befehl gefunden, bitte schau das du ihn richtig und im korrekten Format geschrieben hast'
		self.err_try_again = 'bitte versuche es in ein paar Minuten nochmal'
		self.err_unknown_ocr = 'Fehler: OCR fehlgeschlagen mit unbekanntem Fehler'
		self.err_unknown = 'Unbekannter Fehler, verwende ein Bild von der Inventar Artefakt Seite'
		self.err_admin_only = 'Fehler: Nur Serveradministratoren können diese Aktion ausführen'
		self.err_server_only = 'Fehler: Diese Aktion kann nur auf Servern ausgeführt werden'

		self.help_stats = '`stat` kann einer von den folgenden sein `hp`, `hp%`, `def`, `def%`, `atk`, `atk%`, `er` (Aufladerate), `em` (Elementarkunde), `phys` (Physischer Schaden), `elem` (Elementarer Schaden), `cr` (Krit Rate), `cd` (Krit Schaden), `heal` (Heilungsbonus).'

		self.help_commands = {
			'rate': [
				'-rate <Bild/Link> [preset] [lvl=<Level>] [Stat]',
				f'''
				Bewerten sie ein Artefakt anhand eines 5* Artefakt mit optimalen Stats. Fügen sie den Befehl und das Bild in die selbe Nachicht ein.
				Wenn Sie Windows 10 verwenden, können Sie Umschalt + Windows + S(Shift+Windows+S) verwenden und den Cursor über das Artefakt ziehen. Gehen Sie dann zu Discord und fügen Sie es mit Strg + V ein.
				ieser Bot verwendet Standardgewichte (siehe unten), es sei denn, Sie geben Ihre eigenen an oder wählen eine Voreinstellung aus. Sie können auch das Level angeben, mit der Sie Ihr Artefakt vergleichen möchten.
				**Standardstats:**
				ANG%, DMG%, Crit -1,
				ANG, Aufladerate, Elementarkunde 0,5
				Alles andere -0
				**Optionen**
				`Bild/Link`
				Das zu bewertende Bild wird entweder als Datei oder durch Einfügen der URL in die Nachricht angehängt. [Sample]({self.SAMPLE_URL})
				`preset`
				Die voreingestellte Auswahl der zu verwendenden Stats. Siehe `-presets`, für aktuell verfügbare Presets, oder` -help`, wie zu sehen wie sie Ihre eigenen Presets festlegen können.
				`lvl`
				Das Level des Artefakts, mit der verglichen werden soll, liegt zwischen 0 und 20. Manchmal ist die automatische Erkennung des Levels falsch. Verwenden Sie diese Option, um es zu korrigieren.
				`weights`
				Die Stats, die zur Bewertung dieses Artefakts verwendet werden sollen. Jeder Stat hat das Format "<stat> = <wert>", wobei "wert" eine Zahl zwischen 0 und 1 ist
				{self.help_stats}
				**Beispiele**
				`-rate <bild> atk%=0 hp=1 er=0.5`
				`-rate <Link> support lvl=4`
				'''
			],

			'feedback': [
				'-feedback <Nachicht> [Bild]',
				'Senden Sie Feedback mit Problemen oder Ideen für den Bot. Du kannst ein Bild anhängen.'
			],

			'sets': [
				'-sets',
				'''
				Alle verfügbaren Voreinstellungen anzeigen. Enthält Personal-, Server- und Standardvoreinstellungen.
				Dieser Befehl zeigt eine Liste mit dem Namen der Voreinstellungen, woher sie stammen, und den eingestellten Stats an.
				'''
			],

			'lang': [
				'-[user/server] lang <Sprache>',
				'''
				Stellen Sie Ihre Sprache für alle Befehle auf den 2-Buchstaben-Sprachcode `lang` ein
				Artifact Rater verwendet diese Sprache für die Bilder, die Sie mit dem Befehl `-rate` senden.
				Verfügbare Sprachen: Englisch (en), Spanisch (es), Deutsch (de), Französisch (fr), Portugiesisch (pt), Polnisch (pl), Italian (it), Russisch (ru), Indonesisch (id), Vietnamesisch (vi), Japanisch (ja), Traditionelles Chinesisch  (tw), Vereinfachtes Chinesisch (cn)
				'''
			],

			'prefix': [
				'-server prefix <prefix>',
				'Ändern Sie das Bot-Präfix für diesen Server.'
			],

			'preset': [
				'-[user/server] preset <name> <stat>',
				f'''
				Erstellen Sie eine Voreinstellung mit dem Namen `name`, die beim Bewerten von Artefakten verwendet werden soll.
				Wenn Sie mehrere Artefakte mit denselben Voreinstellungen von Stats überprüfen möchten, können Sie mit diesem Befehl eine Voreinstellung mit den gewünschten Stats erstellen
				"Stats" werden im Befehl "-rate" verwendet, wenn die Voreinstellung verwendet wird. `Stats` sollte das Format` <stat> = <wert> `haben, wobei` wert` eine Zahl zwischen 0 und 1 ist.
				{self.help_stats}
				**Beispiele**
				`-user preset healer hp=0.5 hp%=1 atk%=0`
				`-rate <bild> healer`
				`-[user/server] preset delete <name>`
				Lösche Voreinstellungen mit den Namen `names` (durch Leerzeichen trennen).
				'''
			]
		}

		self.help_title = 'Artifact Rater Hilfe'

		self.help_description = f'''
		**Commands**
		`{self.help_commands['rate'][0]}`
		Bewerten Sie Ihr Artefakt, indem Sie ein Bild davon senden. Weitere Informationen finden Sie unter `-help rate`.
		`{self.help_commands['feedback'][0]}`
		{self.help_commands['feedback'][1]}
		`{self.help_commands['sets'][0]}`
		Zeige alle verfügbaren Voreinstellungen
		`-help <command>`
		Zeigen Sie die Hilfe für diesen Befehl an. Befehle: {', '.join([f'`{command}`' for command in self.help_commands])}.
		**Config**
		`-user` ändert Ihre persönliche Konfiguration. Überschreibt die Standardeinstellungen des Servers.
		`-server` Nur für Administratoren, ändert die Server-Standardeinstellung.
		`{self.help_commands['prefix'][0]}`
		{self.help_commands['prefix'][1]}
		`{self.help_commands['lang'][0]}`
		Stellen Sie Ihre Sprache für alle Befehle auf den 2-Buchstaben-Sprachcode `lang` ein. Sie können auch die Flag-Reaktionen verwenden, um die Sprache zu ändern.
		`{self.help_commands['preset'][0]}`
		Erstellen Sie eine Voreinstellung, die beim Bewerten von Artefakten verwendet werden soll. "Stats" werden im Befehl `-rate` verwendet, wenn die Voreinstellung verwendet wird.
		`-[user/server] preset delete <names>`
		Löscht Voreinstellungen.
		'''

		self.source = 'Source Code'
		self.invite = 'Bot Invite'
		self.support = 'Support'
		self.github = f'[GitHub]({self.GITHUB_URL})'
		self.discord = f'[Link]({self.BOT_URL})'
		self.server = f'[Discord]({self.SERVER_URL})'

		self.help_footer = 'Um die Sprache zu ändern, klicken Sie auf die entsprechende Flagge unten'

class fr(translation):
	def __init__(self):
		super().__init__()

		self.id = 'fr'
		self.code = 'fre'
		self.flags = ['🇫🇷']
		self.supported = True

		self.hp = 'PV'
		self.heal = 'Bonus de soins'
		self.df = 'DÉF'
		self.er = 'Recharge d\'énergie'
		self.em = 'Maîtrise élémentaire'
		self.atk = 'ATQ'
		self.cd = 'DGT CRIT'
		self.cr = 'Taux CRIT'
		self.phys = 'Bonus de DGT physiques'
		self.elem = 'Bonus de DGT élémentaire'
		self.anemo = 'Bonus de DGT Anémo'
		self.elec = 'Bonus de DGT Électro'
		self.pyro = 'Bonus de DGT Pyro'
		self.hydro = 'Bonus de DGT Hydro'
		self.cryo = 'Bonus de DGT Cryo'
		self.geo = 'Bonus de DGT Géo'
		self.dend = 'Bonus de DGT Dendro'

		self.piece_set = 'Set de pièces'

		self.lvl = 'Niveau'
		self.score = 'Puissance de l\'artefact'
		self.main_score = '% Stat principale'
		self.sub_score = '% Stats secondaires'
		self.art_level = 'Niveau d\'Artefact'
		self.join = f'Si vous rencontrez d\'autres problemes, [rejoignez le serveur]({self.SERVER_URL}) Artifact Rater'
		self.feedback = f'Si vous avez un retour d\'informations, s\'il vous plait rejoignez {self.SERVER_URL} si vous voulez rajouter plus de détails'
		self.deprecated = 'Si ça ne fonctionne pas, s\'il vous plaît utilisez la commande -user lang <lang> pour la définir à votre langue'
		self.set_lang = 'Langue définie en Français'
		self.set_prefix = 'Préfix définis en %s'
		self.del_preset = 'Preset %s supprimer'
		self.set_preset = 'Preset %s remplacer par %s'
		self.no_presets = 'Pas de presets trouvés'

		self.err = 'Erreur'
		self.err_not_found = 'Erreur: Aucune image ou url n\'a été trouvée, s\'il vous plait assurez vous qu\'elle a était envoyée avec le message'
		self.err_parse = 'Erreur: La commande ne peut pas être analyser, vérifier le format et l\'orthographe'
		self.err_try_again = 'Merci de réessayer dans quelques minutes'
		self.err_unknown_ocr = 'Erreur: OCR a échoué a cause d\'une erreur inconnue'
		self.err_unknown = 'Erreur inconnue, essayer d\'utiliser une image d\'artefact venant de la page d\'inventaire'
		self.err_admin_only = 'Erreur: Seuls les admins peuvent effectuer cette action'
		self.err_server_only = 'Erreur: Cette action ne peut être effectué que sur le serveur'

		self.help_stats = '`stat` peut être utilisé sur toutes les statistiques : `hp`, `hp%`, `def`, `def%`, `atk`, `atk%`, `er` (Recharge d’énergie), `em` (Maîtrise élémentaire), `phys` (DGT Physique), `elem` (DGT élémentaire%), `cr` (Taux Critique), `cd` (DGT Critique), `heal`.'

		self.help_title = 'Aide Artifact Rater Bot'

		self.help_description = f'''
		Si vous voulez vous joindre à notre serveur privé, utilisez ce [lien](%s)
		Vous pouvez aussi utiliser le bot en envoyant un MP à Artifact Rater#6924.

		`-rate <image/url>  [lvl=<niveau>][<stat>=<valeur par défaut> ...]`
		Évaluez votre artefact grâce à un artefact optimal de 5 étoiles. Entrez la commande avec l’image dans le même message.
		Si vous utilisez Windows 10 vous pouvez utiliser utiliser shift + Windows +S et vous pouvez passer votre curseur par-dessus l'artefact, puis allez sur discord et le coller avec Ctrl+V.

		Valeur par défaut :
		ATQ%, DMG%, Crit - 1
		ATK, EM, Recharge - 0.5
		Les autres stats – 0
		Options :
		lvl: Compare à un niveau d’artefact spécifique(Défaut: < artifact_level >)
		-rate lvl=20
		<stat> : Personnalise la valeur par défaut (valeur entre 0 et 1)
		-rate def%=1 hp%=1 atk=0
		{self.help_stats}

		`-feedback <message> [image]`
		Envoyez un feedback avec les problèmes ou les idées pour le bot. Il peut être envoyé jusqu\'à une image à la fois.
		'''

		self.help_footer = 'Pour changer la langue du bot, cliquez sur le drapeau correspondant'

class vi(translation):
	id = 'vi'
	code = 'vie'
	flags = ['🇻🇳']
	supported = True

	hp = 'HP'
	heal = 'Tăng Trị Liệu'
	df = 'Phòng Ngự'
	er = 'Hiệu Quả Nạp Nguyên Tố'
	em = 'Tinh Thông Nguyên Tố'
	atk = 'Tấn Công'
	cd = 'ST Bạo Kích'
	cr = 'Tỷ Lệ Bạo Kích'
	phys = 'Tăng Sát Thương Vật Lý'
	elem = 'Tăng ST Nguyên Tố'
	anemo = 'Tăng ST Nguyên Tố Phong'
	elec = 'Tăng ST Nguyên Tố Lôi'
	pyro = 'Tăng ST Nguyên Tố Hỏa'
	hydro = 'Tăng ST Nguyên Tố Thủy'
	cryo = 'Tăng ST Nguyên Tố Băng'
	geo = 'Tăng ST Nguyên Tố Nham'
	dend = 'Tăng ST Nguyên Tố Thảo'

	piece_set = 'Bộ 2 món'

	lvl = 'Cấp Độ'
	score = 'Điểm Trang Bị'
	main_score = 'Điểm Dòng Chính'
	sub_score = 'Điểm Dòng Phụ'
	art_level = 'Cấp Độ Thánh Di Vật'
	join = 'Để báo cáo vấn đề gặp phải, hãy tham gia [Artifact Rater Server]%s'
	feedback = 'Góp ý đã được tiếp nhận, hãy tham gia %s nếu bạn muốn cung cấp thêm chi tiết'
	title = 'Trợ giúp: Bot Đánh Giá Thánh Di Vật'
	change = 'Để thay đổi ngôn ngữ hãy bấm vào lá cờ bên dưới'
	deprecated = 'Lệnh này không còn khả dụng, hãy dùng lệnh -user lang <ngôn ngữ> để đặt ngôn ngữ'
	set_lang = 'Đã chuyển ngôn ngữ sang tiếng Việt'
	set_prefix = 'Đã đặt tiền tố %s'
	del_preset = 'Đã xóa preset %s'
	set_preset = 'Đã đặt preset %s với giá trị %s'
	no_presets = 'Không tìm thấy preset nào'

	err = 'Lỗi'
	err_not_found = 'Lỗi: Không tìm thấy ảnh hoặc link, 1 trong 2 phải được gửi chung trong cùng 1 tin nhắn'
	err_parse = 'Lỗi: Không thể xử lý lệnh, vui lòng kiểm tra lại định dạng và chính tả'
	err_try_again = 'hãy thử lại trong vài phút nữa'
	err_unknown_ocr = 'Lỗi: OCR đọc ảnh thất bại lỗi không xác định'
	err_unknown = 'Lỗi không xác định, hãy sử dụng ảnh chụp trong Túi > Thánh Di Vật'
	err_admin_only = 'Lỗi: Chỉ có admin máy chủ mới có thể thực hiện hành động này'
	err_server_only = 'Lỗi: Chỉ có thể thực hiện hành động này trên máy chủ'

	help_description = '''Nếu muốn thêm vào máy chủ riêng hãy vào [link](%s)
	Bạn cũng có thể sử dụng bot bằng cách gửi lệnh qua tin nhắn riêng đến Artifact Rater#6924.'''

	help_source = '''Nếu bạn có vấn đè gì, hãy liên lạc với shrubin#1866 trên discord hoặc dùng lệnh -feedback.
	Mã nguồn mở có sẵn tại [GitHub](%s)'''

	help_feedback_name = '-feedback <nội dung> [ảnh]'
	help_feedback_value = 'Gửi góp ý về các vấn đề hoặc đóng góp ý tưởng cho bot. Có thể gửi tối đa 1 tấm ảnh.'

	help_rate_name = '-rate_vi <ảnh/link> [lvl=<cấp độ>] [<chỉ số>=<hệ số> ...]'
	help_rate_value = '''\
	Đánh giá thánh di vật dựa trên một thánh di vật 5* tối ưu. Đặt dòng lệnh và ảnh chụp trong cùng 1 tin nhắn.

	Nếu sử dụng Windows 10, nhấn phím Shift + Windows + S và vẽ hình chữ nhật bao quanh vùng thông tin, sau đó qua discord và dán bằng phím Ctrl+V.

	Hệ số mặc định
	ATK%, DMG%, Crit - 1
	ATK, EM, Recharge - 0.5
	Còn lại - 0

	Tùy chọn
	lvl: So sánh với cấp độ thánh di vật được cung cấp (mặc định: <artifact_level>)
	-rate_vi lvl=20
	<stat>: Nhập hệ số tùy chọn (giá trị từ 0 tới 1)
	-rate_vi atk=1 er=0 atk%=0.5
	<stat> là 1 trong những giá trị sau: HP, HP%, ATK, ATK%, ER (hồi năng lượng), EM (tinh thông nguyên tố), PHYS (ST vật lý), CR (tỉ lệ bạo kích), CD (ST bạo kích), ELEM (ST nguyên tố%), Heal (trị thương), DEF, DEF% (phòng thủ)
	'''

class pt(translation):
	def __init__(self):
		super().__init__()

		self.id = 'pt'
		self.code = 'por'
		self.flags = ['🇵🇹', '🇧🇷']
		self.supported = True

		self.hp = 'Vida'
		self.heal = 'Bônus de Cura'
		self.df = 'DEF'
		self.er = 'Recarga de Energia'
		self.em = 'Proficiência Elemental'
		self.atk = 'ATQ'
		self.cd = 'Dano Crítico'
		self.cr = 'Taxa Crítica'
		self.phys = 'Bônus de Dano Físico'
		self.elem = 'Bônus de Dano Elemental'
		self.anemo = 'Bônus de Dano Anemo'
		self.elec = 'Bônus de Dano Electro'
		self.pyro = 'Bônus de Dano Pyro'
		self.hydro = 'Bônus de Dano Hydro'
		self.cryo = 'Bônus de Dano Cryo'
		self.geo = 'Bônus de Dano Geo'
		self.dend = 'Bônus de Dano Dendro'

		self.piece_set = 'Conjunto'

		self.lvl = 'Nível'
		self.score = 'Qualidade do Artefato'
		self.main_score = 'Nota Status Principal'
		self.sub_score = 'Nota Substats'
		self.art_level = 'Nível do Artefato'
		self.join = f'Se encontrar problemas, junte-se ao [Artifact Rater Server]({self.SERVER_URL})'
		self.feedback = f'Feedback recebido, por favor junte-se ao servidor se quiser adicionar mais detalhes: {self.SERVER_URL}'
		self.deprecated = 'Descontinuado, por favor user o comando `-user lang <idioma>` para definir seu idioma'
		self.set_lang = 'Idioma definido para português'
		self.set_prefix = 'Prefixo definido para %s'
		self.del_preset = 'Predefinição %s deletada'
		self.set_preset = 'Predefinição %s definida para %s'
		self.no_presets = 'Nenhuma predefinição encontrada'

		self.err = 'Erro'
		self.err_not_found = 'Erro: Nenhuma imagem ou url encontrada, certifique-se de que foram enviadas na mesma mensagem'
		self.err_parse = 'Erro: Comando não pôde ser executado, por favor cheque a formatação e a ortografia'
		self.err_try_again = 'por favor tente novamente em alguns minutos'
		self.err_unknown_ocr = 'Erro: OCR falhou com um erro desconhecido'
		self.err_unknown = 'Erro desconhecido, tente usar uma imagem da página de artefatos'
		self.err_admin_only = 'Erro: Apenas administradores do servidor podem realizar essa ação'
		self.err_server_only = 'Erro: Essa ação só pode ser executada em servidores'

		self.help_stats = '`status`é qualquer um dos atributos: `hp`, `hp%`, `atk`, `atk%`, `er` (Recarga de Energia), `em`(Maestria Elemental),`phys`(Bônus de Dano Físico%), `cr` (Taxa Crítica), `cd` (Dano Crítico), `elem` (Bônus de Dano Elemental%), `heal`, `def`, `def%`'

		self.help_commands = {
			'rate': [
				'-rate <imagem/url> [predefinição] [lvl=<nível>] [peso]',
				f'''
				Avalia um artefato em comparação com um artefato perfeito 5*. Coloque o comando e a imagem na mesma mensagem.
				Tente utilizar uma captura de tela bem clara para melhores resultados.
				Se estiver usando Windows 10, você pode usar Shift + Windows + S e arrastar o cursor sobre o artefato, depois vá para o discord e cole com Ctrl+V.
				Esse bot vai utilizar os pesos padrão(veja abaixo) a menos que você defina os seus próprios ou seleciona um predefinido.  Você também pode especificar o nível do artefator com o qual você quer comparar o seu.
				**Pesos Padrão**
				ATQ%, DMG%, Crit - 1
				ATQ, ME, Recarga – 0.5
				Todo o resto - 0
				**Parâmetros**
				`imagem/url`
				A imagem a ser avaliada, ou anexada como arquivo ou colocando a url na mensagem. [Exemplo]({self.SAMPLE_URL})
				`predefinição`
				A predefinição de pesos selecionada para uso. Veja `-predefinições` para saber quais estão disponíveis, ou ´help´ para saber como criar suas próprias.
				`nível`
				O nível do artefato para comparar com o seu, de 0 a 20. Ás vezes a detecção automática de nível está errada, use esse parâmetro para corrigir.
				`pesos`
				Os pesos que serão usados para avaliar esse artefato. Cada peso é no formato de `<status>=<valor>`, onde ´valor´ é um número entre 0 e 1.
				{self.help_stats}
				**Exemplos**
				`-rate <imagem> atk%=0 hp=1 er=0.5`
				`-rate <url> support lvl=4`
				'''
			],

			'feedback': [
				'-feedback <mensagem> [imagem]',
				'Use para mandar um feedback direto de até uma imagem. Use para mandar ideias ou reportar erros para nos ajudar a melhorar o bot.'
			],

			'sets': [
				'-sets',
				'''
				Mostra todas predefinições disponíveis. Inclui pessoais, do servidor e padrão.
				Esse comando vai mostrar uma lista contendo o nome da predefinição, de onde ela veio, e os pesos que estão definidos.
				'''
			],

			'lang': [
				'-[user/server] lang <idioma>',
				'''
				Define seu idioma para todos os comandos para o código de 2 letras de linguagem `idioma`.
				Artifact Rater irá usar esse idioma para as imagens que você enviar para o comando `-rate`.
				Idiomas: English (en), Spanish (es), German (de), French (fr), Portuguese (pt), Polish (pl), Italian (it), Russian (ru), Indonesian (id), Vietnamese (vi), Japanese (ja), Traditional Chinese (tw), Simplified Chinese (cn)
				'''
			],

			'prefix': [
				'-server prefix <prefixo>',
				'Muda o prefixo do bot para esse servidor.'
			],

			'preset': [
				'-[user/server] preset <nome> <pesos>',
				f'''
				Cria uma predefinição chamada `nome` para usar ao avaliar artefatos.
				Se você quiser checar múltiplos artefatos como o mesmo conjunto de pesos, você pode usar esse comando para criar uma predefinição com os pesos desejados.
				`pesos` vai ser usado no comando `-rate` quando a predefinição for utilizada. `pesos` deve estar no formarto `<status>=<valor>`, onde `valor` é um número entre 0 e 1.
				{self.help_stats}
				**Exemplo**
				`-user preset healer hp=0.5 hp%=1 atk%=0`
				`-rate <imagem> healer`
				`-[user/server] preset delete <nomes>`
				Exclui a definição em `nomes` (separado por espaço.).
				'''
			]
		}

		self.help_title = 'Ajuda do Artifact Rater'

		self.help_description = f'''
		**Comandos**
		`{self.help_commands['rate'][0]}`
		Avalia o arterfato mandando uma imagem do mesmo. Veja `-help rate` para mais detalhes.
		`{self.help_commands['feedback'][0]}`
		{self.help_commands['feedback'][1]}
		`{self.help_commands['sets'][0]}`
		Mostra todas predefinições disponíveis.
		`-help <command>`
		Mostra a ajuda para esse comando. Commandos: {', '.join([f'`{command}`' for command in self.help_commands])}.
		**Configurações**
		`-user` Muda suas configurações pessoais. Substitui os padrões do servidor.
		`-server` Apenas para administradores, muda os padrões do servidor.
		`{self.help_commands['prefix'][0]}`
		{self.help_commands['prefix'][1]}
		`{self.help_commands['lang'][0]}`
		Define seu idioma para todos os comandos para o código de 2 letras de linguagem `idioma`. Você também pode usar as bandeiras de reações para mudar o idioma.
		`{self.help_commands['preset'][0]}`
		Cria predefinições para utilizar quando avaliar artefatos.
		`pesos` serão usados no comando `-rate` quando a predefinição for utilizada.
		`-[user/server] preset delete <nomes>`
		Exclui predefinições.
		'''

		self.source = 'Código-fonte'
		self.invite = 'Convite do bot'
		self.support = 'Suporte'
		self.github = f'[GitHub]({self.GITHUB_URL})'
		self.discord = f'[Link]({self.BOT_URL})'
		self.server = f'[Discord]({self.SERVER_URL})'

		self.help_footer = 'Para mudar o idioma selecione a bandeira abaixo.'

class ja(translation):
	id = 'ja'
	code = 'jpn'
	flags = ['🇯🇵']
	supported = False

	hp = 'HP'
	heal = '治癒効果'
	df = '防御力'
	er = '元素チャージ効率'
	em = '元素熟知'
	atk = '攻撃力'
	cd = '会心ダメージ'
	cr = '会心率'
	phys = '物理ダメージ'
	elem = '元素ダメージ'
	anemo = '風元素ダメージ'
	elec = '雷元素ダメージ'
	pyro = '炎元素ダメージ'
	hydro = '水元素ダメージ'
	cryo = '氷元素ダメージ'
	geo = '岩元素ダメージ'
	dend = '草元素ダメージ'

	piece_set = '2セット'

	replace = {'カ': '力'}

	lvl = 'レベル'
	score = '装備スコア'
	main_score = 'メインステータス評価'
	sub_score = 'サブステータス評価'
	art_level = '聖遺物レベル'
	join = '[公式サーバー]%sに参加する'
	feedback = 'フィードバックを受け取りました。詳細を追加したい場合は、 %sに参加して下さい。'

	err = 'エラー'
	err_not_found = 'エラー：画像またはURLが見つかりませんでした。同じメッセージで送信されたことを確認してください。'
	err_parse = 'エラー：コマンドを解析できません。形式とスペルを再確認してください。'
	err_try_again = 'エラー：数分後にもう一度お試しください。'
	err_unknown_ocr = 'エラー：OCRが不明なエラーで失敗しました。'
	err_unknown = '不明なエラーが発生しました。インベントリの聖遺物ページのイメージを使用してみてください。'

	help_description = '''自分のプライベートサーバーに追加する場合は、次の[リンク](%s)を使用して下さい
	さらに、次のコマンドをArtifact Rater#6924にダイレクトメッセージ（D M）を送ると、BOT も使えます。'''

	help_source = '''問題がある場合は、ディスコードでshrubin#1866に連絡するか、英語の -feedbackコマンドを使って下さい。
	ソースコードをご覧になりたい場合は、こちらへ [GitHub](%s)'''

	help_feedback_name = '-feedback <メッセージ> [イメージ]'
	help_feedback_value = 'BOTの問題やアイデアについてフィードバックを送信します。 最大1つの画像を送信できます。'

	help_rate_name = '-rate_ja <image/url> [lvl=<レベル>] [<stat>=<デフォルトの重み付け> ...]'
	help_rate_value = '''\
	自分の聖遺物を最適な５＊聖遺物と比べます。同じメッセージにコマンドとイメージ両方を入れて下さい。
	Windows 10を使っている場合は、Shift + Windows + Sを押すながら聖遺物の上にカーソルをドラッグし、ディスコードを開くと、Ctrl + Vで貼り付けることができます。

	デフォルトの重み付け
	攻撃力％、各種ダメージバフ％、会心ダメージと会心率 – 1
	攻撃力、元素熟知、元素チャージ効率 – 0.5
	他 – 0
	選択肢
	lvl: 特定の聖遺物レベルと比較する (デフォルト: <聖遺物_レベル>)
	-rate_ja lvl=20
	<stat>: カスタムの重み付けを設定します（値は0から1の間）
	-rate_ja 攻撃力=1 元素チャージ効率=0 攻撃力％=0.5
	<stat> においてHP、HP%、攻撃力、攻撃力％、元素チャージ効率 、元素熟知、物理ダメージ、会心率、会心ダメージ、元素ダメージ、治癒効果、防御力を使えることができます。
	Translated by plastiquedoll#1393 | plastiquedoll#1393によって翻訳されました。
	'''

# Text only, no game translation
class pl(translation):
	id = 'pl'
	code = 'pol'
	flags = ['🇵🇱']
	supported = True

	lvl = 'Level'
	score = 'Wynik ogólny'
	main_score = 'Ocena głównej statystyki'
	sub_score = 'Ocena podstatystyk'
	art_level = 'Poziom artefaktów'
	join = 'W przypadku problemów, dołącz na [Artifact Rater Server]%s'
	feedback = 'Otrzymaliśmy feedback, dołącz na serwer %s jeżeli chciałbyś dodać więcej szczegółów.'
	title = 'Artifact Rater Bot Help'
	change = 'Aby zmienić język kliknij na odpowiednią poniższą flagę'
	deprecated = 'Przestarzałe, użyj komendy -user lang <język> aby ustawić używany język'
	set_lang = 'Ustawiono język na polski'
	set_prefix = 'Ustawiono prefix na %s'
	del_preset = 'Ustawienia %s zostały usunięte'
	set_preset = 'Ustawienia %s zmienione na %s'
	no_presets = 'Nie znaleziono ustawień'

	err = 'Błąd'
	err_not_found = 'Błąd: Nie znaleziono URL ani obrazu, upewnij się czy zostały wysłane w tej samej wiadomości.'
	err_parse = 'Błąd: Komenda nie może zostać sparsowana, sprawdź jeszcze raz jej format i pisownię.'
	err_try_again = 'spróbuj ponownie za kilka minut'
	err_unknown_ocr = 'Błąd: OCR zawiódł z nieznanym błędem.'
	err_unknown = 'Nieznany błąd, spróbuj użyć zrzutu ekranu zawierającego zakładkę z artefaktami w ekwipunku'
	err_admin_only = 'Błąd: Ta akcja może zostać wykonana wyłącznie przez admina.'
	err_server_only = 'Błąd: Ta akcja może zostać wykonana wyłącznie na serwerach.'

	help_description = '''Jeżeli chcesz go dodać do swojego serwera, użyj tego [linku](%s)
	Możesz również użyć tego bota poprzez wysłanie komendy w prywatnej wiadomości do Artifact Rater#6924.'''

	help_source = '''Jeżeli uświadczyłeś problemów, skontaktuj się z shrubin#1866 na discordzie albo użyj komendy -feedback.
	Kod źródłowy dostępny na [GitHub](%s)'''

	help_feedback_name = '-feedback <wiadomość> [obrazek]'
	help_feedback_value = 'Prześlij feedback z problemami albo pomysłami dotyczącymi bota. Możesz dołączyć jeden obrazek.'

	help_rate_name = '-rate_pl <obrazek/url> [lvl=<level>] [<stat>=<wartość> ...]'
	help_rate_value = '''
	Porównaj swój artefakt do optymalnego 5* artefaktu. Wpisz komendę i wrzuć zrzut ekranu w tej samej wiadomości.
	Jeżeli używasz Windows 10, możesz użyć skrótu Shift + Windows + S i zaznaczyć swój artefakt, a następnie przejść na Discord i wkleić go za pomocą Ctrl+V.

	Wartości domyślne
	ATK%, DMG%, Crit - 1
	ATK, EM, Recharge - 0.5
	Wszystko inne - 0
	Opcje
	lvl: Porównaj do artefaktu o określonym poziomie (domyślnie: <artifact_level>)
	-rate_pl lvl=20
	<stat>: Ustaw własne wartości (wartości między 0 i 1)
	-rate_pl atk=1 er=0 atk%=0.5
	<stat> jest którymś z: HP, HP%, ATK, ATK%, ER (Recharge), EM, PHYS, CR (Crit Rate), CD (Crit Damage), ELEM (Elemental DMG%), Heal, DEF, DEF
	Translated by qtFox#9773 | Przetłumaczone przez qtFox#9773
	'''

class ru(translation):
	id = 'ru'
	code = 'rus'
	flags = ['🇷🇺']
	supported = False

	hp = 'НР'
	heal = 'Бонус лечения'
	df = 'Защита'
	er = 'Восст. энергии'
	em = 'Мастерство стихий'
	atk = 'Сила атаки'
	cd = 'Крит. урон'
	cr = 'Шанс крит. попадания'
	phys = 'Бонус Физ. урона'
	elem = 'Бонус Элем. урона'
	anemo = 'Бонус Анемо урона'
	elec = 'Бонус Электро урона'
	pyro = 'Бонус Пиро урона'
	hydro = 'Бонус Гидро урона'
	cryo = 'Бонус Крио урона'
	geo = 'Бонус Гео урона'
	dend = 'Бонус Дендро урона'

	piece_set = '2 предмета'

	lvl = 'Уровень'
	score = 'Общая оценка'
	main_score = 'Оценка главного стата'
	sub_score = 'Оценка вторичных статов'
	art_level = 'Уровень артефакта'
	join = 'Если у вас возникли проблемы, присоединяйтесь к [Artifact Rater Server]%s'
	feedback = 'Отзыв получен, присоединяйтесь к %s для большей информации.'
	title = 'Помощь по Artifact Rater боту'
	change = 'Чтобы изменить язык, нажмите на соответствующий флаг ниже'
	deprecated = 'Устарело, пожалуйста испольщуйте команду -user lang <lang>, чтобы выбрать ваш язык'
	set_lang = 'Выбран язык: Русский'
	set_prefix = 'Префикс %s выбран'
	del_preset = 'Шаблон %s удален'
	set_preset = 'Шаблон %s изменен на %s'
	no_presets = 'Шаблон не найден'

	err = 'Ошибка'
	err_not_found = 'Ошибка: изображение или url не найдены, убедитесь, что отправляете в одном сообщении с командой.'
	err_parse = 'Ошибка: команда не распознана. Пожалуйста, проверьте правильность ввода.'
	err_try_again = 'Пожалуйста, попробуйте чуть позже.'
	err_unknown_ocr = 'Ошибка: неизвестная ошибка распознавания текста.'
	err_unknown = 'Неизвестная ошибка, попробуйте использовать изображение из инвентаря/со страницы артефакта.'
	err_admin_only = 'Ошибка: Только админы сервера могут выполнить эту команду.'
	err_server_only = 'Ошибка: Это действие может быть выполнено только на серверах.'

	help_description = '''Если вы хотите добавить его на свой сервер, используйте [ссылку](%s)
	Так же вы можете использовать бота, отправив личное сообщение Artifact Rater#6924.'''

	help_source = '''Если у вас какие-то проблемы, свяжитесь с shrubin#1866 в Дискорде или используйте команду -feedback.
	Исходный код доступен по адресу [GitHub](%s)'''

	help_feedback_name = '-feedback <сообщение> [изображение]'
	help_feedback_value = 'Отправьте отзыв с проблемами или идеями для бота. Можно добавить одно изображение.'

	help_rate_name = '-rate_ru <image/url> [lvl=<Уровень>] [<stat>=<По умолчанию> ...]'
	help_rate_value = '''\
	Оцените свой артефакт относительно идеального 5* артефакта. Отправьте изображение в одном сообщении с командой.
	Если вы используете Windows 10, вы можете зажать Shift + Windows + S и выделить для скриншота артефакт, а затем вставить его в Дискорд с помощью Ctrl+V.

	Оценка по умолчанию:
	Сила атаки %, шанс и урон крита - 1
	Сила атаки, мастерство стихий, восстановление энергии - 0.5
	Всё остальное - 0
	Опции:
	lvl:  Сравнить с указанным уровнем артефакта (по умолчанию: <artifact_level>)
	-rate_ru lvl=20
	<stat>: Настроить значения по умолчанию (от 0 до 1)
	-rate_ru Сила атаки=1 Восст.энергии=0 Сила атаки%=0.5
	<stat> может использоваться для любого показателя: HP, HP%, Атака, Атака %, Восст (Восстановление энергии), Мастерство (стихий), Физ (Физический урон), Крит.Шанс, Крит.Урон, Элем (Элементальный урон), Лечение (бонус), Защита, Защита %
	Translated by wellywob#8772 | Переведено by wellywob#8772
	'''

class tw(translation):
	def __init__(self):
		super().__init__()

		self.id = 'tw'
		self.code = 'cht'
		self.flags = ['🇹🇼']
		self.supported = False

		self.hp = '生命值'
		self.heal = '治療加成'
		self.df = '防禦力'
		self.er = '元素充能效率'
		self.em = '元素精通'
		self.atk = '攻擊力'
		self.cd = '暴擊傷害'
		self.cr = '暴擊率'
		self.phys = '物理傷害加成'
		self.elem = '元素傷害加成'
		self.anemo = '風元素傷害加成'
		self.elec = '雷元素傷害加成'
		self.pyro = '火元素傷害加成'
		self.hydro = '水元素傷害加成'
		self.cryo = '冰元素傷害加成'
		self.geo = '岩元素傷害加成'
		self.dend = '草元素傷害加成'

		self.piece_set = '套裝'

		self.replace = {'·': '.'}

		self.lvl = '等級'
		self.score = '聖遺物評分'
		self.main_score = '主屬性評分'
		self.sub_score = '副屬性評分'
		self.art_level = '聖遺物等級'
		self.join = f'有任何問題,請加入[Artifact Rater Server]({self.SERVER_URL})'
		self.feedback = f'已經收到你的意見,如果你想獲得更多詳細資訊 請加入{self.SERVER_URL}'
		self.deprecated = '請使用`-user lang <語言>`命令設定你的語言'
		self.set_lang = '語言設定已更改為繁體中文'
		self.set_prefix = '前綴設定為 %s'
		self.del_preset = '已刪除設定值 %s'
		self.set_preset = '設定值 %s 已更改為 %s'
		self.no_presets = '未找到設定值'

		self.err = '錯誤'
		self.err_not_found = '錯誤:找不到圖片或網址,請確定他們在同一條訊息中發送'
		self.err_parse = '錯誤:無法解析命令,請仔細檢查格式和拼寫'
		self.err_try_again = '錯誤:請在幾分鐘後再試一次'
		self.err_unknown_ocr = '錯誤:圖片識別失敗,出現未知錯誤'
		self.err_unknown = '未知錯誤,請嘗試使用測試頁面中的圖片'
		self.err_admin_only = '錯誤:只有伺服器管理員才能使用這個命令'
		self.err_server_only = '錯誤:這個命令只能在伺服器上使用'

		self.help_stats = '`stat`值可以是以下任何一種:生命`hp`,生命%`hp%`,防禦`def`,防禦%`def%`,攻擊`atk`,攻擊%`atk%`,元素充能`er`,元素精通`em`,物理傷害`phys`,元素傷害`elem`,爆擊率`cr`,爆擊傷害`cd`,治療加成`heal`.'

		self.help_commands = {
			'rate': [
				'-rate <圖片/圖片網址> [預設權重preset] [lvl=<等級>] [權重weights]',
				f'''
				針對5星聖遺物進行等級評分.請將命令和圖像放在同一條消息中.請使用清晰的螢幕截圖以獲得最佳效果.
				如果你使用的是Windows 10,你可以使用 Shift + Windows + S 並將滑鼠拖到畫面上,然後去discord使用 Ctrl+V 貼上.
				這個機器人將使用預設權重(詳見下文),除非你更改預設權重.你還可以與想要的等級進行評分.
				**預設權重**
				攻擊%,各種傷害%,爆擊 - 1
				攻擊,元素精通,元素充能 – 0.5
				其他 - 0
				**參數**
				`image/url`
				要評分的圖片,可以作為文件附加,也可以在訊息中添加網址. [Sample]({self.SAMPLE_URL})
				`preset`
				設定使用的權重.使用`-presets`查看哪些可用,或`-help`查看如何自己設定.
				`lvl`
				要評分的聖遺物等級,值介於0~20.有時自動檢測等級是錯誤的,可以用來修正.
				`weights`
				用於評分此聖遺物的權重.權重的格式`<stat>=<value>`,`value`值介於0~1.
				{self.help_stats}
				**例子**
				`-rate <圖片> atk%=0 hp=1 er=0.5`
				`-rate <圖片網址> 輔助 lvl=4`
				'''
			],

			'feedback': [
				'-feedback <訊息> [圖片]',
				'發送有關機器人的問題或意見.請使用它發送想法或錯誤報告,來協助我們改進機器人.'
			],

			'sets': [
				'-sets',
				'''
				查看所有可用的設定值.包括個人,伺服器的設定值.
				該命令將顯示一個清單,項目以及其設定值.
				'''
			],

			'lang': [
				'-[user/server] lang <語言代碼>',
				'''
				將更改機器人的語言設定為語言代碼`lang`.
				Artifact Rater將使用此語言處理你在`-rate`的指令.
				語言清單: English (en), Spanish (es), German (de), French (fr), Portuguese (pt), Polish (pl), Italian (it), Russian (ru), Indonesian (id), Vietnamese (vi), Japanese (ja), 繁體中文 (tw), 簡體中文 (cn)
				'''
			],

			'prefix': [
				'-server prefix <前綴>',
				'更改此機器人的指令前綴.'
			],

			'preset': [
				'-[user/server] preset <名稱> <權重>',
				f'''
				創建一個名為`名稱`的權重設定在對文物進行評級時使用.
				如果要檢查具有相同權重的多個聖遺物,你可以使用此命令創建具有所需權重的預設.
				`weights`將用於`-rate`使用預設時的命令.`weights`應採用以下格式`<stat>=<value>`,`value`值介於0~1.
				{self.help_stats}
				**例子**
				`-user preset healer hp=0.5 hp%=1 atk%=0`
				`-rate <圖片> healer`
				`-[user/server] preset delete <名稱>`
				刪除預設中的值`名稱` (用空格隔開).
				'''
			]
		}

		self.help_title = '聖遺物評分小工具幫助'

		self.help_description = f'''
		**指令**
		`{self.help_commands['rate'][0]}`
		通過發送圖片來評分你的聖遺物.使用`-help rate`查看更多細節.
		`{self.help_commands['feedback'][0]}`
		{self.help_commands['feedback'][1]}
		`{self.help_commands['sets'][0]}`
		查看所有可用的設定值.
		`-help <command>`
		顯示命令的説明消息.指令: {', '.join([f'`{command}`' for command in self.help_commands])}.
		**設定檔**
		`-user` 更改你的個人設定,覆蓋伺服器預設設定.
		`-server` 僅限管理員,更改伺服器預設設定.
		`{self.help_commands['prefix'][0]}`
		{self.help_commands['prefix'][1]}
		`{self.help_commands['lang'][0]}`
		將更改機器人的語言設定為語言代碼`lang`.你也可以使用國旗圖示反應來更改語言.
		`{self.help_commands['preset'][0]}`
		創建在對聖遺物進行評分時要使用的預設權重.`weights`將用於`-rate`指令時使用的預設.
		`-[user/server] preset delete <名稱>`
		刪除設定值.
		'''

		self.source = '源代碼'
		self.invite = '邀請Bot'
		self.support = '幫助'
		self.github = f'[GitHub]({self.GITHUB_URL})'
		self.discord = f'[Link]({self.BOT_URL})'
		self.server = f'[Discord]({self.SERVER_URL})'

		self.help_footer = '如果要更改語言,請點擊下面的相應國旗圖示'

class cn(translation):
	def __init__(self):
		super().__init__()

		self.id = 'cn'
		self.code = 'chs'
		self.flags = ['🇨🇳']
		self.supported = False

		self.hp = '生命值'
		self.heal = '治疗加成'
		self.df = '防御力'
		self.er = '元素充能效率'
		self.em = '元素精通'
		self.atk = '攻击力'
		self.cd = '暴击伤害'
		self.cr = '暴击率'
		self.phys = '物理伤害加成'
		self.elem = '元素伤害加成'
		self.anemo = '风元素伤害加成'
		self.elec = '雷元素伤害加成'
		self.pyro = '火元素伤害加成'
		self.hydro = '水元素伤害加成'
		self.cryo = '冰元素伤害加成'
		self.geo = '岩元素伤害加成'
		self.dend = '草元素伤害加成'

		self.piece_set = '套装'

		self.replace = {'·': '.'}

		self.lvl = '等级'
		self.score = '圣遗物评分'
		self.main_score = '主属性评分'
		self.sub_score = '副属性评分'
		self.art_level = '圣遗物等级'
		self.join = f'有任何问题,请加入[Artifact Rater Server]({self.SERVER_URL})'
		self.feedback = f'已经收到你的意见,如果你想获得更多详细信息 请加入{self.SERVER_URL}'
		self.deprecated = '请使用`-user lang <语言>`命令设定你的语言'
		self.set_lang = '语言设定已更改简体中文'
		self.set_prefix = '前缀设定为 %s'
		self.del_preset = '已删除设定值 %s'
		self.set_preset = '设定值 %s 已更改为 %s'
		self.no_presets = '未找到设定值'

		self.err = '错误'
		self.err_not_found = '错误:找不到图片或网址,请确定他们在同一条讯息中发送'
		self.err_parse = '错误:无法解析命令,请仔细检查格式和拼写'
		self.err_try_again = '错误:请在几分钟后再试一次'
		self.err_unknown_ocr = '错误:图片识别失败,出现未知错误'
		self.err_unknown = '未知错误,请尝试使用测试页面中的图片'
		self.err_admin_only = '错误:只有伺服器管理员才能使用这个命令'
		self.err_server_only = '错误:这个命令只能在伺服器上使用'

		self.help_stats = '`stat`值可以是以下任何一种:生命`hp`,生命%`hp%`,防御`def`,防御%`def%`,攻击`atk`,攻击%`atk%`,元素充能`er`,元素精通`em`,物理伤害`phys`,元素伤害`elem`,爆击率`cr`,爆击伤害`cd`,治疗加成`heal`.'

		self.help_commands = {
			'rate': [
				'-rate <图片/图片网址> [预设权重preset] [lvl=<等级>] [权重weights]',
				f'''
				针对5星圣遗物进行等级评分.请将命令和图像放在同一条消息中.请使用清晰的屏幕截图来获得最佳效果.
				如果你使用的是Windows 10,你可以使用 Shift + Windows + S 并将鼠标拖到画面上,然后去discord使用 Ctrl+V 贴上.
				这个机器人将使用预设权重(详见下文),除非你更改预设权重.你还可以与想要的等级进行评分.
				**预设权重**
				攻击%,各种伤害%,爆击 - 1
				攻击,元素精通,元素充能 – 0.5
				其他 - 0
				**参数**
				`image/url`
				要评分的图片,可以作为文件附加,也可以在讯息中添加网址. [Sample]({self.SAMPLE_URL})
				`preset`
				设定使用的权重.使用`-presets`查看哪些可用,或`-help`查看如何自己设定.
				`lvl`
				要评分的圣遗物等级,值介于0~20.有时自动检测等级是错误的,可以用来修正.
				`weights`
				用于评分此圣遗物的权重.权重的格式`<stat>=<value>`,`value`值介于0~1.
				{self.help_stats}
				**例子**
				`-rate <图片> atk%=0 hp=1 er=0.5`
				`-rate <图片网址> 辅助 lvl=4`
				'''
			],

			'feedback': [
				'-feedback <讯息> [图片]',
				'发送有关机器人的问题或意见.请使用它发送想法或错误报告,来协助我们改进机器人.'
			],

			'sets': [
				'-sets',
				'''
				查看所有可用的设定值.包括个人,服务器的设定值.
				该命令将显示一个清单,项目以及其设定值.
				'''
			],

			'lang': [
				'-[user/server] lang <语言代码>',
				'''
				将更改机器人的语言设定为语言代码`lang`.
				Artifact Rater将使用此语言处理你在`-rate`的指令.
				语言列表: English (en), Spanish (es), German (de), French (fr), Portuguese (pt), Polish (pl), Italian (it), Russian (ru), Indonesian (id), Vietnamese (vi), Japanese (ja), 繁体中文 (tw), 简体中文 (cn)
				'''
			],

			'prefix': [
				'-server prefix <前缀>',
				'更改此机器人的指令前缀.'
			],

			'preset': [
				'-[user/server] preset <名称> <权重>',
				f'''
				创建一个名为`名称`的权重设定在对文物进行评级时使用.
				如果要检查具有相同权重的多个圣遗物,你可以使用此命令创建具有所需权重的预设.
				`weights`将用于`-rate`使用预设时的命令.`weights`应采用以下格式`<stat>=<value>`,`value`值介于0~1.
				{self.help_stats}
				**例子**
				`-user preset healer hp=0.5 hp%=1 atk%=0`
				`-rate <图片> healer`
				`-[user/server] preset delete <名称>`
				删除设定值`名称` (用空格隔开).
				'''
			]
		}

		self.help_title = '圣遗物评分小工具帮助'

		self.help_description = f'''
		**指令**
		`{self.help_commands['rate'][0]}`
		通过发送图片来评分你的圣遗物.使用`-help rate`查看更多细节.
		`{self.help_commands['feedback'][0]}`
		{self.help_commands['feedback'][1]}
		`{self.help_commands['sets'][0]}`
		查看所有可用的设定值.
		`-help <command>`
		显示命令的说明消息.指令: {', '.join([f'`{command}`' for command in self.help_commands])}.
		**配置文件**
		`-user` 更改你的个人设定,覆盖伺服器预设设定.
		`-server` 仅限管理员,更改伺服器预设设定.
		`{self.help_commands['prefix'][0]}`
		{self.help_commands['prefix'][1]}
		`{self.help_commands['lang'][0]}`
		将更改机器人的语言设定为语言代码`lang`.你也可以使用国旗图示反应来更改语言.
		`{self.help_commands['preset'][0]}`
		创建在对圣遗物进行评分时要使用的预设权重.`weights`将用于`-rate`指令时使用的设定.
		`-[user/server] preset delete <名称>`
		删除设定值.
		'''

		self.source = '源代码'
		self.invite = '邀请Bot'
		self.support = '帮助'
		self.github = f'[GitHub]({self.GITHUB_URL})'
		self.discord = f'[Link]({self.BOT_URL})'
		self.server = f'[Discord]({self.SERVER_URL})'

		self.help_footer = '如果要更改语言,请点击下面的相应国旗图示'

# Text only, no game translation
class it(translation):
	def __init__(self):
		super().__init__()

		self.id = 'it'
		self.code = 'ita'
		self.flags = ['🇮🇹']
		self.supported = True

		self.lvl = 'Livello'
		self.score = 'Punteggio dell\'Artefatto'
		self.main_score = 'Valutazione della Statistica Principale'
		self.sub_score = 'Valutazione delle Statistiche Secondarie'
		self.art_level = 'Livello dell\'Atefatto'
		self.join = f'In caso di probelmi, unisciti al [Artifact Rater Server]({self.SERVER_URL})'
		self.feedback = f'Feedback ricevuto, unisciti al server discord per aggiunere ulteriori dettagli: {self.SERVER_URL}'
		self.title = 'Aiuto per Artifact Rater Bot'
		self.change = 'Per cambiare lingua del bot, selezionare la bandiera corrispondente'
		self.deprecated = 'Comando disapprovato, usare il comando `-user lang <lang>` per impostare la lingua'
		self.set_lang = 'Lingua impostata ad Italiano'
		self.set_prefix = 'Prefisso impostato a %s'
		self.del_preset = 'Preset %s cancellato'
		self.set_preset = 'Preset %s impostato a %s'
		self.no_presets = 'Nessun preset è stato trovato'

		self.err = 'Errore'
		self.err_not_found = 'Errore: Nessun URL o immagine sono stati trovati, assicurarsi che siano stati spediti nello stesso messaggio'
		self.err_parse = 'Errore: Il comando non può essere analizzato, ricontrollare il formato e la compitazione'
		self.err_try_again = 'Riprova tra un qualche minuto'
		self.err_unknown_ocr = 'Errore: OCR ha fallito per un errore sconosciuto'
		self.err_unknown = 'Errore sconosciuto, prova utilizzando un\'immagine proveniente dalla pagina di artefatti'
		self.err_admin_only = 'Errore: Solamente l\'amministratore del server può effettuare questa azione'
		self.err_server_only = 'Errore: Questa azione può esere effettuata unicamente sui server'

		self.help_stats = '`stat` può essere uno tra le seguenti: `hp`, `hp%`, `def`, `def%`, `atk`, `atk%`, `er` (Energy Recharge), `em` (Elemental Mastery), `phys` (Physical DMG), `elem` (Elemental DMG), `cr` (Crit Rate), `cd` (Crit Damage), `heal` (Healing Bonus).'

		self.help_commands = {
			'rate': [
				'-rate <immagine/url> [preset] [lvl=<livello>] [pesi]',
				f'''
				Per valutare un artefatto comparlandolo ad uno ottimale 5*, inserisci il comando e l'immagine nello stesso messaggio (Più l'immagine è chiara, migliori saranno i risultati).
				Se si sta utilizzando Windows 10, è possibile usare la scorciatoia Shift + Windows + S e trascinare il cursore sull'artefatto per copiare l'immagine, poi usare Ctrl+V in discord per incollare.
				Questo bot userà dei pesi predefiniti per giudicare gli artefatti (vedi sotto), a meno che non si voglia specificarli or un preset sia stato scelto.
				**Pesi Predefiniti**
				ATK%, DMG%, Crit - 1
				ATK, EM, Recharge – 0.5
				Everything else - 0
				**Parametri**
				`immagine/url`
				L'immagine che si vuole valutare deve essere allegata al messaggio oppure inserita tramite un url. [Esempio]({self.SAMPLE_URL})
				`preset`
				I 'preset' sono insiemi di valori predefiniti allocati alle diverse statistiche dell'artefatto (p.e. attacco, difesa, etc..). Vedi '-presets' per mostrare i preset disponibili, o '-help' per come creare il proprio.
				`lvl`
				Il livello dell'artefatto con con il quale si vuole comparare, da 0 a 20. A volte il rilevamento automatico per il livello si può sbagliare, usa questo per correggerlo.
				`pesi`
				Queste sono le valute usate per la valutazione di questo artefatto. Ogni 'peso' è nel formato '<stat>=<valore>', dove 'valore' è un numero tra 0 e 1.


				{self.help_stats}
				**Esempi**
				`-rate <immagine> atk%=0 hp=1 er=0.5`
				`-rate <url> support lvl=4`
				'''
			],

			'feedback': [
				'-feedback <messaggio> [immagine]',
				'Mandaci un feedback con allegato fino ad un\'immagine. Usa questa funzione per mandarci idee o per segnalarci possibili errori in modo tale da poterli correggiere e migliorare il bot.'
			],

			'sets': [
				'-sets',
				'''
				Visualizza tutti i preset disponibili. Include i presets personali, quelli dati dal server e quelli predefiniti.

				Questo comando mostrerà una lista contenente il nome del preset, l'appartenenza e i pesi assiciati ad esso.
				'''
			],

			'lang': [
				'-[utente/server] lang <lingua>',
				'''
				Imposta la lingua per i comandi usando una sigla di 2 lettere al posto di 'lingua'.
				Il bot userà questa lingua per le immagini che saranno mandate con il comando '-rate'.
				Lingue: Inglese (en), Spagnolo (es), Tedesco (de), Francese (fr), Portoghese (pt), Polacco (pl), Italiano (it), Russo (ru), Indonesiano (id), Vietnamita (vi), Giapponese (ja), Cinese Tradizionale (tw), Cinese semplificato (cn)
				'''
			],

			'prefix': [
				'-server prefix <prefisso>',
				'Cambia il prefisso del bot per questo server.'
			],

			'preset': [
				'-[utente/server] preset <nome> <pesi>',
				f'''
				Crea un preset chiamato 'nome' da usare per la valutazione degli artefatti.
				Se si vuole valutare molteplici artefatti utilizzando la medesima serie di pesi, è possibile utilizzare questo comando per creare un preset con i pesi desiderati.
				'pesi' sarà utilizzato nel comando '-rate' quando il preset verrà utilizzato. 'pesi' deve essere nel formato '<stat>=<valore>', dove 'valore' è un numero tra 0 a 1.
				{self.help_stats}
				**Esempio**
				`-user preset healer hp=0.5 hp%=1 atk%=0`
				`-rate <immagine> healer`
				`-[utente/server] preset delete <nome>`
				cancella i preset in `nomi` (separato da spazzi).
				'''
			]
		}

		self.help_title = 'Artifact Rater Help'

		self.help_description = f'''
		**Comandi**
		`{self.help_commands['rate'][0]}`
		Valuta il tuo artefatto mandando un'immagine. Vedi '-help rate' per più dettagli.

		`{self.help_commands['feedback'][0]}`
		{self.help_commands['feedback'][1]}

		`{self.help_commands['sets'][0]}`
		Visualizza tutti i preset disponibili.

		`-help <command>`
		Mostra il messaggio d'aiuto per quel comando. Comando: {', '.join([f'`{command}`' for command in self.help_commands])}.

		**Configurazione**

		`-user` cambia la tua configurazione personale. Sovrascrive le impostazioni di default del server.
		`-server` solo per amministratori, cambia i predefiniti del server.

		`{self.help_commands['prefix'][0]}`
		{self.help_commands['prefix'][1]}

		`{self.help_commands['lang'][0]}`
		Imposta la lingua per tutti i comandi attraverso il codice a 2 lettere 'lingua'. È inoltre possibile utilizzare la bandiera come reazione per cambiare lingua.

		`{self.help_commands['preset'][0]}`
		Crea un preset da utulizzare nell valutazione degli artefatti. 'pesi' sarà usato nel comando '-rate' quando il preset verrà utilizzato.

		`-[user/server] preset delete <nomi>`
		Cancell ai presets.
		'''

		self.source = 'Codice sorgente'
		self.invite = 'Invito per il Bot'
		self.support = 'Supporto'
		self.github = f'[GitHub]({self.GITHUB_URL})'
		self.discord = f'[Link]({self.BOT_URL})'
		self.server = f'[Discord]({self.SERVER_URL})'

		self.help_footer = 'Per cambiare lingua selezionare la bandiera corrispondente qui sotto'

# Text only, no game translation
class idn(translation):
	id = 'id'
	code = 'idn'
	flags = ['🇮🇩']
	supported = True

	lvl = 'Level'
	score = 'Skor Gear'
	main_score = 'Nilai Main Stat'
	sub_score = 'Nilai Substat'
	art_level = 'Level Artefak'
	join = 'Untuk masalah, silahkan bergabung [Artifact Rater Server]%s'
	feedback = 'Tanggapan diterima, silahkan bergabung %s jika kamu ingin menambahkan detail'
	title = 'Bantuan Bot Artifact Rater'

	err = 'Error'
	err_not_found = 'Error: Gambar atau url tidak ditemukan, pastikan keduanya dikirim dalam satu pesan'
	err_parse = 'Error: Command tidak bisa di proses, tolong periksa ulang format dan penulisan'
	err_try_again = 'Coba lagi dalam beberapa menit'
	err_unknown_ocr = 'Error: OCR gagal dengan error yang tidak diketahui'
	err_unknown = 'Error tidak diketahui, coba gunakan gambar dari inventori artefak'

	help_description = '''Jika ingin menggunakan bot di server privat, gunakan [link](%s)
	Kamu juga bisa menggunakan bot dengan mengririm command dalam DM ke Artifact Rater#6924.'''

	help_source = '''Jika kamu mempunyai masalah, tolong hubungi shrubin#1866 dalam discord atau gunakan -feedback command.
	Source code tersedia pada [GitHub](%s)'''

	help_feedback_name = '-feedback <pesan> [gambar]'
	help_feedback_value = 'Kirim masukan terkait masalah atau ide ke bot. Hingga satu gambar dapat dikirim.'

	help_rate_name = '-rate <gambar/url> [lvl=<level>] [<stat>=<nilai> ...]'
	help_rate_value = '''\
	Nilai sebuah artefak dengan sebuah *5 artefak yang optimal. Kirim command dan gambar dalam satu pesan.
	Jika kamu menggunakan Windows 10, Kamu bisa melakukan Shift + Windows + S dan kemudian drag cursor ke gambar artefak, lalu ke discord and paste gambar dengan Ctrl+V.

	Nilai standar
	ATK%, DMG%, Crit - 1
	ATK, EM, Recharge - 0.5
	Yang lainnya - 0

	Opsi
	lvl: Bandingkan dengan artefak spesifik (default: <artifact_level>)
	-rate lvl=20
	<stat>: Taruh nilai khusus (antara 0 dan 1)
	-rate atk=1 er=0 atk%=0.5
	<stat> adalah apapun dari HP, HP%, ATK, ATK%, ER (Recharge), EM, PHYS, CR (Crit Rate), CD (Crit Damage), ELEM (Elemental DMG%), Heal, DEF, DEF
	'''

languages = {lang.id: lang for lang in [en(), es(), de(), fr(), vi(), pt(), ja(), pl(), ru(), tw(), cn(), it(), idn()]}
