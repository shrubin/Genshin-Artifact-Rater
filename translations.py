class translation:
	# 2-digit language code
	id = 'en'
	# 3-digit language code
	code = 'eng'
	# Unicode flag
	flag = '🇺🇸'
	# Supported by OCR Engine 2
	supported = True

	SERVER_URL = 'https://discord.gg/SyGmBxds3M'
	BOT_URL = 'https://discord.com/api/oauth2/authorize?client_id=774612459692621834&permissions=19456&scope=bot'
	GITHUB_URL = 'https://github.com/shrubin/Genshin-Artifact-Rater'
	SAMPLE_URL = 'https://cdn.discordapp.com/attachments/787533173004173343/790751503475802122/unknown.png'

	# stats as they appear in-game
	hp = 'HP'
	heal = 'Healing'
	df = 'DEF'
	er = 'Energy Recharge'
	em = 'Elemental Mastery'
	atk = 'ATK'
	cd = 'CRIT DMG'
	cr = 'CRIT Rate'
	phys = 'Physical DMG'
	elem = 'Elemental DMG'
	anemo = 'Anemo DMG'
	elec = 'Electro DMG'
	pyro = 'Pyro DMG'
	hydro = 'Hydro DMG'
	cryo = 'Cryo DMG'
	geo = 'Geo DMG'
	dend = 'Dendro DMG'

	# text that appears below artifact stats (2-piece set)
	piece_set = 'Piece Set'

	# lines will be ignored if they're an exact match
	ignore = ['in']
	replace = {}

	# text for bot messages
	lvl = 'Level'
	score = 'Gear Score'
	main_score = 'Main Stat Rating'
	sub_score = 'Substat Rating'
	art_level = 'Artifact Level'
	join = f'For issues, join the [Artifact Rater Server]({SERVER_URL})'
	feedback = f'Feedback received, please join {SERVER_URL} if you\'d like to add more details'
	deprecated = 'Deprecated, please use the `-user lang <lang>` command to set your language'
	set_lang = 'Language set to English'
	set_prefix = 'Prefix set to %s'
	del_preset = 'Preset %s deleted'
	set_preset = 'Preset %s set to %s'
	no_presets = 'No presets found'

	# text for bot errors
	err = 'Error'
	err_not_found = 'Error: No image or url found, please make sure they were sent in the same message'
	err_parse = 'Error: Command cannot be parsed, please double check the format and spelling'
	err_try_again = 'please try again in a few minutes'
	err_unknown_ocr = 'Error: OCR failed with unknown error'
	err_unknown = 'Unknown error, try using an image from the inventory\'s artifact page'
	err_admin_only = 'Error: Only server admins can perform this action'
	err_server_only = 'Error: This action can only be performed on servers'

	# help text
	help_stats = '`stat` can be one of `hp`, `hp%`, `def`, `def%`, `atk`, `atk%`, `er` (Energy Recharge), `em` (Elemental Mastery), `phys` (Physical DMG), `elem` (Elemental DMG), `cr` (Crit Rate), `cd` (Crit Damage), `heal` (Healing Bonus).'

	help_commands = {
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
			The image to be rated, either attached as a file or by putting the url in the message. [Sample]({SAMPLE_URL})

			`preset`
			The preset selection of weights to use. See `-presets` for which presets are available, or `-help` for how to set your own.

			`lvl`
			The level of the artifact to compare against, from 0 to 20. Sometimes the auto-detection for level is wrong, use this to correct it.

			`weights`
			The weights to use for rating this artifact. Each weight is of the format `<stat>=<value>`, where `value` is a number between 0 and 1.
			{help_stats}

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
			{help_stats}

			**Example**
			`-user preset healer hp=0.5 hp%=1 atk%=0`
			`-rate <image> healer`

			`-[user/server] preset delete <name>`

			Delete the presets in `names` (separated by spaces).
			'''
		]
	}

	help_title = 'Artifact Rater Help'

	help_description = f'''
	**Commands**

	`{help_commands['rate'][0]}`
	Rate your artifact by sending an image of it. See `-help rate` for more details.

	`{help_commands['feedback'][0]}`
	{help_commands['feedback'][1]}

	`{help_commands['sets'][0]}`
	View all available presets.

	`-help <command>`
	Show the help message for that command. Commands: {', '.join([f'`{command}`' for command in help_commands])}.

	**Config**

	`-user` changes your personal config. Overrides server default settings.
	`-server` admin-only, changes the server default.

	`{help_commands['prefix'][0]}`
	{help_commands['prefix'][1]}

	`{help_commands['lang'][0]}`
	Set your language for all commands to the 2 letter language code `lang`. You can also use the flag reactions to change languages.

	`{help_commands['preset'][0]}`
	Create a preset to be used when rating artifacts. `weights` will be used in the `-rate` command when the preset is used.

	`-[user/server] preset delete <names>`
	Delete presets.
	'''

	source = 'Source Code'
	invite = 'Bot Invite'
	support = 'Support'
	github = f'[GitHub]({GITHUB_URL})'
	discord = f'[Link]({BOT_URL})'
	server = f'[Discord]({SERVER_URL})'

	help_footer = 'To change languages click on the corresponding flag below'

class en(translation):
	pass

class es(translation):
	id = 'es'
	code = 'spa'
	flag = '🇪🇸'
	supported = True

	hp = 'Vida'
	heal = 'Curación'
	df = 'DEF'
	er = 'Recarga de Energía'
	em = 'Maestría Elemental'
	atk = 'ATQ'
	cd = 'Daño CRIT'
	cr = 'Prob. CRIT'
	phys = 'Físico'
	elem = 'Elemental'
	anemo = 'Anemo'
	elec = 'Electro'
	pyro = 'Pyro'
	hydro = 'Hydro'
	cryo = 'Cryo'
	geo = 'Geo'
	dend = 'Dendro'

	piece_set = 'Conjunto'

	lvl = 'lvl'
	score = 'Gear Score'
	main_score = '% Stat Principal'
	sub_score = '% Substat'
	art_level = 'Nivel de artefacto'
	join = 'Si tienes algún problema, [únete al servidor]%s oficial'
	feedback = 'Feedback recibido, por favor, únete al servidor si deseas añadir más detalles: %s'
	title = 'Artifact Rater Bot Help'
	change = 'Para cambiar el idioma, pulsa sobre la bandera correspondiente'
	deprecated = 'Comando obsoleto, por favor, usa el comando -user lang <idioma> para seleccionar tu idioma'
	set_lang = 'Idioma cambiado al español'
	set_prefix = 'Prefijo seleccionado %s'
	del_preset = 'Preset %s elminado'
	set_preset = 'Preset %s configurado con %s'
	no_presets = 'No se encuentran presets'

	err = 'Error'
	err_not_found = 'Error: No se encuentra la imagen o la url no funciona, asegurate de mandarla en el mismo mensaje'
	err_parse = 'Error: el comando no ha podido ejecutarse, asegurate de que esté bien escrito y el formato sea correcto'
	err_try_again = 'por favor, prueba de nuevo en un rato'
	err_unknown_ocr = 'Error: el OCR ha fallado con un error desconocido'
	err_unknown = 'Error desconocido, intenta subir una imagen con la página de artefactos completa'
	err_admin_only = 'Error: Solo los admins del server pueden realizar esta acción'
	err_server_only = 'Error: Esta acción solo puede utilizarse en servidores'

	help_description = '''Si quieres, puedes invitar al bot a tu propio servidor de discord con este [link](%s)
	También puedes hablarle al bot por privado y enviarle el artefacto por ahí Artifact Rater#6924.'''

	help_source = '''Si tienes algún problema, por favor, contacta con shrubin#1866 (inglés) en discord o usa el comando -feedback
	El código del bot lo puedes encontrar aquí [GitHub](%s)'''

	help_feedback_name = '-feedback <mensaje> [imagen]'
	help_feedback_value = 'Envía feedback con los problemas o sugerencias para el bot. Puedes adjuntar solo una imagen.'

	help_rate_name = '-rate_es <imagen/url> [lvl=<level>] [<stat>=<valoración> ...]'
	help_rate_value = '''\
	Valora un artefacto comparándolo con los posibles stats de un 5*. Simplemente pon el comando y adjunta la imagen en el mismo mensaje.

	Si estás usando windows 10, puedes usar Shift + Windows + S y seleccionar el artefacto, después ir a discord y pegarlo con Ctrl + V.

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

class de(translation):
	id = 'de'
	code = 'ger'
	flag = '🇩🇪'
	supported = True

	hp = 'LP'
	heal = 'Heilungsbonus'
	df = 'VTD'
	er = 'Aufladerate'
	em = 'Elementarkunde'
	atk = 'ANG'
	cd = 'KSCH'
	cr = 'KT'
	phys = 'Physischer SCH-Bonus'
	elem = 'Elementarer Schaden'
	anemo = 'Anemo SCH-Bonus'
	elec = 'Elek SCH-Bonus'
	pyro = 'Pyro SCH-Bonus'
	hydro = 'Hydro SCH-Bonus'
	cryo = 'Cryo SCH-Bonus'
	geo = 'Geo SCH-Bonus'
	dend = 'Dendro SCH-Bonus'

	piece_set = 'Set mit 2 Teilen'

	lvl = 'Level'
	score = 'Gear Bewertung'
	main_score = 'Haupt-Stat'
	sub_score = 'Unter-Stat'
	art_level = 'Artifakt Level'
	join = 'Bei Problemen join dem Discord [Artifact Rater Server]%s'
	feedback = 'Feedback erhalten, bitte joine %s wenn du weitere Details hinzufügen möchtest'
	title = 'Artifact Rater Bot Hilfe'
	change = 'Um die Sprache zu ändern klick auf die dazugehörige Flagge unten.'
	deprecated = 'Veraltet, verwenden Sie bitte den Befehl -user lang <lang>, um Ihre Sprache festzulegen'
	set_lang = 'Sprache geändert auf Deutsch'
	set_prefix = 'Voreinstellung geändert zu %s'
	del_preset = 'Voreinstellung %s gelöscht'
	set_preset = 'Voreinstellung %s geändert zu %s'
	no_presets = 'Keine Voreinstellung gefunden'

	err = 'Fehler'
	err_not_found = 'Fehler: Kein Bild oder URL gefunden, bitte stelle sicher das sich das Bild in der selben Nachicht befindet'
	err_parse = 'Fehler: Kein Befehl gefunden, bitte schau das du ihn richtig und im korrekten Format geschrieben hast'
	err_try_again = 'bitte versuche es in ein paar Minuten nochmal'
	err_unknown_ocr = 'Fehler: OCR fehlgeschlagen mit unbekanntem Fehler'
	err_unknown = 'Unbekannter Fehler, verwende ein Bild von der Inventar Artefakt Seite'
	err_admin_only = 'Fehler: Nur Serveradministratoren können diese Aktion ausführen'
	err_server_only = 'Fehler: Diese Aktion kann nur auf Servern ausgeführt werden'

	help_description = '''Wenn sie den Bot auf ihrem privaten Discord Server nutzen wollen verwenden sie diesen [Link](%s)
	Sie können den Bot auch direkt eine private Nachicht schicken mit dem Befehl an Artifact Rater#6924'''

	help_source = '''Wenn sie irgendwelche Probleme haben wenden sie sich bitte an shrubin#1866 oder benutzen sie den Befehl: -feedback ( in englisch bitte )
	Quellcode ist vorhanden auf [Github](%s) unter'''

	help_feedback_name = '-feedback <Nachicht> [Bild]'
	help_feedback_value = 'Senden Sie Feedback mit Problemen oder Ideen für den Bot. Du kannst ein Bild anhängen.'

	help_rate_name = 'rate_de <Bild / Url> [lvl=<level>][stat=stat...]'
	help_rate_value = '''\
	Bewerten sie ein Artefakt anhand eines 5* Artefakt mit optimalen Stats. Fügen sie den Befehl und das Bild in die selbe Nachicht ein.

	Wenn Sie Windows 10 verwenden, können Sie Umschalt + Windows + S(Shift+Windows+S) verwenden und den Cursor über das Artefakt ziehen.
	Gehen Sie dann zu Discord und fügen Sie es mit Strg + V ein.

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

class fr(translation):
	id = 'fr'
	code = 'fre'
	flag = '🇫🇷'
	supported = True

	hp = 'PV'
	heal = 'Bonus de soins'
	df = 'DÉF'
	er = 'Recharge d\'énergie'
	em = 'Maîtrise élémentaire'
	atk = 'ATQ'
	cd = 'DGT CRIT'
	cr = 'Taux CRIT'
	phys = 'Bonus de DGT physiques'
	elem = 'Bonus de DGT élémentaire'
	anemo = 'Bonus de DGT Anémo'
	elec = 'Bonus de DGT Électro'
	pyro = 'Bonus de DGT Pyro'
	hydro = 'Bonus de DGT Hydro'
	cryo = 'Bonus de DGT Cryo'
	geo = 'Bonus de DGT Géo'
	dend = 'Bonus de DGT Dendro'

	piece_set = 'Set de pièces'

	lvl = 'Niveau'
	score = 'Puissance de l\'artefact'
	main_score = '% Stat principale'
	sub_score = '% Stats secondaires'
	art_level = 'Niveau d\'Artefact'
	join = 'Si vous rencontrez d\'autres problemes, [rejoignez le serveur]%s Artifact Rater'
	feedback = 'Si vous avez un retour d\'informations, s\'il vous plait rejoignez %s si vous voulez rajouter plus de détails'
	title = 'Aide Artifact Rater Bot'
	change = 'Pour changer la langue du bot, cliquez sur le drapeau correspondant'
	deprecated = 'Si ça ne fonctionne pas, s\'il vous plaît utilisez la commande -user lang <lang> pour la définir à votre langue'
	set_lang = 'Langue définie en Français'
	set_prefix = 'Préfix définis en %s'
	del_preset = 'Preset %s supprimer'
	set_preset = 'Preset %s remplacer par %s'
	no_presets = 'Pas de presets trouvés'

	err = 'Erreur'
	err_not_found = 'Erreur: Aucune image ou url n\'a été trouvée, s\'il vous plait assurez vous qu\'elle a était envoyée avec le message'
	err_parse = 'Erreur: La commande ne peut pas être analyser, vérifier le format et l\'orthographe'
	err_try_again = 'Merci de réessayer dans quelques minutes'
	err_unknown_ocr = 'Erreur: OCR a échoué a cause d\'une erreur inconnue'
	err_unknown = 'Erreur inconnue, essayer d\'utiliser une image d\'artefact venant de la page d\'inventaire'
	err_admin_only = 'Erreur: Seuls les admins peuvent effectuer cette action'
	err_server_only = 'Erreur: Cette action ne peut être effectué que sur le serveur'

	help_description = '''Si vous voulez vous joindre à notre serveur privé, utilisez ce [lien](%s)
	Vous pouvez aussi utiliser le bot en envoyant un MP à Artifact Rater#6924.'''

	help_source = '''Si vous rencontrez un problème, merci de contacter shrubin#1866 sur discord ou d’utiliser la commande –feedback
	Code source disponible sur [GitHub](%s)'''

	help_feedback_name = '-feedback <message> [image]'
	help_feedback_value = 'Envoyez un feedback avec les problèmes ou les idées pour le bot. Il peut être envoyé jusqu\'à une image à la fois.'

	help_rate_name = '-rate_fr <image/url>  [lvl=<niveau>][<stat>=<valeur par défaut> ...]'
	help_rate_value = '''\
	Évaluez votre artefact grâce à un artefact optimal de 5 étoiles. Entrez la commande avec l’image dans le même message.
	Si vous utilisez Windows 10 vous pouvez utiliser utiliser shift + Windows +S et vous pouvez passer votre curseur par-dessus l'artefact, puis allez sur discord et le coller avec Ctrl+V.

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

class vi(translation):
	id = 'vi'
	code = 'vie'
	flag = '🇻🇳'
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
	id = 'pt'
	code = 'por'
	flag = '🇵🇹'
	supported = True

	hp = 'Vida'
	heal = 'Bônus de Cura'
	df = 'DEF'
	er = 'Recarga de Energia'
	em = 'Proficiência Elemental'
	atk = 'ATQ'
	cd = 'Dano Crítico'
	cr = 'Taxa Crítica'
	phys = 'Bônus de Dano Físico'
	elem = 'Bônus de Dano Elemental'
	anemo = 'Bônus de Dano Anemo'
	elec = 'Bônus de Dano Electro'
	pyro = 'Bônus de Dano Pyro'
	hydro = 'Bônus de Dano Hydro'
	cryo = 'Bônus de Dano Cryo'
	geo = 'Bônus de Dano Geo'
	dend = 'Bônus de Dano Dendro'

	piece_set = 'Conjunto'

	lvl = 'Nível'
	score = 'Qualidade do Artefato'
	main_score = 'Nota Status Principal'
	sub_score = 'Nota Substats'
	art_level = 'Nível do Artefato'
	join = 'Se encontrar problemas, junte-se ao [Artifact Rater Server]%s'
	feedback = 'Feedback recebido, por favor junte-se ao servidor se quiser adicionar mais detalhes: %s'
	title = 'Artifact Rater Bot Help'
	change = 'Para mudar de idioma clique na bandeira correspondente abaixo'
	deprecated = 'Descontinuado, por favor user o  comando -user lang<idioma> para definir seu idioma'
	set_lang = 'Idioma definido para português'
	set_prefix = 'Prefixo definido para %s'
	del_preset = 'Predefinição %s deletada'
	set_preset = 'Predefinição %s definida para %s'
	no_presets = 'Nenhuma predefinição encontrada'

	err = 'Erro'
	err_not_found = 'Erro: Nenhuma imagem ou url encontrada, certifique-se de que foram enviadas na mesma mensagem'
	err_parse = 'Erro: Comando não pôde ser executado, por favor cheque a formatação e a ortografia'
	err_try_again = 'por favor tente novamente em alguns minutos'
	err_unknown_ocr = 'Erro: OCR falhou com um erro desconhecido'
	err_unknown = 'Erro desconhecido, tente usar uma imagem da página de artefatos'
	err_admin_only = 'Erro: Apenas administradores do servidor podem realizar essa ação'
	err_server_only = 'Erro: Essa ação só pode ser executada em servidores'

	help_description = '''Se quiser adicionar ao seu servidor privado use o [link](%s)
	Você também pode usar o bot mandando uma mensagem privada para Artifact Rater#6924.'''

	help_source = '''Se tiver problemas, entre em contato com shrubin#1866 no discord ou use o comando -feedback.
	Código-fonte disponível em [GitHub](%s)'''

	help_feedback_name = '-feedback <mensagem> [imagem]'
	help_feedback_value = 'Mande um feedback com problemas ou ideias para o bot. Apenas uma imagem pode ser enviada'

	help_rate_name = '-rate_pt <imagem/url> [lvl=<nível>] [<status>=<peso> ...]'
	help_rate_value = '''\
	Avalia um artefato em comparação com um artefato perfeito 5*. Coloque o comando e a imagem na mesma mensagem.
	Se estiver usando Windows 10, você pode usar Shift + Windows + S e arrastar o cursor sobre o artefato, depois vá para o discord e cole com Ctrl+V.

	Pesos padrão
	ATQ%, Bônus de Dano%, Crit - 1
	ATQ, Prof.Elemental, Recarga - 0.5
	Todo o resto - 0
	Opções
	lvl: Compara com o nível de artefato específicado (default: <artifact_level>)
	-rate_pt lvl=20
	<status>: Define pesos padrão (valor entre 0 e 1)
	-rate_pt atk=1 er=0 atk%=0.5
	<status> é qualquer um dos atributos: HP, HP%, ATQ, ATQ%, ER (Recarga de Energia), EM(Maestria Elemental),PHYS(Bônus de Dano Físico%), CR (Taxa Crítica), CD (Dano Crítico), ELEM (Bônus de Dano Elemental%), Cura, DEF, DEF%
	Translated by Dale#4801
	'''

class ja(translation):
	id = 'ja'
	code = 'jpn'
	flag = '🇯🇵'
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
	flag = '🇵🇱'
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
	flag = '🇷🇺'
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
	id = 'tw'
	code = 'cht'
	flag = '🇹🇼'
	supported = False

	hp = '生命值'
	heal = '治療加成'
	df = '防禦力'
	er = '元素充能效率'
	em = '元素精通'
	atk = '攻擊力'
	cd = '暴擊傷害'
	cr = '暴擊率'
	phys = '物理傷害加成'
	elem = '元素傷害加成'
	anemo = '風元素傷害加成'
	elec = '雷元素傷害加成'
	pyro = '火元素傷害加成'
	hydro = '水元素傷害加成'
	cryo = '冰元素傷害加成'
	geo = '岩元素傷害加成'
	dend = '草元素傷害加成'

	piece_set = '套裝'

	replace = {'·': '.'}

	lvl = '等級'
	score = '聖遺物評分'
	main_score = '主屬性評分'
	sub_score = '副屬性評分'
	art_level = '聖遺物等級'
	join = '有任何問題,請加入[Artifact Rater Server]({SERVER_URL})'
	feedback = '已經收到你的意見,如果您想獲得更多詳細資訊 請加入{SERVER_URL}'
	deprecated = '請使用-user lang <語言>命令設置您的語言'
	set_lang = '語言設置已更改為繁體中文'
	set_prefix = '前綴設置為 %s'
	del_preset = '已刪除預設前綴 %s'
	set_preset = '預設首碼 %s 已更改為 %s'
	no_presets = '未找到預設前綴'

	err = '錯誤'
	err_not_found = '錯誤:找不到圖片或網址,請確定他們在同一條訊息中發送'
	err_parse = '錯誤:無法解析命令,請仔細檢查格式和拼寫'
	err_try_again = '錯誤:請在幾分鐘後再試一次'
	err_unknown_ocr = '錯誤:圖片識別失敗,出現未知錯誤'
	err_unknown = '未知錯誤,請嘗試使用測試頁面中的圖片'
	err_admin_only = '錯誤:只有伺服器管理員才能使用這個命令'
	err_server_only = '錯誤:這個命令只能在伺服器上使用'

	help_stats = '`stat`值可以是以下任何一種:生命`hp`,生命%`hp%`,防禦`def`,防禦%`def%`,攻擊`atk`,攻擊%`atk%`,元素充能`er`,元素精通`em`,物理傷害`phys`,元素傷害`elem`,爆擊率`cr`,爆擊傷害`cd`,治療加成`heal`.'

	help_commands = {
		'rate': [
			'-rate <圖片/圖片網址> [預設權重preset] [lvl=<等級>] [權重weights]',
			f'''
			針對5星聖遺物進行等級評分.請將命令和圖像放在同一條消息中.請使用清晰的螢幕截圖以獲得最佳效果.
			如果您使用的是Windows 10,您可以使用 Shift + Windows + S 並將滑鼠拖到畫面上,然後去discord使用 Ctrl+V 貼上.
			這個機器人將使用預設權重(詳見下文),除非你更改預設權重.你還可以與想要的等級進行評分.
			**預設權重**
			攻擊%,各種傷害%,爆擊 - 1
			攻擊,元素精通,元素充能 – 0.5
			其他 - 0
			**參數**
			`image/url`
			要評分的圖片,可以作為文件附加,也可以在訊息中添加網址. [Sample]({SAMPLE_URL})
			`preset`
			預設使用的權重.使用`-presets`查看哪些可用,或`-help`查看如何自己設置.
			`lvl`
			要評分的聖遺物等級,值介於0~20.有時自動檢測等級是錯誤的,可以用來修正.
			`weights`
			用於評分此聖遺物的權重.權重的格式`<stat>=<value>`,`value`值介於0~1.
			{help_stats}
			**例子**
			`-rate <圖片> atk%=0 hp=1 er=0.5`
			`-rate <圖片網址> 支援 lvl=4`
			'''
		],

		'feedback': [
			'-feedback <訊息> [圖片]',
			'發送有關機器人的問題或意見.請使用它發送想法或錯誤報告,來協助我們改進機器人.'
		],

		'sets': [
			'-sets',
			'''
			查看所有可用的預設.包括個人,伺服器的預設值.
			該命令將顯示一個清單,項目以及設定值.
			'''
		],

		'lang': [
			'-[user/server] lang <語言代碼>',
			'''
			將更改機器人的語言設置為語言代碼`lang`.
			Artifact Rater將使用此語言處理您在`-rate`的指令.
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
			創建一個名為`name`的權重設定在對文物進行評級時使用.
			如果要檢查具有相同權重的多個聖遺物,您可以使用此命令創建具有所需權重的預設.
			`weights`將用於`-rate`使用預設時的命令.`weights`應採用以下格式`<stat>=<value>`,`value`值介於0~1.
			{help_stats}
			**例子**
			`-user preset healer hp=0.5 hp%=1 atk%=0`
			`-rate <圖片> healer`
			`-[user/server] preset delete <名稱>`
			刪除預設中的值`names` (用空格隔開).
			'''
		]
	}

	help_title = '聖遺物評分小工具幫助'

	help_description = f'''
	**指令**
	`{help_commands['rate'][0]}`
	通過發送圖片來評分你的聖遺物.使用`-help rate`查看更多細節.
	`{help_commands['feedback'][0]}`
	{help_commands['feedback'][1]}
	`{help_commands['sets'][0]}`
	查看所有可用的預設值.
	`-help <command>`
	顯示命令的説明消息.指令: {', '.join([f'`{command}`' for command in help_commands])}.
	**設定檔**
	`-user` 更改您的個人設置,覆蓋伺服器預設設置.
	`-server` 僅限管理員,更改伺服器預設設置.
	`{help_commands['prefix'][0]}`
	{help_commands['prefix'][1]}
	`{help_commands['lang'][0]}`
	將更改機器人的語言設置為語言代碼`lang`.您也可以使用國旗圖示反應來更改語言.
	`{help_commands['preset'][0]}`
	創建在對聖遺物進行評分時要使用的預設權重.`weights`將用於`-rate`指令時使用的預設.
	`-[user/server] preset delete <名稱>`
	刪除預設值.
	'''

	source = '源代碼'
	invite = '邀請Bot'
	support = '幫助'
	github = f'[GitHub]({GITHUB_URL})'
	discord = f'[Link]({BOT_URL})'
	server = f'[Discord]({SERVER_URL})'

	help_footer = '如果要更改語言,請點擊下面的相應國旗圖示'

class cn(translation):
	id = 'cn'
	code = 'chs'
	flag = '🇨🇳'
	supported = False

	hp = '生命值'
	heal = '治疗加成'
	df = '防御力'
	er = '元素充能效率'
	em = '元素精通'
	atk = '攻击力'
	cd = '暴击伤害'
	cr = '暴击率'
	phys = '物理伤害加成'
	elem = '元素伤害加成'
	anemo = '风元素伤害加成'
	elec = '雷元素伤害加成'
	pyro = '火元素伤害加成'
	hydro = '水元素伤害加成'
	cryo = '冰元素伤害加成'
	geo = '岩元素伤害加成'
	dend = '草元素伤害加成'

	piece_set = '套装'

	replace = {'·': '.'}

	lvl = '等级'
	score = '圣遗物评分'
	main_score = '主属性评分'
	sub_score = '副属性评分'
	art_level = '圣遗物等级'
	join = '有任何问题,请加入[Artifact Rater Server]({SERVER_URL})'
	feedback = '已经收到你的意见,如果您想获得更多详细信息 请加入{SERVER_URL}'
	deprecated = '请使用-user lang <语言>命令设置您的语言'
	set_lang = '语言设置已更改简体中文'
	set_prefix = '前缀设置为 %s'
	del_preset = '已删除预设前缀 %s'
	set_preset = '预设前缀 %s 已更改为 %s'
	no_presets = '未找到预设前缀'

	err = '错误'
	err_not_found = '错误:找不到图片或网址,请确定他们在同一条讯息中发送'
	err_parse = '错误:无法解析命令,请仔细检查格式和拼写'
	err_try_again = '错误:请在几分钟后再试一次'
	err_unknown_ocr = '错误:图片识别失败,出现未知错误'
	err_unknown = '未知错误,请尝试使用测试页面中的图片'
	err_admin_only = '错误:只有伺服器管理员才能使用这个命令'
	err_server_only = '错误:这个命令只能在伺服器上使用'

	help_stats = '`stat`值可以是以下任何一种:生命`hp`,生命%`hp%`,防御`def`,防御%`def%`,攻击`atk`,攻击%`atk%`,元素充能`er`,元素精通`em`,物理伤害`phys`,元素伤害`elem`,爆击率`cr`,爆击伤害`cd`,治疗加成`heal`.'

	help_commands = {
		'rate': [
			'-rate <图片/图片网址> [预设权重preset] [lvl=<等级>] [权重weights]',
			f'''
			针对5星圣遗物进行等级评分.请将命令和图像放在同一条消息中.请使用清晰的屏幕截图来获得最佳效果.
			如果您使用的是Windows 10,您可以使用 Shift + Windows + S 并将鼠标拖到画面上,然后去discord使用 Ctrl+V 贴上.
			这个机器人将使用预设权重(详见下文),除非你更改预设权重.你还可以与想要的等级进行评分.
			**预设权重**
			攻击%,各种伤害%,爆击 - 1
			攻击,元素精通,元素充能 – 0.5
			其他 - 0
			**参数**
			`image/url`
			要评分的图片,可以作为文件附加,也可以在讯息中添加网址. [Sample]({SAMPLE_URL})
			`preset`
			预设使用的权重.使用`-presets`查看哪些可用,或`-help`查看如何自己设置.
			`lvl`
			要评分的圣遗物等级,值介于0~20.有时自动检测等级是错误的,可以用来修正.
			`weights`
			用于评分此圣遗物的权重.权重的格式`<stat>=<value>`,`value`值介于0~1.
			{help_stats}
			**例子**
			`-rate <图片> atk%=0 hp=1 er=0.5`
			`-rate <图片网址> 支持 lvl=4`
			'''
		],

		'feedback': [
			'-feedback <讯息> [图片]',
			'发送有关机器人的问题或意见.请使用它发送想法或错误报告,来协助我们改进机器人.'
		],

		'sets': [
			'-sets',
			'''
			查看所有可用的预设.包括个人,服务器的预设值.
			该命令将显示一个清单,项目以及设定值.
			'''
		],

		'lang': [
			'-[user/server] lang <语言代码>',
			'''
			将更改机器人的语言设置为语言代码`lang`.
			Artifact Rater将使用此语言处理您在`-rate`的指令.
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
			创建一个名为`name`的权重设定在对文物进行评级时使用.
			如果要检查具有相同权重的多个圣遗物,您可以使用此命令创建具有所需权重的预设.
			`weights`将用于`-rate`使用预设时的命令.`weights`应采用以下格式`<stat>=<value>`,`value`值介于0~1.
			{help_stats}
			**例子**
			`-user preset healer hp=0.5 hp%=1 atk%=0`
			`-rate <图片> healer`
			`-[user/server] preset delete <名称>`
			删除预设中的值`names` (用空格隔开).
			'''
		]
	}

	help_title = '圣遗物评分小工具帮助'

	help_description = f'''
	**指令**
	`{help_commands['rate'][0]}`
	通过发送图片来评分你的圣遗物.使用`-help rate`查看更多细节.
	`{help_commands['feedback'][0]}`
	{help_commands['feedback'][1]}
	`{help_commands['sets'][0]}`
	查看所有可用的预设值.
	`-help <command>`
	显示命令的说明消息.指令: {', '.join([f'`{command}`' for command in help_commands])}.
	**配置文件**
	`-user` 更改您的个人设置,覆盖伺服器预设设置.
	`-server` 仅限管理员,更改伺服器预设设置.
	`{help_commands['prefix'][0]}`
	{help_commands['prefix'][1]}
	`{help_commands['lang'][0]}`
	将更改机器人的语言设置为语言代码`lang`.您也可以使用国旗图示反应来更改语言.
	`{help_commands['preset'][0]}`
	创建在对圣遗物进行评分时要使用的预设权重.`weights`将用于`-rate`指令时使用的预设.
	`-[user/server] preset delete <名称>`
	删除默认值.
	'''

	source = '源代码'
	invite = '邀请Bot'
	support = '帮助'
	github = f'[GitHub]({GITHUB_URL})'
	discord = f'[Link]({BOT_URL})'
	server = f'[Discord]({SERVER_URL})'

	help_footer = '如果要更改语言,请点击下面的相应国旗图示'

# Text only, no game translation
class it(translation):
	id = 'it'
	code = 'ita'
	flag = '🇮🇹'
	supported = True

	lvl = 'Livello'
	score = 'Punteggio dell\'Artefatto'
	main_score = 'Valutazione della Statistica Principale'
	sub_score = 'Valutazione delle Statistiche Secondarie'
	art_level = 'Livello dell\'Atefatto'
	join = 'In caso di probelmi, unisciti al [Artifact Rater Server]%s'
	feedback = 'Feedback ricevuto, unisciti al server discord per aggiunere ulteriori dettagli: %s'
	title = 'Aiuto per Artifact Rater Bot'
	change = 'Per cambiare lingua del bot, selezionare la bandiera corrispondente'
	deprecated = 'Comando disapprovato, usare il comando -user lang <lang> per impostare la lingua'
	set_lang = 'Lingua impostata ad Italiano'
	set_prefix = 'Prefisso impostato a %s'
	del_preset = 'Preset %s cancellato'
	set_preset = 'Preset %s impostato a %s'
	no_presets = 'Nessun preset è stato trovato'

	err = 'Errore'
	err_not_found = 'Errore: Nessun URL o immagine sono stati trovati, assicurarsi che siano stati spediti nello stesso messaggio'
	err_parse = 'Errore: Il comando non può essere analizzato, ricontrollare il formato e la compitazione'
	err_try_again = 'Riprova tra un qualche minuto'
	err_unknown_ocr = 'Errore: OCR ha fallito per un errore sconosciuto'
	err_unknown = 'Errore sconosciuto, prova utilizzando un\'immagine proveniente dalla pagina di artefatti'
	err_admin_only = 'Errore: Solamente l\'amministratore del server può effettuare questa azione'
	err_server_only = 'Errore: Questa azione può esere effettuata unicamente sui server'

	help_description = '''Nel qual caso tu voglia aggiungerlo ad un server privato usa il [link](%s)
	Puoi anche servirti del bot mandando un messaggio privato contenente il comando a Artifact Rater#6924.'''

	help_source = '''Per qualunque problema, contatta shrubin#1866 su discord oppure utilizza il comando -feedback.
	Il codice sorgente è disponibile all'indirizzo [GitHub](%s)'''

	help_feedback_name = '-feedback <messaggio> [immagine]'
	help_feedback_value = 'Manda il tuo feedback di problemi o idee al bot. Solo un immagine alla volta sarà accettata.'

	help_rate_name = '-rate_it <immagine/url> [lvl=<livello>] [<stato>=<peso> ...]'
	help_rate_value = '''\
	Confronta un artefatto con un'ottimale artefatto 5*. Metti il comando e l'immagine nello stesso messaggio.

	Se stai utilizzando Windows 10, puoi usare Shift + Windows + S e trascinare il cursore sull'artefatto per copiare l'immagine, poi usa Ctrl+V in discord per incollare.

	Pesi predefiniti
	ATK%, DMG%, Crit - 1
	ATK, EM, Recharge - 0.5
	Tutto il resto - 0

	Opzioni
	lvl: Compara con un artefatto di livello specifico (default: <artifact_level>)
	-rate_it lvl=20
	<stato>: imposta pesi predefiniti (valori compresi tra 0 e 1)
	-rate_it atk=1 er=0 atk%=0.5
	<stato> è qualunque tra: HP, HP%, ATK, ATK%, ER (Recharge), EM, PHYS, CR (Crit Rate), CD (Crit Damage), ELEM (Elemental DMG%), Heal, DEF, DEF
	'''

# Text only, no game translation
class idn(translation):
	id = 'id'
	code = 'idn'
	flag = '🇮🇩'
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

languages = {lang.id: lang for lang in [en, es, de, fr, vi, pt, ja, pl, ru, tw, cn, it, idn]}
