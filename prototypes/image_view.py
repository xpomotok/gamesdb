#!python3

'''
This widget script shows thumbnails of photos that were recently added to the photo library.

Tapping the widget opens the Photos app.
'''

import appex
import ui
import photos

def widget_tapped(sender):
	import webbrowser
	webbrowser.open('photos-redirect://')


pth = "../thumbs/"
images = [pth+"Brahma.jpg", pth+"ArmA 3.jpg", pth+"BoF3.jpg", pth+"Gladius.jpg"]

w = 120
h = 120

if True:
	v = ui.View(frame=(0, 0, 360, 120))
	
	for i, j in enumerate(images):
		img_view = ui.ImageView(flex='tb', frame=(i * (w+10), 0, w, h))
		img_view.content_mode = ui.CONTENT_SCALE_ASPECT_FILL
		img_view.flex = 'tb'
		img_view.image = ui.Image(j, size=(120,120))
		v.add_subview(img_view)
		
	tap_button = ui.Button(frame=v.bounds, flex='wh', action=widget_tapped)
	v.add_subview(tap_button)
	
	appex.set_widget_view(v)
	
else:
	appex.set_widget_view(None)
	print('Cannot access photos')
