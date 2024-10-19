# coding: utf-8
#
# deprecated
#

import appex
from html2text import html2text
import console
import re

from game import Game
from gamelist import GameList

def main():
	if not appex.is_running_extension():
		print('This script is intended to be run from the sharing extension.')
		return
	
	text = appex.get_text()
	if not text:
		print('No text input found.')
		return
	
	Games = GameList("Wishlist")
	Games.load("wishlist.json")
	NewGame = Game(text)
	Games.add(NewGame)
	
	Games.save("wishlist.json")
	
	console.alert('Game', '%s has been added' % (text), 'OK', hide_cancel_button=True)

if __name__ == '__main__':
	main()
	
