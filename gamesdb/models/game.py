# coding: utf-8
''' 
Приложение для борьбы с ленью.
Пишу сюда по строчке в день.
Файл с объектами можно сортировать, хоть по названию, хоть по рейтингу

28.10.2019
08.11.2019
02.12.2019
06.12.2019
09.12.2019
18.12.2019
09.03.2020 - добавлены свойства для хранения описания и картинок
07.06.2022 - добавлен метод для обновления объекта 

	1. Посмотреть как мерить производительность
	2. Насколько ресурсоёмко итерироваться по списку объектов Game
'''

__version__ = '0.0.9'

__all__ = []

__author__ = 'Sergey Kuzmin <sergey.a.kuzmin@gmail.com>'

import codecs
import json
# import scommon

# from PIL import Image
# import sys
# if sys.version_info[0] >= 3:
# 	from urllib.request import urlretrieve
# else:
# 	from urllib import urlretrieve
# size = 128, 128


class Game(object):
	
	def __init__(self, title=""):
		self.title = title
		self.genre = ""
		self.interest = 0
		self.finished = False
		self.notes = ""
		self.platform = ""
		self.released = ""
		self.rating = 0
		self.image = ""
		# new
		self.description = ""
		self.pics = []
		self.is_playing = False
		
	def update(self, title='', genre='', platform='', interest=0, finished=False, notes='', released='', rating=0, cover=''):
		if title != '':
			self.title = title
		if genre != '':
			self.genre = genre
		if interest != 0:			
			self.interest = interest
		if finished != False:
			self.finished = finished
		if notes != '':
			self.notes = notes
		if platform != '':			
			self.platform = platform
		if released != '':
			self.released = released
		if rating != 0:			
			self.rating = rating
		if cover != '':			
			self.image = cover
		
	def print_game(self):
		print("Game: {}".format(self.title))
		print("Genre: {}".format(self.genre))
		print("Platform: {}".format(self.platform))
		print("Notes: ", self.notes)
		# print(self.__dict__)
		#print(type(self.title))
		
		# img_name = 'covers/'+self.title+'.jpg'
		# thumb_name = 'thumbs/'+self.title+'.jpg'
		
		if self.image != "":
			#urlretrieve(self.image, img_name)
			#img = Image.open(img_name)
			#img.thumbnail(size, Image.ANTIALIAS)
			#img.save(thumb_name, "JPEG")
			#img.show()
			pass
			
	def get_notes(self):
		return self.notes
		
	def set_notes(self, new_notes):
		self.notes = new_notes

	def deserialize(self, map: dict):
		"""
			Если словарь, прочитанный из файла неполон, то будет испорчен словарь обьекта,
			поэтому последовательно проходим все записи
		"""
		for key in map.keys():
			if key in self.__dict__:
				self.__dict__[key] = map[key]
		#self.__dict__ = map

	def serialize(self):
		return self.__dict__
		

if __name__ == "__main__":
	a = Game("Doom 2")
	b = Game("")
	
	b = a
	b.update(rating=50, released='2016', platform='Switch', notes='True 60FPS on Switch')
	b.print_game()
	
