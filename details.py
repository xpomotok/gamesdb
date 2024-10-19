''' 
Тест формы с деталями об игре 
'''

import ui
from game import Game

covers = "covers/"
thumbs = "thumbs/"
viewname = "ui/details"
game1 = Game('Doom (2016)')
game1.title = 'DOOM 2016'
game1.genre = 'RPG'
game1.platform = 'Windows'
game1.released = '2016'
game1.notes = 'Very brutal, very interesting'
game1.interest = '97'
game1.image='DOOM 2016.jpg'
game1.finished = 'True'
game1.notes = "Во всех платформах кроме Nintendo Switch, присутствует встроенная утилита для создания уровней, называемая «SnapMap», которая позволяет игрокам создавать и редактировать карты со своей собственной структурой и игровой логикой.[16] С помощью SnapMap, игроки могут создавать карты для разных режимов, начиная от одиночных и заканчивая кооперативным или многопользовательскими картами."


v = ui.load_view(viewname)
v.name = game1.title
# v.frame = (0,0,1920,1080)

if game1:
	if game1.image != "":
		img = ui.Image(''.join([covers, game1.image]))
	else:
		img = ui.Image(''.join([covers, "unknown_game.png"]))
			
	imv = v['imageview1']
	
	ui.TableViewCell.image_view.
	ui.ImageView.
	imv.image = img
	# imv.flex = 'tb'
	imv.content_mode = ui.CONTENT_SCALE_ASPECT_FIT
		
		
		
# v['labelTitle'].text = game1.title
v['labelFinished'].text = game1.finished
v['labelReleased'].text = game1.released
v['labelPlatform'].text = game1.platform
v['labelGenre'].text = game1.genre
v['labelRating'].text = game1.interest
	
v['textview1'].text = game1.notes
	
v.present('sheet')
