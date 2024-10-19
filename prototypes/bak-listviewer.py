
__version__ = '0.0.9'

__all__ = []

__author__ = 'Sergey Kuzmin <@gmail.com>'


import ui
import clipboard
from console import hud_alert
from game import Game
from gamelist import GameList


class MyTableViewDelegate (object):
	def tableview_did_select(self, tableview, section, row):
		# Called when a row was selected.
		hud_alert('Done!')
		pass

	def tableview_did_deselect(self, tableview, section, row):
		# Called when a row was de-selected (in multiple selection mode).
		pass

	def tableview_title_for_delete_button(self, tableview, section, row):
		# Return the title for the 'swipe-to-***' button.
		return 'Delete'


class MyTableViewDataSource (object):
	
	def __init__(self, rows=3, sec=1):
		self.sections = ['Section 1', 'Section 2']
		self.items = ['1','2','3','4']
		self.sec = sec
		self.rows = rows
		pass
		 
	def tableview_number_of_sections(self, tableview):
		# Return the number of sections (defaults to 1)
		return  self.sec#1

	def tableview_number_of_rows(self, tableview, section):
		# Return the number of rows in the section
		return self.rows#0

	def tableview_cell_for_row(self, tableview, section, row):
		# Create and return a cell for the given section/row
		cell = ui.TableViewCell(style='subtitle')
		
		cell.text_label.text = self.items[row]
		cell.detail_text_label.text = 'Baz'
		return cell

	def tableview_title_for_header(self, tableview, section):
		# Return a title for the given section.
		# If this is not implemented, no section headers will be shown.
		#return 'Some Section'
		return self.sections[section]

	def tableview_can_delete(self, tableview, section, row):
		# Return True if the user should be able to delete the given row.
		return True

	def tableview_can_move(self, tableview, section, row):
		# Return True if a reordering control should be shown for the given row (in editing mode).
		return True

	def tableview_delete(self, tableview, section, row):
		# Called when the user confirms deletion of the given row.
		pass

	def tableview_move_row(self, tableview, from_section, from_row, to_section, to_row):
		# Called when the user moves a row with the reordering control (in editing mode).
		pass


covers = "covers/"
thumbs = "thumbs/"
whishname = "db/wishlist.json"

Games = GameList("Wishlist")


def button_tapped(sender):
	'@type sender: ui.Button'
	sender.superview.close()
	pass
	
def show_info(sender):
	'@type sender: ui.ListDataSource'
	#sender.add_subview(GameView2)
	
	t = sender.selected_row
	g = sender.items[t]
	print(g)
	
	v = ui.load_view('ui/GameView2')
	game1 = Games.get_by_title(g['title'])
	if game1:
		v['textfield1'].text = game1.title
		v['textfield2'].text = game1.genre
		v['textfield3'].text = game1.platform
		v['textfield4'].text = game1.released
		#v['textfield5'].text = game1.notes
		v['textfield6'].text = game1.image
	else:
		v['textfield1'].text = g['title']
	v.present()
	
def view_init_table(view):
	tv = view['tableview1']
	tv.editable = False
	tv.data_source.items.clear()
	
	indi = 'detail_button'
	#indi = 'disclosure_indicator'
	
	for g in Games.games:
		if g.image != "":
			img = ui.Image(covers+g.image)
			tv.data_source.items.append({'title':g.title,'image':img, 'accessory_type': indi})
			#lt.items.append({'title':g.title,'image':img, 'accessory_type':'detail_button'})
		else:
			img = ui.Image(covers+"unknown_game.png")
			tv.data_source.items.append({'title':g.title,'image':img, 'accessory_type':'detail_button'})
			pass
			
			
def main():
	v = ui.load_view('ui/GameListView')
	Games.load(whishname)
	
	#view_init_table(v)
	tv = v['tableview1']
	tv.delegate = MyTableViewDelegate()
	
	tds = MyTableViewDataSource()

	tv.data_source = tds
	tv.reload()

	
	#tv = v['tableview1']
	#tv.editable = False
	#tv.data_source.items.clear()

	if ui.get_screen_size()[1] >= 768:
		# iPad
		#print("Large screen")
		v.present('sheet')
	else:
		# iPhone
		#print("Small screen")
		v.present('popover')
		
	
if __name__ == "__main__":
	main()
