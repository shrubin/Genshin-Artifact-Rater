class translation:
	# 2-digit language code
	uid = 'en'
	# 3-digit language code
	code = 'eng'
	# Unicode flag
	flag = '🇺🇸'
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
	feedback = 'Feedback received, please join %s if you\'d like to add more details'
	title = 'Artifact Rater Bot Help'
	change = 'To change languages click on the corresponding flag below'
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

	help_description = '''If you would like to add it to your private server use the [link](%s)
	You can also use the bot by sending the command in a DM to Artifact Rater#6924.'''

	help_source = '''If you have any issues, please contact shrubin#1866 on discord or use the -feedback command.
	Source code available at [GitHub](%s)'''

	help_feedback_name = '-feedback <message> [image]'
	help_feedback_value = 'Send feedback with issues or ideas for the bot. Up to one image can be sent.'

	help_rate_name = '-rate <image/url> [lvl=<level>] [<stat>=<weight> ...]'
	help_rate_value = '''\
	Rate an artifact against an optimal 5* artifact. Put the command and image in the same message.

	If you are using Windows 10, you can use Shift + Windows + S and drag your cursor over the artifact, then go to discord and paste it with Ctrl+V.

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
	requested = 'Pedido por %s'
	join = 'Si tienes algún problema, [únete al servidor]%s oficial'
	feedback = 'Feedback recibido, por favor, únete al servidor si deseas añadir más detalles: %s'

	err = 'Error'
	err_not_found = 'Error: No se encuentra la imagen o la url no funciona, asegurate de mandarla en el mismo mensaje'
	err_parse = 'Error: el comando no ha podido ejecutarse, asegurate de que esté bien escrito y el formato sea correcto'
	err_try_again = 'por favor, prueba de nuevo en un rato'
	err_unknown_ocr = 'Error: el OCR ha fallado con un error desconocido'
	err_unknown = 'Error desconocido, intenta subir una imagen con la página de artefactos completa'

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
	uid = 'de'
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
	feedback = 'Feedback erhalten, bitte joine %s wenn du weitere Details hinzufügen möchtest'

	err = 'Fehler'
	err_not_found = 'Fehler: Kein Bild oder URL gefunden, bitte stelle sicher das sich das Bild in der selben Nachicht befindet'
	err_parse = 'Fehler: Kein Befehl gefunden, bitte schau das du ihn richtig und im korrekten Format geschrieben hast'
	err_try_again = 'bitte versuche es in ein paar Minuten nochmal'
	err_unknown_ocr = 'Fehler: OCR fehlgeschlagen mit unbekanntem Fehler'
	err_unknown = 'Unbekannter Fehler, verwende ein Bild von der Inventar Artefakt Seite'

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
	uid = 'fr'
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
	feedback = 'Si vous avez un retour d\'informations, s\'il vous plait rejoignez %s si vous voulez rajouter plus de détails'

	err = 'Erreur'
	err_not_found = 'Erreur: Aucune image ou url n\'a été trouvée, s\'il vous plait assurez vous qu\'elle a était envoyée avec le message'
	err_parse = 'Erreur: La commande ne peut pas être analyser, vérifier le format et l\'orthographe'
	err_try_again = 'Merci de réessayer dans quelques minutes'
	err_unknown_ocr = 'Erreur: OCR a échoué a cause d\'une erreur inconnue'
	err_unknown = 'Erreur inconnue, essayer d\'utiliser une image d\'artefact venant de la page d\'inventaire'

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
	uid = 'vi'
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
	requested = 'Người đặt lệnh: %s'
	join = 'Để báo cáo vấn đề gặp phải, hãy tham gia [Artifact Rater Server]%s'
	feedback = 'Góp ý đã được tiếp nhận, hãy tham gia %s nếu bạn muốn cung cấp thêm chi tiết'

	err = 'Lỗi'
	err_not_found = 'Lỗi: Không tìm thấy ảnh hoặc link, 1 trong 2 phải được gửi chung trong cùng 1 tin nhắn'
	err_parse = 'Lỗi: Không thể xử lý lệnh, vui lòng kiểm tra lại định dạng và chính tả'
	err_try_again = 'hãy thử lại trong vài phút nữa'
	err_unknown_ocr = 'Lỗi: OCR đọc ảnh thất bại lỗi không xác định'
	err_unknown = 'Lỗi không xác định, hãy sử dụng ảnh chụp trong Túi > Thánh Di Vật'

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
	uid = 'pt'
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
	feedback = 'Feedback recebido, por favor junte-se ao servidor se quiser adicionar mais detalhes: %s'

	err = 'Erro'
	err_not_found = 'Erro: Nenhuma imagem ou url encontrada, certifique-se de que foram enviadas na mesma mensagem'
	err_parse = 'Erro: Comando não pôde ser executado, por favor cheque a formatação e a ortografia'
	err_try_again = 'por favor tente novamente em alguns minutos'
	err_unknown_ocr = 'Erro: OCR falhou com um erro desconhecido'
	err_unknown = 'Erro desconhecido, tente usar uma imagem da página de artefatos'

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
	uid = 'ja'
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

	hp_opt = 'hp'
	heal_opt = '治癒効果'
	df_opt = '防御力'
	er_opt = '元素チャージ効率'
	em_opt = '元素熟知'
	atk_opt = '攻撃力'
	cr_opt = '会心率'
	cd_opt = '会心ダメージ'
	phys_opt = '物理ダメージ'
	elem_opt = '元素ダメージ'
	lvl_opt = 'レベル'

	piece_set = '2セット'

	replace = {'カ': '力'}

	lvl = 'レベル'
	score = '装備スコア'
	main_score = 'メインステータス評価'
	sub_score = 'サブステータス評価'
	art_level = '聖遺物レベル'
	requested = '％sからのリクエスト'
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
	uid = 'pl'
	code = 'pol'
	flag = '🇵🇱'
	supported = True

	lvl = 'Level'
	score = 'Wynik ogólny'
	main_score = 'Ocena głównej statystyki'
	sub_score = 'Ocena podstatystyk'
	art_level = 'Poziom artefaktów'
	requested = 'Wywołano przez %s'
	join = 'W przypadku problemów, dołącz na [Artifact Rater Server]%s'
	feedback = 'Otrzymaliśmy feedback, dołącz na serwer %s jeżeli chciałbyś dodać więcej szczegółów.'

	err = 'Błąd'
	err_not_found = 'Błąd: Nie znaleziono URL ani obrazu, upewnij się czy zostały wysłane w tej samej wiadomości.'
	err_parse = 'Błąd: Komenda nie może zostać sparsowana, sprawdź jeszcze raz jej format i pisownię.'
	err_try_again = 'spróbuj ponownie za kilka minut'
	err_unknown_ocr = 'Błąd: OCR zawiódł z nieznanym błędem.'
	err_unknown = 'Nieznany błąd, spróbuj użyć zrzutu ekranu zawierającego zakładkę z artefaktami w ekwipunku'

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
	uid = 'ru'
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

	hp_opt = 'НР'
	heal_opt = 'Лечение'
	df_opt = 'Защита'
	er_opt = 'Восст'
	em_opt = 'Мастерство'
	atk_opt = 'Атака'
	cr_opt = 'Крит.Шанс'
	cd_opt = 'Крит.Урон'
	phys_opt = 'Физ'
	elem_opt = 'Элем'
	lvl_opt = 'лвл'

	piece_set = '2 предмета'

	lvl = 'Уровень'
	score = 'Общая оценка'
	main_score = 'Оценка главного стата'
	sub_score = 'Оценка вторичных статов'
	art_level = 'Уровень артефакта'
	requested = 'Запрос в %'
	join = 'Если у вас возникли проблемы, присоединяйтесь к [Artifact Rater Server]%s'
	feedback = 'Отзыв получен, присоединяйтесь к %s для большей информации.'

	err = 'Ошибка'
	err_not_found = 'Ошибка: изображение или url не найдены, убедитесь, что отправляете в одном сообщении с командой.'
	err_parse = 'Ошибка: команда не распознана. Пожалуйста, проверьте правильность ввода.'
	err_try_again = 'Пожалуйста, попробуйте чуть позже.'
	err_unknown_ocr = 'Ошибка: неизвестная ошибка распознавания текста.'
	err_unknown = 'Неизвестная ошибка, попробуйте использовать изображение из инвентаря/со страницы артефакта.'

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
	uid = 'tw'
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

	hp_opt = '生命'
	heal_opt = '治療'
	df_opt = '防禦'
	er_opt = '元素充能'
	em_opt = '元素精通'
	atk_opt = '攻擊'
	cr_opt = '暴傷'
	cd_opt = '暴率'
	phys_opt = '物理'
	elem_opt = '元素'
	lvl_opt = '等級'

	piece_set = '套裝'

	lvl = '等級'
	score = '聖遺物評分'
	main_score = '主屬性評分'
	sub_score = '副屬性評分'
	art_level = '聖遺物等級'
	requested = '%s要求'
	join = '有任何問題,請加入 [Artifact Rater Server]%s'
	feedback = '已經收到你的意見,如果您想獲得更多詳細信息 請加入%s'

	err = '錯誤'
	err_not_found = '錯誤:找不到圖片或網址,請確保他們在同一條訊息中發送'
	err_parse = '錯誤:無法解析命令,請仔細檢查格式和拼寫'
	err_try_again = '錯誤:請在幾分鐘後再試一次'
	err_unknown_ocr = '錯誤:OCR失敗,出現未知錯誤'
	err_unknown = '未知錯誤,嘗試使用測試頁面中的圖片\'s測試頁面'

	help_description = '''如果要將其添加到您的伺服器,請使用以下[鏈接](%s)
	您可以通過將命令發送來使用該機器人 Artifact Rater#6924.'''

	help_source = '''如果有什麼問題,請在discord聯繫 shrubin#1866 或使用-feedback命令.
	源代碼位於[GitHub](%s)'''

	help_feedback_name = '-feedback <message> [image]'
	help_feedback_value = '發送有關機器人的問題或意見.最多可以發送一張圖像.'

	help_rate_name = '-rate_tw <image/url> [lvl=<level>] [<stat>=<weight> ...]'
	help_rate_value = '''\
	針對5星聖遺物進行等級評分.請將命令和圖像放在同一條消息中.
	如果您使用的是Windows 10,您可以使用 Shift + Windows + S 並將鼠標拖到畫面上,然後去discord使用 Ctrl+V 貼上.

	預設權重
	攻擊%, 各種傷害%, 爆擊 - 1
	攻擊, 元素精通, 元素充能 - 0.5
	其他 - 0
	選項
	lvl: 指定聖遺物的等級進行比較 (預設: <聖遺物_等級>)
	-rate_tw lvl=20
	<stat>: 設置自定義權重 (值介於0至1)
	-rate_tw atk=1 er=0 atk%=0.5
	<stat> 值可以是以下任何 生命(HP), 生命%(HP%), 攻擊(ATK), 攻擊%(ATK%), 元素充能(ER), 元素精通(EM), 物理傷害(PHYS), 爆率(CR), 爆傷CD, 元素傷害(ELEM), 治療(Heal), 防禦(DEF), 防禦%(DEF%)
	'''

class cn(translation):
	uid = 'cn'
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

	hp_opt = '生命'
	heal_opt = '治疗'
	df_opt = '防御'
	er_opt = '元素充能'
	em_opt = '元素精通'
	atk_opt = '攻击'
	cr_opt = '暴伤'
	cd_opt = '暴率'
	phys_opt = '物理'
	elem_opt = '元素'
	lvl_opt = '等级'

	piece_set = '套装'

	lvl = '等级'
	score = '圣遗物评分'
	main_score = '主属性评分'
	sub_score = '副属性评分'
	art_level = '圣遗物等级'
	requested = '%s要求'
	join = '有任何问题,请加入 [Artifact Rater Server]%s'
	feedback = '已经收到你的意见,如果您想获得更多详细信息 请加入%s'

	err = '错误'
	err_not_found = '错误:找不到图片或网址,请确保他们在同一条讯息中发送'
	err_parse = '错误:无法解析命令,请仔细检查格式和拼写'
	err_try_again = '错误:请在几分钟后再试一次'
	err_unknown_ocr = '错误:OCR失败,出现未知错误'
	err_unknown = '未知错误,尝试使用测试页面中的图片\'s测试页面'

	help_description = '''如果要将其添加到您的伺服器,请使用以下[链接](%s)
	您可以通过将命令发送来使用该机器人 Artifact Rater#6924.'''

	help_source = '''如果有什么问题,请在discord联系 shrubin#1866 或使用-feedback命令.
	源代码位于[GitHub](%s)'''

	help_feedback_name = '-feedback <message> [image]'
	help_feedback_value = '发送有关机器人的问题或意见.最多可以发送一张图像.'

	help_rate_name = '-rate_cn <image/url> [lvl=<level>] [<stat>=<weight> ...]'
	help_rate_value = '''\
	针对5星圣遗物进行等级评分.请将命令和图像放在同一条消息中.
	如果您使用的是Windows 10,您可以使用 Shift + Windows + S 并将鼠标拖到画面上,然后去discord使用 Ctrl+V 贴上.

	预设权重
	攻击%, 各种伤害%, 爆击 - 1
	攻击, 元素精通, 元素充能 - 0.5
	其他 - 0
	选项
	lvl: 指定圣遗物的等级进行比较 (预设: <圣遗物_等级>)
	-rate_cn lvl=20
	<stat>: 设置自定义权重 (值介于0至1)
	-rate_cn atk=1 er=0 atk%=0.5
	<stat> 值可以是以下任何生命(HP), 生命%(HP%), 攻击(ATK), 攻击%(ATK%), 元素充能(ER), 元素精通(EM), 物理伤害(PHYS), 爆率(CR), 爆伤CD, 元素伤害(ELEM), 治疗(Heal), 防御(DEF), 防御%(DEF%)
	'''

# Text only, no game translation
class it(translation):
	uid = 'it'
	code = 'ita'
	flag = '🇮🇹'
	supported = True

	lvl = 'Livello'
	score = 'Punteggio dell\'Artefatto'
	main_score = 'Valutazione della Statistica Principale'
	sub_score = 'Valutazione delle Statistiche Secondarie'
	art_level = 'Livello dell\'Atefatto'
	requested = 'Richiesto da %s'
	join = 'In caso di probelmi, unisciti al [Artifact Rater Server]%s'
	feedback = 'Feedback ricevuto, unisciti al server discord per aggiunere ulteriori dettagli: %s'

	err = 'Errore'
	err_not_found = 'Errore: Nessun URL o immagine sono stati trovati, assicurarsi che siano stati spediti nello stesso messaggio'
	err_parse = 'Errore: Il comando non può essere analizzato, ricontrollare il formato e la compitazione'
	err_try_again = 'Riprova tra un qualche minuto'
	err_unknown_ocr = 'Errore: OCR ha fallito per un errore sconosciuto'
	err_unknown = 'Errore sconosciuto, prova utilizzando un\'immagine proveniente dalla pagina di artefatti'

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

class idn(translation):
	uid = 'id'
	code = 'idn'
	flag = '🇮🇩'
	supported = True

	lvl = 'Level'
	score = 'Skor Gear'
	main_score = 'Nilai Main Stat'
	sub_score = 'Nilai Substat'
	art_level = 'Level Artefak'
	requested = 'Diminta oleh %s'
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

languages = {lang.uid: lang for lang in [en, es, de, fr, vi, pt, ja, pl, ru, tw, cn, it, idn]}
