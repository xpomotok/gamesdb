import ui
from console import hud_alert
from game import Game
from gamelist import GameList


covers = "covers/"
thumbs = "thumbs/"
whishname = "db/wishlist.json"

Games = GameList("Wishlist")
viewname = "ui/listproto"
gameview = "ui/GameView"

def show_info(row):
	'@type sender: ui.ListDataSource'
	#sender.add_subview(GameView2)
	
	game1 = Games.games[row]
	
	v = ui.load_view(gameview)

	if game1:
		if game1.image != "":
			img = ui.Image(covers+game1.image)
		else:
			img = ui.Image(covers+"unknown_game.png")
			
		v['imageview1'].image = img
		
		
		v['label1'].text = game1.title
		v['textfield1'].text = game1.title
		v['textfield2'].text = game1.genre
		v['textfield3'].text = game1.platform
		v['textfield4'].text = game1.released
		#v['textfield5'].text = game1.notes
		v['textfield5'].text = game1.image
	else:
		v['textfield1'].text = 'None'
		
		v['textview1'].text = game1.notes
	v.present()


def button_tapped(sender):
	'@type sender: ui.Button'
	sender.superview.close()
	pass


def tableview_did_select( tableview, section, row):
		# Called when a row was selected.
		#hud_alert('Done!')
	show_info(row)
	

def tableview_cell_for_row(tableview, section, row):
		# Create and return a cell for the given section/row
	# print("test")
	data = tableview.data_source.items[row]
	
	cell = ui.TableViewCell(style='subtitle')
	cell.accessory_type = 'disclosure_indicator'
	cell.text_label.text = data.title
	cell.detail_text_label.text = data.platform + " , " + data.released
	
		
	if data.image != "":
		img = ui.Image(covers+data.image)
	else:
		img = ui.Image(covers+"unknown_game.png")
	
	cell.image_view.image= img
		
	return cell

			
def main():
	v = ui.load_view(viewname)
	
	Games.load(whishname)
	
	#view_init_table(v)
	tv = v['tableview1']
	tv.delegate.tableview_did_select = tableview_did_select
	
	tds = ui.ListDataSource(items=Games.games)
	tv.data_source = tds
	tv.data_source.tableview_cell_for_row = tableview_cell_for_row
	
	tv.reload()


	tv.editable = True

	v.present('sheet')
		
	
if __name__ == "__main__":
	main()
