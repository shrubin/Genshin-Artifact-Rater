class translation:
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

class en(translation):
	ignore = ['in']

class es(translation):
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

class de(translation):
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

class fr(translation):
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
