class translation:
	# 2-digit language code
	uid = 'en'
	# 3-digit language code
	code = 'eng'
	# Supported by OCR Engine 2
	supported = True

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

	# shortnames for setting stat weights / level
	hp_opt = 'hp'
	heal_opt = 'heal'
	df_opt = 'def'
	er_opt = 'er'
	em_opt = 'em'
	atk_opt = 'atk'
	cr_opt = 'cr'
	cd_opt = 'cd'
	phys_opt = 'phys'
	elem_opt = 'elem'
	lvl_opt = 'lvl'

	# text that appears below artifact stats (2-piece set)
	piece_set = 'Piece Set'

	# lines will be ignored if they're an exact match
	ignore = []
	replace = {}

	# text for bot messages
	lvl = 'Level'
	score = 'Gear Score'
	main_score = 'Main Stat Rating'
	sub_score = 'Substat Rating'
	art_level = 'Artifact Level'
	requested = 'Requested by %s'
	join = 'For issues, join the [Artifact Rater Server]%s'
	feedback = 'Feedback received, please join https://discord.gg/SyGmBxds3M if you\'d like to add more details'

	# text for bot errors
	err = 'Error'
	err_not_found = 'Error: No image or url found, please make sure they were sent in the same message'
	err_parse = 'Error: Command cannot be parsed, please double check the format and spelling'
	err_try_again = 'please try again in a few minutes'
	err_unknown_ocr = 'Error: OCR failed with unknown error'
	err_unknown = 'Unknown error, try using an image from the inventory\'s artifact page'

	help_feedback = '''\
Send feedback with issues or ideas for the bot. Up to one image can be sent.

-feedback <message> [image]
'''

	help_rate = '''\
Rate an artifact against an optimal 5* artifact. Put the command and image in the same message.

If you are using Windows 10, you can use Shift + Windows + S and drag your cursor over the artifact, then go to discord and paste it with Ctrl+V.

If you would like to add it to your private server use the link:
https://discord.com/api/oauth2/authorize?client_id=774612459692621834&permissions=19456&scope=bot

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

<stat> is any of HP, HP%, ATK, ATK%, ER (Recharge), EM, PHYS, CR (Crit Rate), CD (Crit Damage), ELEM (Elemental DMG%), Heal, DEF, DEF
'''

class en(translation):
	ignore = ['in']

class es(translation):
	uid = 'es'
	code = 'spa'
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
	requested = 'Pedido por %s'
	join = 'Si tienes algún problema, [únete al servidor]%s oficial'
	feedback = 'Feedback recibido, por favor, únete al servidor si deseas añadir más detalles: https://discord.gg/SyGmBxds3M'

	err = 'Error'
	err_not_found = 'Error: No se encuentra la imagen o la url no funciona, asegurate de mandarla en el mismo mensaje'
	err_parse = 'Error: el comando no ha podido ejecutarse, asegurate de que esté bien escrito y el formato sea correcto'
	err_try_again = 'por favor, prueba de nuevo en un rato'
	err_unknown_ocr = 'Error: el OCR ha fallado con un error desconocido'
	err_unknown = 'Error desconocido, intenta subir una imagen con la página de artefactos completa'

	help_feedback = '''\
Envía feedback con los problemas o sugerencias para el bot. Puedes adjuntar solo una imagen.

-feedback <mensaje> [imagen]
'''

	help_rate = '''\
Valora un artefacto comparándolo con los posibles stats de un 5*. Simplemente pon el comando y adjunta la imagen en el mismo mensaje.

Si estás usando windows 10, puedes usar Shift + Windows + S y seleccionar el artefacto, después ir a discord y pegarlo con Ctrl + V.

Si quieres, puedes invitar al bot a tu propio servidor de discord con este link:
https://discord.com/api/oauth2/authorize?client_id=774612459692621834&permissions=19456&scope=bot

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

class de(translation):
	uid = 'de'
	code = 'deu'
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
	elec = 'Elektro SCH-Bonus'
	pyro = 'Pyro SCH-Bonus'
	hydro = 'Hydro SCH-Bonus'
	cryo = 'Cryo SCH-Bonus'
	geo = 'Geo SCH-Bonus'
	dend = 'Dendro SCH-Bonus'

	hp_opt = 'lp'
	heal_opt = 'healingbonus'
	df_opt = 'vtd'
	er_opt = 'aufladerate'
	em_opt = 'elementarkunde'
	atk_opt = 'ang'
	cr_opt = 'kt'
	cd_opt = 'ksch'
	phys_opt = 'physischbonus'
	elem_opt = 'elementarbonus'
	lvl_opt = 'lvl'

	piece_set = 'Set mit 2 Teilen'

	lvl = 'Level'
	score = 'Gear Bewertung'
	main_score = 'Haupt-Stat'
	sub_score = 'Unter-Stat'
	art_level = 'Artifakt Level'
	requested = 'Angefragt von %s'
	join = 'Bei Problemen join dem Discord [Artifact Rater Server]%s'
	feedback = 'Feedback erhalten, bitte joine https://discord.gg/SyGmBxds3M wenn du weitere Details hinzufügen möchtest'

	err = 'Fehler'
	err_not_found = 'Fehler: Kein Bild oder URL gefunden, bitte stelle sicher das sich das Bild in der selben Nachicht befindet'
	err_parse = 'Fehler: Kein Befehl gefunden, bitte schau das du ihn richtig und im korrekten Format geschrieben hast'
	err_try_again = 'bitte versuche es in ein paar Minuten nochmal'
	err_unknown_ocr = 'Fehler: OCR fehlgeschlagen mit unbekanntem Fehler'
	err_unknown = 'Unbekannter Fehler, verwende ein Bild von der Inventar Artefakt Seite'

	help_feedback = '''\
Senden Sie Feedback mit Problemen oder Ideen für den Bot. Du kannst ein Bild anhängen.

-feedback <Nachicht> [Bild]
'''

	help_rate = '''\
Bewerten sie ein Artefakt anhand eines 5* Artefakt mit optimalen Stats.
Fügen sie den Befehl und das Bild in die selbe Nachicht ein.

Wenn Sie Windows 10 verwenden, können Sie Umschalt + Windows + S(Shift+Windows+S) verwenden und den Cursor über das Artefakt ziehen.
Gehen Sie dann zu Discord und fügen Sie es mit Strg + V ein.

Wenn sie den Bot auf ihrem privaten Discord Server nutzen wollen verwenden sie diesen Link:
https://discord.com/api/oauth2/authorize?client_id=774612459692621834&permissions=19456&scope=bot

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

class fr(translation):
	uid = 'fr'
	code = 'fra'
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

	hp_opt = 'pv'
	heal_opt = 'soins'
	df_opt = 'def'
	er_opt = 're'
	em_opt = 'me'
	atk_opt = 'atq'
	cr_opt = '%crt'
	cd_opt = 'crtdmg'
	phys_opt = 'phys'
	elem_opt = 'elem'
	lvl_opt = 'niv'

	piece_set = 'Set de pièces'

	lvl = 'Niveau'
	score = 'Puissance de l\'artefact'
	main_score = '% Stat principale'
	sub_score = '% Stats secondaires'
	art_level = 'Niveau d\'Artefact'
	requested = 'Demandé par %s'
	join = 'Si vous rencontrez d\'autres problemes, [rejoignez le serveur]%s Artifact Rater'
	feedback = 'Si vous avez un retour d\'informations, s\'il vous plait rejoignez https://discord.gg/SyGmBxds3M si vous voulez rajouter plus de détails'

	err = 'Erreur'
	err_not_found = 'Erreur: Aucune image ou url n\'a été trouvée, s\'il vous plait assurez vous qu\'elle a était envoyée avec le message'
	err_parse = 'Erreur: La commande ne peut pas être analyser, vérifier le format et l\'orthographe'
	err_try_again = 'Merci de réessayer dans quelques minutes'
	err_unknown_ocr = 'Erreur: OCR a échoué a cause d\'une erreur inconnue'
	err_unknown = 'Erreur inconnue, essayer d\'utiliser une image d\'artefact venant de la page d\'inventaire'

	help_feedback = '''\
Envoyez un feedback avec les problèmes ou les idées pour le bot. Il peut être envoyé jusqu'à une image à la fois.

-feedback <message> [image]
'''

	help_rate = '''\
Évaluez votre artefact grâce à un artefact optimal de 5 étoiles. Entrez la commande avec l’image dans le même message.

Si vous utilisez Windows 10 vous pouvez utiliser utiliser shift + Windows +S et vous pouvez passer votre curseur par-dessus l'artefact, puis allez sur discord et le coller avec Ctrl+V.

Si vous voulez vous joindre à notre serveur privé, utilisez ce lien :
https://discord.com/api/oauth2/authorize?client_id=774612459692621834&permissions=19456&scope=bot
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

class vi(translation):
	uid = 'vi'
	code = 'vie'
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

class pt(translation):
	uid = 'pt'
	code = 'por'
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

	hp_opt = 'vida'
	heal_opt = 'cura'
	df_opt = 'def'
	er_opt = 're'
	em_opt = 'pe'
	atk_opt = 'atq'
	cr_opt = 'txcrit'
	cd_opt = 'danocrit'
	phys_opt = 'fis'
	elem_opt = 'elem'
	lvl_opt = 'lvl'

	piece_set = 'Conjunto'

	lvl = 'Nível'
	score = 'Qualidade do Artefato'
	main_score = 'Nota Status Principal'
	sub_score = 'Nota Substats'
	art_level = 'Nível do Artefato'
	requested = 'Solicitado por %s'
	join = 'Se encontrar problemas, junte-se ao [Artifact Rater Server]%s'
	feedback = 'Feedback recebido, por favor junte-se ao servidor se quiser adicionar mais detalhes: https://discord.gg/SyGmBxds3M'

	err = 'Erro'
	err_not_found = 'Erro: Nenhuma imagem ou url encontrada, certifique-se de que foram enviadas na mesma mensagem'
	err_parse = 'Erro: Comando não pôde ser executado, por favor cheque a formatação e a ortografia'
	err_try_again = 'por favor tente novamente em alguns minutos'
	err_unknown_ocr = 'Erro: OCR falhou com um erro desconhecido'
	err_unknown = 'Erro desconhecido, tente usar uma imagem da página de artefatos'

	help_feedback = '''\
Mande um feedback com problemas ou ideias para o bot. Apenas uma imagem pode ser enviada
-feedback <mensagem> [imagem]
'''

	help_rate = '''\
Avalia um artefato em comparação com um artefato perfeito 5*. Coloque o comando e a imagem na mesma mensagem.

Se estiver usando Windows 10, você pode usar Shift + Windows + S e arrastar o cursor sobre o artefato, depois vá para o discord e cole com Ctrl+V.

Se quiser adicionar ao seu servidor privado use o link:
https://discord.com/api/oauth2/authorize?client_id=774612459692621834&permissions=3072&scope=bot

Você também pode usar o bot mandando uma mensagem privada para Artifact Rater#6924.

-rate_pt <imagem/url> [lvl=<nível>] [<status>=<peso> ...]

Se tiver problemas, entre em contato com shrubin#1866 no discord ou use o comando -feedback.
Código-fonte disponível em: https://github.com/shrubin/Genshin-Artifact-Rater

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
	uid = 'ja'
	code = 'jpn'
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

	hp_opt = 'hp'
	heal_opt = '治癒'
	df_opt = '防御'
	er_opt = '元素チャージ'
	em_opt = '元素熟知'
	atk_opt = '攻撃'
	cr_opt = '会心'
	cd_opt = '会心ダメージ'
	phys_opt = '物理'
	elem_opt = '元素'
	lvl_opt = 'レベル'

	piece_set = '2セット'

	replace = {'カ': '力'}

	lvl = 'レベル'
	score = 'ギアスコア'
	main_score = 'メインステータス評価'
	sub_score = 'サブステータス評価'
	art_level = '聖遺物レベル'
	requested = '％sからのリクエスト'
	join = '[公式サーバー]%sに参加する'
	feedback = 'フィードバックを受け取りました。詳細を追加したい場合は、 https://discord.gg/SyGmBxds3Mに参加して下さい。'

	err = 'エラー'
	err_not_found = 'エラー：画像またはURLが見つかりませんでした。同じメッセージで送信されたことを確認してください。'
	err_parse = 'エラー：コマンドを解析できません。形式とスペルを再確認してください。'
	err_try_again = 'エラー：数分後にもう一度お試しください。'
	err_unknown_ocr = 'エラー：OCRが不明なエラーで失敗しました。'
	err_unknown = '不明なエラーが発生しました。インベントリの聖遺物ページのイメージを使用してみてください。'

	help_feedback = '''\
BOTの問題やアイデアについてフィードバックを送信します。 最大1つの画像を送信できます。

-feedback <メッセージ> [イメージ]
'''

	help_rate = '''\
自分の聖遺物を最適な５＊聖遺物と比べます。同じメッセージにコマンドとイメージ両方を入れて下さい。

Windows 10を使っている場合は、Shift + Windows + Sを押すながら聖遺物の上にカーソルをドラッグし、ディスコードを開くと、Ctrl + Vで貼り付けることができます。

自分のプライベートサーバーに追加する場合は、次のリンクを使用して下さい：https://discord.com/api/oauth2/authorize?client_id=774612459692621834&permissions=3072&scope=bot

さらに、次のコマンドをArtifact Rater#6924にダイレクトメッセージ（D M）を送ると、BOT も使えます。

-rate_jp <image/url> [lvl=<レベル>] [<stat>=<デフォルトの重み付け> ...]

問題がある場合は、ディスコードでshrubin#1866に連絡するか、英語の -feedbackコマンドを使って下さい。ソースコードをご覧になりたい場合は、こちらへ：https://github.com/shrubin/Genshin-Artifact-Rater

デフォルトの重み付け

攻撃力％、各種ダメージバフ％、会心 – 1
攻撃力、元素熟知、元素チャージ効率 – 0.5
他 – 0

選択肢

lvl: 特定の聖遺物レベルと比較する (デフォルト: <聖遺物_レベル>)
-rate_jp lvl=20

<stat>: カスタムの重み付けを設定します（値は0から1の間）
-rate_jp 攻撃力=1 元素チャージ効率=0 攻撃力％=0.5

<stat> においてHP、HP%、攻撃力、攻撃力％、元素チャージ効率 、元素熟知、物理ダメージ、会心率、会心ダメージ、元素ダメージ、治癒効果、防御力を使えることができます。

Translated by plastiquedoll#1393 | plastiquedoll#1393によって翻訳されました。
'''

class pl(translation):
	lvl = 'Level'
	score = 'Wynik ogólny'
	main_score = 'Ocena głównej statystyki'
	sub_score = 'Ocena podstatystyk'
	art_level = 'Poziom artefaktów'
	requested = 'Wywołano przez %s'
	join = 'W przypadku problemów, dołącz na [Artifact Rater Server]%s'
	feedback = 'Otrzymaliśmy feedback, dołącz na serwer https://discord.gg/SyGmBxds3M jeżeli chciałbyś dodać więcej szczegółów.'

	err = 'Błąd'
	err_not_found = 'Błąd: Nie znaleziono URL ani obrazu, upewnij się czy zostały wysłane w tej samej wiadomości.'
	err_parse = 'Błąd: Komenda nie może zostać sparsowana, sprawdź jeszcze raz jej format i pisownię.'
	err_try_again = 'spróbuj ponownie za kilka minut'
	err_unknown_ocr = 'Błąd: OCR zawiódł z nieznanym błędem.'
	err_unknown = 'Nieznany błąd, spróbuj użyć zrzutu ekranu zawierającego zakładkę z artefaktami w ekwipunku'

	help_feedback = '''\
Prześlij feedback z problemami albo pomysłami dotyczącymi bota. Możesz dołączyć jeden obrazek.
-feedback <wiadomość> [obrazek]
'''

	help_rate = '''\
Porównaj swój artefakt do optymalnego 5* artefaktu. Wpisz komendę i wrzuć zrzut ekranu w tej samej wiadomości.

Jeżeli używasz Windows 10, możesz użyć skrótu Shift + Windows + S i zaznaczyć swój artefakt, a następnie przejść na Discord i wkleić go za pomocą Ctrl+V.

Jeżeli chcesz go dodać do swojego serwera, użyj tego linku:
https://discord.com/api/oauth2/authorize?client_id=774612459692621834&permissions=19456&scope=bot

Możesz również użyć tego bota poprzez wysłanie komendy w prywatnej wiadomości do Artifact Rater#6924.
-rate <obrazek/url> [lvl=<level>] [<stat>=<wartość> ...]

Jeżeli uświadczyłeś problemów, skontaktuj się z shrubin#1866 na discordzie albo użyj komendy -feedback.
Kod źródłowy dostępny na https://github.com/shrubin/Genshin-Artifact-Rater

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
	uid = 'ru'
	code = 'rus'
	supported = False

	hp = 'HP'
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

	hp_opt = 'HP'
	heal_opt = 'Лечение'
	df_opt = 'Защита'
	er_opt = 'Восст'
	em_opt = 'Мастерство'
	atk_opt = 'Атака'
	cr_opt = 'ШансКРТ'
	cd_opt = 'УронКРТ'
	phys_opt = 'Физ'
	elem_opt = 'Элем'
	lvl_opt = 'лвл'

	piece_set = '2 предмета'

	lvl = 'Уровень'
	score = 'Общая оценка'
	main_score = 'Оценка главного стата'
	sub_score = 'Оценка побочных статов'
	art_level = 'Уровень артефакта'
	requested = 'Запрос в %'
	join = 'Если у вас возникли проблемы, присоединяйтесь к [Artifact Rater Server]%s'
	feedback = 'Отзыв получен, присоединяйтесь к https://discord.gg/SyGmBxds3M для большей информации.'

	err = 'Ошибка'
	err_not_found = 'Ошибка: изображение или url не найдены, убедитесь, что отправляете в одном сообщении с командой.'
	err_parse = 'Ошибка: команда не распознана. Пожалуйста, проверьте правильность ввода.'
	err_try_again = 'Пожалуйста, попробуйте чуть позже.'
	err_unknown_ocr = 'Ошибка: неизвестная ошибка распознавания текста.'
	err_unknown = 'Неизвестная ошибка, попробуйте использовать изображение из инвентаря/со страницы артефакта.'

	help_feedback = '''\
Отправьте отзыв с проблемами или идеями для бота. Можно добавить одно изображение.
-feedback <сообщение> [изображение]
'''

	help_rate = '''\
Оцените свой артефакт относительно идеального 5* артефакта. Отправьте изображение в одном сообщении с командой. 

Если вы используете Windows 10, вы можете зажать Shift + Windows + S и выделить для скриншота артефакт, а затем вставить его в Дискорд с помощью Ctrl+V.

Если вы хотите добавить его на свой сервер, используйте ссылку:
https://discord.com/api/oauth2/authorize?client_id=774612459692621834&permissions=19456&scope=bot

Так же вы можете спользовать бота, отправив личное сообщение Artifact Rater#6924.

-rate <image/url> [lvl=<Уровень>] [<stat>=<По умолчанию> ...]

Если у вас какие-то проблемы, свяжитесь с shrubin#1866 в Дискорде или используйте команду -feedback.
Исходный код доступен по адресу: https://github.com/shrubin/Genshin-Artifact-Rater

Оценка по умолчанию:

Сила атаки %, шанс и урон крита - 1
Сила атки, мастерство элементов, восстановление энергии - 0.5
Всё остальное - 0

Опции:

lvl:  Сравнить с указанным уровнем артефакта (по умолчанию: <artifact_level>)
-rate_ru lvl=20

<stat>: Настроить значения по умолчанию (от 0 до 1)
-rate_ru Сила атаки=1 Восст.энергии=0 Сила атаки%=0.5

<stat> может использоваться для любого показателя: HP, HP%, Атака, Атака %, Восст (Восстановление энергии), Мастерство (стихий), Физ (Физический урон), ШансКРТ, УронКРТ, Элем (Элементальный урон), Лечение (бонус), Защита, Защита %

Translated by wellywob#8772 | Переведено by wellywob#8772
'''

languages = {lang.uid: lang for lang in [en, es, de, fr, vi, pt, ja, pl, ru]}
