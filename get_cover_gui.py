import ui
import appex
import console

from PIL import Image
import sys
if sys.version_info[0] >= 3:
	from urllib.request import urlretrieve
else:
	from urllib import urlretrieve
	
size = 128, 128

def get_cover(url : str, fname : str) -> Image:
	img_name = fname+".jpg"
	thumb_name = "t_" +fname+".jpg"
	
	#try:
	urlretrieve(url, img_name)
	#img = Image.open(img_name)
	return  ui.Image(img_name)
	#img.thumbnail(size, Image.ANTIALIAS)
	#img.save(thumb_name, "JPEG")
	#img.show()


url ="https://images-na.ssl-images-amazon.com/images/I/91r8dD6dHOL._AC_SL1500_.jpg"
fname = "skyrim.jpg"


def save_to_file(sender):
	if sender.text:
		
		thumb_name = "t_" + sender.text + ".jpg"
		img = Image.open(fname)

		img.thumbnail(size, Image.ANTIALIAS)
		img.save(thumb_name, "JPEG")
	
		console.hud_alert("Done!")
		sender.superview.close()


def factory_image(l, t, width=24, height=24, pict=None) -> ui.Image:
	
	if pict:
		pict = ui.Image(fname)
		w, h= pict.size
		
		if w != h:
			w = 192
			h = 256
		else:
			w = 256
			h = 256
	else:
		w = width
		h = height
	
	#print(w,h)
	#left = (vmain.width / 2) - 96
	
	img = ui.ImageView(frame=(l, t, w, h))
	
	img.background_color = "white"
	img.corner_radius = 14
	#img.border_width = 1
	img.bordered = False
	#img.border_color = 'green'
	
	if pict:
		img.image = pict
	
	return img


def factory_shadow(w,h):
	print(w,h)
	with ui.ImageContext(w, h) as ctx:
		ui.set_shadow('#e2e2e2',3,3,2)
		ui.set_color('white')
		ui.fill_rect(0, 0, w-5, h-5)
		ui.set_color('white')
		
		shadow = ui.Path.rounded_rect(0, 0, w-14, h-14, 5)
		shadow.fill()
		
		custom_img = ctx.get_image()
		
		return custom_img

def factory_view(l, t, w, h, name):
	v = ui.View(frame=(l, t, w, h), hide_close_button=True)
	v.background_color= '#c0c0c0'
	#vmain.background_color = "white"
	v.name = name
	
	return v

def main():
	vmain = factory_view(0,0,400,400, 'Save to file')
	
	left = (vmain.width / 2) - 128
	top = 20
	
	#img = factory_image(left+10, top+10, 192, 256)
	
	# frame original picture
	img = factory_image(left-8, top-8, 256+16, 256+16)
	#img.image = factory_shadow(192, 256)
	
	
	vmain.add_subview(img)
	
	img1 = factory_image(left, top, pict=fname)
	vmain.add_subview(img1)
	
	el = 14
	et= 64 + 256
	ew = vmain.width - 14
	eh = 48
	
	editf = ui.TextField(frame=(el, et, ew, eh))
	editf.background_color = '#e2e2e2'
	#editf.border_width = 2
	#editf.bordered = True
	editf.corner_radius = 14
	#editf.border_color = 'grey'
	editf.placeholder = "File name"
	editf.clear_button_mode = "while_editing"
	editf.action = save_to_file
	
	vmain.add_subview(editf)
	
	
	
	vmain.present('sheet')
	
if __name__ == "__main__":
	
	if not appex.is_running_extension():
		print('This script is intended to be run from the sharing extension.')
		return
		
	fname = input()
	
	text = appex.get_url()
	if not text:
		print('No url provided.')
		return
	
	get_cover(text, fname)
	
	main()
