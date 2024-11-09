import ui

#import main_gamesdb
from models.game import Game
from ui_config import ui_config, Config
from form_edit import FormEdit
from console import hud_alert

class FormDetails:
	
	def __init__(self, cur_game: Game):
		# print(CurGame)
		self.CurrentGame = cur_game
		# print(self.CurrentGame)
		
	def btn_edit_clicked(self, sender):
		# should be simple FormEdit.show()
		Editor = FormEdit(self.CurrentGame)
		self.FormEdit = Editor.Form
		self.FormEdit.background_color = Config.color_main_back
		self.FormEdit.present('sheet', hide_close_button=True)
		
	def add_data(self, title, data):
		value = "{}\t\t\t{}".format(title, data)
		
		return {'title':value,'image':None,'accessory_type':'none'}
		
	def show(self) -> ui.View:
		vu = ui.load_view("gui/details-new.pyui")
		
		rbtn1 = ui.ButtonItem(title='Edit')
		# rbtn1= ui.ButtonItem(title='', image='iob:ios7_copy_outline_24')
		rbtn1.action = self.btn_edit_clicked
		
		vu.right_button_items = rbtn1,
		
		game1 = self.CurrentGame
		
		if game1:
			img = load_image(game1.image)

			vs = vu['view1']
			imv = vu['imageview1']
			
			imv.image = img
			imv.flex = 'tb'
			imv.content_mode = ui.CONTENT_SCALE_ASPECT_FIT

			vu.name = game1.title
		
			game_data = []
			game_data.append(self.add_data('Genre', game1.genre))
			game_data.append(self.add_data('Released', game1.released))
			game_data.append(self.add_data('Platform', game1.platform))
			
			game_data.append(self.add_data('Rating', game1.rating))
			game_data.append(self.add_data('Finished', game1.finished))
			game_data.append(self.add_data('Interest', game1.interest))
			
			tds = ui.ListDataSource(game_data)
			tv = vu['tableview1']
			tv.data_source = tds
			tv.reload()
			
		return vu
		
		
def load_image(image) -> ui.Image:
    if image != "":
        return ui.Image(''.join([Config.covers_path, image]))
    else:
        return ui.Image(''.join([Config.covers_path, Config.default_image]))
