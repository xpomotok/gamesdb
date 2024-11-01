
__version__ = '0.0.9.1'

__all__ = []

__author__ = 'Sergey Kuzmin <@gmail.com>'


import ui
from models.gamelist import GameList

covers = "covers/"
thumbs = "thumbs/"
whishname = "db/playing.json"
viewname = "ui/GameListView"

Games = GameList("Now playing")
v = ui.load_view(viewname)

nav = ui.NavigationView(v)


def show_details(row):
	vu = ui.load_view("ui/details")
	
	game1 = Games.games[row]
	
	if game1:
		if game1.image != "":
			img = ui.Image(thumbs+game1.image)
		else:
			img = ui.Image(covers+"unknown_game.png")
		
		imv = vu['imageview1']
		w, h = img.size
		if w != h:
			imv.width = 96
			imv.height = 128
		else:
			imv.width = 128
			imv.height = 128
			
		imv.image = img
		
		
		vu['labelTitle'].text = game1.title
		if game1.finished:
			vu['labelFinished'].text = "Finished"
		else:
			vu['labelFinished'].text = "Not"
		vu['labelReleased'].text = game1.released
		vu['labelPlatform'].text = game1.platform
		vu['labelGenre'].text = game1.genre
		vu['labelRating'].text = str(game1.interest)
	
		vu['textview1'].text = game1.notes
	else:
		vu['textfield1'].text = 'None'
		
		vu['textview1'].text = game1.notes
		# для работы с родным navigation
		#v.nav.push_view(vu)
		
	nav.push_view(vu)		
		

def show_info(row):
	'@type sender: ui.ListDataSource'
	#sender.add_subview(GameView2)
	
	game1 = Games.games[row]
	
	vu = ui.load_view('GameView')

	if game1:
		if game1.image != "":
			img = ui.Image(covers+game1.image)
		else:
			img = ui.Image(covers+"unknown_game.png")
			
		vu['imageview1'].image = img
		
		
		vu['label1'].text = game1.title
		vu['textfield1'].text = game1.title
		vu['textfield2'].text = game1.genre
		vu['textfield3'].text = game1.platform
		vu['textfield4'].text = game1.released
		#v['textfield5'].text = game1.notes
		vu['textfield5'].text = game1.image
	else:
		vu['textfield1'].text = 'None'
		
		vu['textview1'].text = game1.notes
		# для работы с родным navigation
		#v.nav.push_view(vu)
		
	nav.push_view(vu)
	#v.present()


def button_tapped(sender):
	'@type sender: ui.Button'
	sender.superview.close()
	pass


def tableview_did_select( tableview, section, row):
		# Called when a row was selected.
	#hud_alert('Done!')
	#show_info(row)
	show_details(row)


def tableview_cell_for_row(tableview, section, row):
		# Create and return a cell for the given section/row
	# print("test")
	data = tableview.data_source.items[row]
	
	cell = ui.TableViewCell(style='subtitle')
	cell.accessory_type = 'disclosure_indicator'
	cell.text_label.text = data.title
	cell.detail_text_label.text = data.platform
		
	if data.image != "":
		img = ui.Image(covers+data.image)
	else:
		img = ui.Image(covers+"unknown_game.png")
			
	cell.image_view.image = img
		
	return cell

			
def main():
	#v = ui.load_view('GameListView')
	Games.load(whishname)
	
	#view_init_table(v)
	tv = v['tableview1']
	# tv.delegate = MyTableViewDelegate()
	tv.delegate.tableview_did_select = tableview_did_select
	
	tds = ui.ListDataSource(items=Games.games)
	tv.data_source = tds
	tv.data_source.tableview_cell_for_row = tableview_cell_for_row
	
	tv.reload()


	tv.editable = True

	#nav = ui.NavigationView(v)
	nav.present()

#	if ui.get_screen_size()[1] >= 768:
		# iPad
		#print("Large screen")
	#v.present('sheet')
#	else:
		# iPhone
		#print("Small screen")
#		v.present('popover')
		
	
if __name__ == "__main__":
	main()
