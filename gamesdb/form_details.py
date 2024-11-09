import ui

#import main_gamesdb
from models.game import Game
from ui_config import ui_config, Config
from form_edit import FormEdit


class FormDetails:
	
	def __init__(self, cur_game: Game):
		# print(CurGame)
		self.CurrentGame = cur_game
		# print(self.CurrentGame)
		
	def btn_edit_clicked(self, sender):
		# should be simple FormEdit.show()
		Editor = FormEdit(self.CurrentGame)
		self.FormEdit = Editor.Form
		self.FormEdit.present('sheet', hide_close_button=True)

	def show(self) -> ui.View:
		vu = ui.load_view("gui/details.pyui")
		
		rbtn1 = ui.ButtonItem(title='Edit')
		# rbtn1= ui.ButtonItem(title='', image='iob:ios7_copy_outline_24')
		rbtn1.action = self.btn_edit_clicked
		
		vu.right_button_items = rbtn1,
		
		game1 = self.CurrentGame
		
		if game1:
			img = load_image(game1.image)

			vs = vu['scrollview1']
			imv = vs['imageview1']
			
			imv.image = img
			imv.flex = 'tb'
			imv.content_mode = ui.CONTENT_SCALE_ASPECT_FIT

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
		return vu
		
		
def load_image(image) -> ui.Image:
    if image != "":
        return ui.Image(''.join([Config.covers_path, image]))
    else:
        return ui.Image(''.join([Config.covers_path, Config.default_image]))

