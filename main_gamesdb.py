# 01.06.2022 - нижнее меню обернуто в класс
# 01.06.2022 - кнопки нижнего меню создаются через класс нижнего меню
# 03.06.2022 - dummy a favor
# 25.06.2022 - Перенос внутрь Pythonista

__version__ = '0.1.2.6'

__all__ = []

__author__ = 'Sergey Kuzmin <@gmail.com>'


from typing import Collection
from ui_config import ui_config
import ui
import clipboard
from console import hud_alert
from game import Game
from gamelist import GameList
from text_view import text_view
from bottom_menu_class import BottomMenu
from form_details import FormDetails
from form_edit import FormEdit

# simple globals
covers = ui_config.covers_path
thumbs = ui_config.thumbs_path
whishname = "db/wishlist.json"
playname = "db/playing.json"
allname = "db/games.json"
WhishGames = GameList("Wishlist")
NowPlaying = GameList("Now Playing")
GameCollection = GameList("Collection")


class Controller (object):
	
	def update_view(self, name, model):
		
		if name == 'details':
			print(name)
		pass

class App (object):
	
	def __init__(self):
		self.Controller = Controller()
		
		self.MainWindow : ui.NavigationView
	
		self.FormEdit : ui.View
		self.FormDetails : ui.View
		self.FormListView : ui.View
		self.CurrentView : ui.View
		self.CurrentList : GameList
		self.CurrentGame : Game
		self.CurrentRow : int
		self.CurrentFile : str
		
		WhishGames.load(whishname)
		NowPlaying.load(playname)
		GameCollection.load(allname)
		
		
		self.create_main_view()
		self.CurrentList = WhishGames
		self.CurrentFile = whishname
		self.FormListView.name = self.CurrentList.title
		


	def create_main_view(self):
		
		self.FormListView = ui.View()
		
		self.FormListView = ui.load_view("ui/GameListView.pyui")
		
		self.Edit = ui.View()
		self.TableView = self.FormListView['tableview1']
		
		self.MainWindow = ui.NavigationView(self.FormListView)
		self.MainWindow.name = "Игродата"
		self.MainWindow.title_color = 'orange'
		self.MainWindow.tint_color = 'orange'
		self.MainWindow.background_color = 'white'
		#if (ui_config.has_bottom_menu):
			#add_bottom_menu()
		self.MainWindow.frame = (0, 0, 390, 734)
		bmenu_x = self.MainWindow.bounds[0]
		bmenu_w = self.MainWindow.bounds[2]
		bmenu_y = self.MainWindow.bounds[3]
		
		bmenu_h = 56
		ff = BottomMenu()
		ff.frame = (bmenu_x, bmenu_y - 80 - (bmenu_h), bmenu_w, bmenu_h + 56)
		#ff.frame = (bmenu_x, bmenu_y - 72 - (bmenu_h), bmenu_w, bmenu_h + 56)
		
		ff.add_button('Играю','iob:game_controller_a_32', self.view_playing)
		ff.add_button('Желаемое', 'iob:ios7_star_outline_32', self.view_whishlist)
		ff.add_button('Коллекция', 'iob:ios7_box_outline_32', self.view_collection)
		ff.add_button('Добавить', 'iob:ios7_compose_outline_32', self.view_new_game)
		
		self.FormListView.add_subview(ff)

		rbtn1= ui.ButtonItem(title='Save')
		#rbtn1= ui.ButtonItem(title='', image='iob:ios7_copy_outline_24')
		rbtn1.action = self.save_all
		
		self.MainWindow.right_button_items = rbtn1,
		self.MainWindow.present(style='fullscreen', hide_title_bar=False, hide_close_button=False)
		
	def run(self):		
		tv = self.TableView
		tv.delegate.tableview_did_select = self.tableview_did_select
		
		tds = ui.ListDataSource(items=self.CurrentList.games)
		tv.data_source = tds
		tv.data_source.tableview_cell_for_row = self.tableview_cell_for_row	
		tv.reload()
		
		tv.editable = True

	### Функции для работы с основным списком игр
	def tableview_did_select(self, tableview, section, row):
		# Called when a row is selected.
		self.CurrentGame = tableview.data_source.items[row]
		
		Details = FormDetails(self.CurrentList.games[row])
		# print(self.CurrentList.games[row])
		#Details = FormDetails(self.CurrentGame)
		self.FormDetails = Details.show_details()
		self.FormDetails.name = self.CurrentGame.title
		self.FormDetails.present('sheet', hide_close_button=False)
		#self.MainWindow.pop_view()
		
		#self.Controller.update_view('details', model)
		

	def tableview_cell_for_row(self, tableview, section, row):
		# Create and return a cell for the given section/row
		# print("test")
		#global ActualGame
		data: Game
		data = tableview.data_source.items[row]
		#ActualGame = data
		
		cell = ui.TableViewCell(style='subtitle')
		cell.accessory_type = 'disclosure_indicator'
		cell.text_label.text = data.title
		cell.detail_text_label.text = ''.join([data.platform, ", ", data.released])
			
		if data.image != "":
			img = ui.Image(''.join([covers, data.image]))
		else:
			img = ui.Image(''.join([covers, "unknown_game.png"]))
		
		
		#
		#cell.image_view.content_mode = 
		#cell.image_view.flex = 'tb'
		cell.image_view.image = img
	
		cell.image_view.flex = 'tb'
		cell.image_view.corner_radius = 6
		cell.image_view.flex = 'tb'
		# print(cell.image_view.flex)
		
		return cell

	def button_tapped(self, sender):
		'@type sender: ui.Button'
		sender.superview.close()
		pass
			
	def view_playing(self, sender):		
		self.CurrentList = NowPlaying
		self.CurrentFile = playname

		self.FormListView.name = self.CurrentList.title
		
		tv = self.TableView
		tds = ui.ListDataSource(items=NowPlaying.games)
		tv.data_source = tds
		tv.data_source.tableview_cell_for_row = self.tableview_cell_for_row
		
		tv.reload()
		
		#hud_alert('Button!')

	def view_whishlist(self, sender):
		self.CurrentList = WhishGames
		self.CurrentFile = whishname
		
		self.FormListView.name = WhishGames.title
		
		tv = self.TableView
		tds = ui.ListDataSource(items=WhishGames.games)
		tv.data_source = tds
		tv.data_source.tableview_cell_for_row = self.tableview_cell_for_row
		
		tv.reload()
		#hud_alert('Button!')		

	def view_collection(self, sender):
		self.CurrentList = GameCollection
		self.CurrentFile = allname
		
		self.FormListView.name = GameCollection.title
		
		tv = self.TableView
		tds = ui.ListDataSource(items=GameCollection.games)
		tv.data_source = tds
		tv.data_source.tableview_cell_for_row = self.tableview_cell_for_row
		
		tv.reload()
		

	def view_new_game(self, sender):
		# определить текущий список и добавить в него новую игру
		#self.CurrentList = GameCollection
		#self.CurrentFile = allname
		
		NewGame = Game('New')
		self.CurrentList.add(NewGame)
		self.CurrentGame = NewGame
		Editor = FormEdit(self.CurrentGame)
		self.FormEdit = Editor.Form
		self.FormEdit.present('sheet', hide_close_button=True)
		
		
	def save_all(self, sender):
		GameCollection.save(allname)
		WhishGames.save(whishname)
		NowPlaying.save(playname)
			

def main():
	GamesDb = App()
	GamesDb.run()
	
	
if __name__ == "__main__":
	main()
