#03.06.2022- Initial import
import ui
from models.game import Game
from ui_config import ui_config
from form_edit import FormEdit
# from PIL import Image

# Здесь тоже не помешает класс
class FormDetails():
	
	def __init__(self, CurGame : Game):
		# print(CurGame)
		self.CurrentGame = CurGame
		# print(self.CurrentGame)
		
	def btn_edit_clicked(self, sender):
		Editor = FormEdit(self.CurrentGame)
		self.FormEdit = Editor.Form
		self.FormEdit.present('sheet', hide_close_button=True)

	def show_details(self):
		vu = ui.load_view("gui/details.pyui")
		
		rbtn1= ui.ButtonItem(title='Edit')
		#rbtn1= ui.ButtonItem(title='', image='iob:ios7_copy_outline_24')
		rbtn1.action = self.btn_edit_clicked
		
		vu.right_button_items = rbtn1,
		
		game1 = self.CurrentGame
		
		if game1:
			if game1.image != "":
				img = ui.Image(''.join([ui_config.covers_path, game1.image]))
			else:
				img = ui.Image(''.join([ui_config.covers_path, "unknown_game.png"]))
			vs = vu['scrollview1']
			imv = vs['imageview1']
			
			
			imv.image = img
			imv.flex = 'tb'
			imv.content_mode = ui.CONTENT_SCALE_ASPECT_FIT
			#btn_edit = vu['btn_edit']
			
			#btn_edit.action = self.btn_edit_clicked
			
			# vu['labelTitle'].text = game1.title
			
			
			if game1.finished:
				vs['labelFinished'].text = "Finished"
			else:
				vs['labelFinished'].text = "Not yet"
				
			vs['labelReleased'].text = game1.released
			vs['labelPlatform'].text = game1.platform
			vs['labelGenre'].text = game1.genre
			vs['labelRating'].text = str(game1.rating)
			vs['labelInterest'].text = str(game1.interest)
		
			if game1.is_playing:
				vs['labelIsPlaying'].text = "Да"
			else:
				vs['labelIsPlaying'].text = "Нет"
			
			vs['textview1'].text = game1.notes
			# для работы с родным navigation
			#v.nav.push_view(vu)
			#vu.present()
		# nav.push_view(vu)
		return vu