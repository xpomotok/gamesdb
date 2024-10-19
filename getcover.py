# coding: utf-8
'''
	Программа для скачивания обложек игр.
	Сохраняет оригинал в папку covers и копию 128х128 в thumbs.
	Предназначена для использования из расширения IOS.
'''

__version__ = '1.0.0'

__all__ = []

__author__ = 'Sergey Kuzmin <@gmail.com>'
import appex
import console

from PIL import Image
import sys
if sys.version_info[0] >= 3:
	from urllib.request import urlretrieve
else:
	from urllib import urlretrieve
	
size = 128, 128

def get_cover(url, fname):
	img_name = "covers/"+fname+".jpg"
	thumb_name = "thumbs/"+fname+".jpg"
	
	#try:
	urlretrieve(url, img_name)
	img = Image.open(img_name)
	
	w, h = img.size
	if w != h:
		w = 192
		h = 256
	else:
		w = 256
		h = 256
		
	#img.thumbnail(size, Image.ANTIALIAS)
	img.thumbnail((w,h), Image.ANTIALIAS)
	img.save(thumb_name, "JPEG")
	img.show()
		
	#except :
		# print("Error retrieving image!")
	
def main():
	if not appex.is_running_extension():
		print('This script is intended to be run from the sharing extension.')
		return
		
	fname = input()
	
	text = appex.get_url()
	if not text:
		print('No url provided.')
		return
	
	get_cover(text, fname)
	
	
if __name__ == "__main__":
	main()
