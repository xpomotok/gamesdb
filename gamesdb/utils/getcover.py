'''
	Simple app for getting box cover art
	Save original image in "covers" and makes a copy 128x128 in "thumbs"
	Supposed to use as Pythonista extension on iOS
'''

__version__ = '1.0.0'

__all__ = []

__author__ = 'Sergey Kuzmin'

import appex
import console

from PIL import Image
import sys
if sys.version_info[0] >= 3:
	from urllib.request import urlretrieve
else:
	from urllib import urlretrieve

from ui_config import Config


config = Config()


def get_cover(url, file_name):
	img_name = "{}/{}.jpg".format(config.covers_path, file_name)
	thumb_name = "{}/{}.jpg".format(config.thumbs_path, file_name)
	
	urlretrieve(url, img_name)
	img = Image.open(img_name)
	
	w, h = img.size
	if w != h:
		w = 192
		h = 256
	else:
		w = 256
		h = 256
		
	img.thumbnail((w, h), Image.ANTIALIAS)
	img.save(thumb_name, "JPEG")
	img.show()


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
