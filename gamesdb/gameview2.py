'''
	Программа для добавления игр в wishlist.
	Может использоваться из расширения IOS 
	
	31.03.2020 - добавлена опция стирания данных в текстовых полях
'''

__version__ = '1.0.1'

__all__ = []

__author__ = 'Sergey Kuzmin <@gmail.com>'

import appex
import ui
from console import hud_alert
from models.game import Game
from models.gamelist import GameList

viewname = "ui/GameView2"

def button_tapped(sender):
	'@type sender: ui.Button'
	# Get the button's title for the following logic:
	t = sender.title
	Games = GameList("Wishlist")
	Games.load("db/wishlist.json")
	
	# label = sender.superview['label1']
	if t == 'Save':
		s_title = sender.superview['textfield1']
		s_genre = sender.superview['textfield2']
		s_platform = sender.superview['textfield3']
		s_released = sender.superview['textfield4']
		#s_notes = sender.superview['textview1']
		s_image = sender.superview['textfield6']
		
		new_game = Game(s_title.text)
		new_game.genre = s_genre.text
		new_game.platform = s_platform.text
		new_game.released = s_released.text
		#new_game.notes = s_notes.text
		new_game.image = s_image.text
		
		Games.add(new_game)
		
		Games.save("db/wishlist.json")
		
		hud_alert('Done.')
		#new_game.print_game()
		
		sender.superview.close()
		
def is_extension():
	if not appex.is_running_extension():
		print('This script is intended to be run from the sharing extension.')
		return False
	else:
		return True
		
# для удобства отладки добавлен Appexed
def main():
	Appexed = is_extension()
	
	
	v = ui.load_view(viewname)
	v['textfield1'].clear_button_mode = 'while_editing'
	v['textfield2'].clear_button_mode = 'while_editing'
	v['textfield3'].clear_button_mode = 'while_editing'
	v['textfield4'].clear_button_mode = 'while_editing'
	v['textfield6'].clear_button_mode = 'while_editing'
	
	
	debug = list()
	if Appexed:
		v['textfield1'].text = appex.get_text()
		debug = appex.get_images()
		print("List: {}".format(debug))
	else:
		v['textfield1'].text = "No one"
	
	if ui.get_screen_size()[1] >= 768:
		# iPad
		v.present('sheet')
	else:
		# iPhone
		v.present()
		
	
if __name__ == "__main__":
	main()
