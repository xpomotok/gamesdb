""" 
	Class for representing list of games
"""

__version__ = '0.0.9.1'

__all__ = ["GameList"]

__author__ = 'Sergey Kuzmin <@gmail.com>'

import codecs
import json

from gamesdb.models.game import Game


class GameList(object):
	def __init__(self, title: str):
		self.title = title
		self.cursor = 0
		self.count = 0
		self.games = []

	def add(self, game):
		# print(game.title)
		self.games.append(game)
		self.count += 1

	def update(self, game):
		self.games[self.cursor] = game

	def remove(self):
		if self.count > 0:
			self.count -= 1
		return self.games.pop(self.cursor)	

	def sort_by_name(self, order):
		pass

	def get(self):
		return self.games[self.cursor]

	def dec_cursor(self):
		if self.cursor > 1:
			self.cursor -= 1
			
	def inc_cursor(self):	
		if self.cursor < self.count:
			self.cursor += 1

	def move_up(self):
		i = self.cursor
		if i > 0:
			tmp = self.games[i-1]
			self.games[i-1] = self.games[i]
			self.games[i] = tmp
			
	def move_down(self):
		i = self.cursor
		if i < self.count - 1:
			tmp = self.games[i+1]
			self.games[i+1] = self.games[i]
			self.games[i] = tmp
		
	def get_by_title(self, game_name):
		print("Searching for {}".format(game_name))

		# new: if game_name in games ?
		for g in self.games:
			# print(type(g))
			if g.title == game_name:
				return g
		else:
			return None

	def _load_json_(self, fname):
		try:
			with codecs.open(fname, "rU", "utf-8") as fp:
				return json.load(fp)

		except OSError as E:
			print("Something '{}', actually, went wrong".format(E.strerror))
			return None

	def _save_json_(self, fname, js):
		try:
			# 2. А это вторая часть - файл открывается для записи, но в него ничего 
			# не попадает из-за 1
			# with codecs.open(fname, "w", "utf-8") as fp:
			with codecs.open(fname, "r+", "utf-8") as fp:
				map = ""
				# 1. Это одна часть кода, который может испортить файл с базой
				# json.dump(js, fp, indent=4, ensure_ascii=False)
				try:
					map = json.dumps(js, indent=4, ensure_ascii=False)
				except TypeError as E:
					print("Something '{}', actually, went wrong".format(E))
					return

				print("Saving to file \"{}\"".format(fname))
				fp.writelines(map)
						
		except OSError as E:
			print("Something '{}', actually, went wrong".format(E.strerror))

	def load(self, fname):
		map = self._load_json_(fname)

		if (map != None):
			version_map = map["version"]

			# print(version_map)
			games_map = map["games"]

			for item in games_map:
				# не удалять !
				#print(type(item))
				#print(item)

				game = Game("")
				game.deserialize(item)
				self.add(game)

			# print("Games loaded {}".format(counter))
			# print(self.games)

	def save(self, fname):
		dict_list = []
		new_games_map = {}
		
		new_games_map["version"] = "1.1"
		
		for game in self.games:
			game_d = game.serialize()
			dict_list.append(game_d)
		
		new_games_map["games"] = dict_list
		# print(new_games_map)
		self._save_json_(fname, new_games_map)
			
	def print_list(self):
		for g in self.games:
			g.print_game()
			print("---------------")
		print("Games total: {}".format(self.count))

	def get_count(self):
		return self.count


