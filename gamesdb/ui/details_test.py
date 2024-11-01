''' 
Тест формы со скроллированием
'''

import ui


covers = "../covers/"
thumbs = "../thumbs/"
viewname = "details2"



v = ui.load_view(viewname)
v.name = "Doom"
vs = ui.ScrollView()
vs = v['scrollview1']
#vs.frame = (0,0,320,240)
vs.border = 2

lbl = ui.Label('Hello')
lbl.text = 'Hello'
lbl.frame = (10,10,200,64)

vs.add_subview(lbl)
#vs.content_size = (320,640)

img = ui.Image(''.join([covers, "unknown_game.png"]))
			
imv = v['imageview1']

imv.image = img
	# imv.flex = 'tb'
imv.content_mode = ui.CONTENT_SCALE_ASPECT_FIT
		
v['label1'].text = 'PS2'
		
# v['labelTitle'].text = game1.title
#v['labelFinished'].text = game1.finished
#v['labelReleased'].text = game1.released
#v['labelPlatform'].text = game1.platform
#v['labelGenre'].text = game1.genre
#v['labelRating'].text = game1.interest
	
#v['textview1'].text = game1.notes
	
v.present()
