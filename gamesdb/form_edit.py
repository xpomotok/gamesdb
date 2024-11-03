# 03.06.2022 - Initial import
# 07.06.2022 - Альтернативный вариант класса
# 16.06.2022 - Исправлены ошибки
__author__ = "Sergey Kuzmin"


import ui
from models.game import Game
from gui.my_text_view_delegate import MyTextViewDelegate
from ui_config import ui_config
from gui.my_table_edit import MyTableEditDataSource
from gui.my_text_field_delegate import MyTextFieldDelegate

class FormEdit():
	
	def __init__(self, game : Game):
		# объект нужен для чтения данных об описании
		self.EditDataSource : MyTableEditDataSource
		self.NotesTextView : ui.TextView
		
		self.EditDataSource = MyTableEditDataSource()
		
		self.CurrentGame = game
		#print(self.CurrentGame)
		# неудобный список - датасет для таблицы
		self.data = []
		self.did_update = False

		#self.Form = self.show_edit()
		self.Form = self.show_edit_new()
		
	def edit_close(self, sender):
		self.did_update = False
		
		self.Form.close()
		pass
	
	def save_all(self, sender):
		
		self.did_update = True
		
		Title = self.EditDataSource.input_provider[0].text
		Interest = self.EditDataSource.input_provider[1].text
		Rating = self.EditDataSource.input_provider[2].text
		Finished = self.EditDataSource.input_provider[3].text
		Platform = self.EditDataSource.input_provider[4].text
		Genre = self.EditDataSource.input_provider[5].text
		Released = self.EditDataSource.input_provider[6].text
		Cover = self.EditDataSource.input_provider[7].text
		self.CurrentGame.update(Title, Genre, Platform, Interest, False, self.NotesTextView.text, Released, Rating, Cover)
		
		self.Form.close()
		pass
	
	def show_edit_new(self) -> ui.View:
		game1 : Game
		game1 = self.CurrentGame	
	
		section0 = (game1.title,str(game1.interest),str(game1.rating), 'No')
		section1 = (game1.platform, game1.genre, game1.released,game1.image)
	
		self.data.append(section0)
		self.data.append(section1)

		ve = ui.View(frame=(0,0,375,768))
		ve.background_color = ui_config.form_color
		
		if game1.title == 'New':
			ve.name = "Add new game"
		else:
			ve.name = "Edit Game"
		
		vs = ui.ScrollView(frame=(0,0,375,768))
		vs.content_size = 374, 1080
	
		vs.scroll_enabled=True
		vs.background_color = ui_config.form_color #"#ffffff"
		
		rbtn1= ui.ButtonItem(title='Done')
		rbtn1.action = self.save_all
		lbtn2 = ui.ButtonItem(title='Cancel')
		lbtn2.action = self.edit_close
		
		tv1 = ui.TableView()
		#!!!
		tv1.scroll_enabled = False
		
		tv1.data_source = self.EditDataSource
		tv1.data_source.items = self.data
		
		tv1.frame = (16,16, 374-32, 430)
		tv1.name = 'EditorTable'
		tv1.corner_radius = 9
		tv1.border_width = 1
		vs.add_subview(tv1)
		#ve.add_subview(tv)
		
		# b = text_view('Details', 0,0)
		# vs.add_subview(b)
		
		# c = text_view('Notes', 0, 40+360-5)
		# vs.add_subview(c)
	
		# Текстовое поле для ввода описания 
		d = ui.TextView(frame=(16, 480, 374-32, 360))
		d.border_width = 1
		d.corner_radius = 6
		
		d.background_color = ui_config.edit_textview_color
		# d.font = (ui_config.edit_textview_font_face, ui_config.edit_textview_font_size)
		d.text = game1.notes
		d.delegate = MyTextViewDelegate()
		self.NotesTextView = d
		vs.add_subview(d)
		
		ve.right_button_items = rbtn1, 
		ve.left_button_items = lbtn2,
		ve.add_subview(vs)
	
		return ve
	


