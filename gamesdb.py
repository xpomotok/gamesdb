
__version__ = '0.0.3'

__all__ = []

__author__ = 'Sergey Kuzmin <@gmail.com>'


from game import Game
from gamelist import GameList


class GamesDb(object):
	covers = "covers/"
	thumbs = "thumbs/"
	
	
	whish = "db/wishlist.json"
	nowplaying = "db/playing.json"
	print("Hallou!")
	
GamesDb()
