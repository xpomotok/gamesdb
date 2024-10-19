
__version__ = '0.0.9.6'

__all__ = []

__author__ = 'Sergey Kuzmin <@gmail.com>'


import ui
import clipboard
from console import hud_alert
from game import Game
from gamelist import GameList
from bottom_menu import bottom_menu
from menu_button import menu_button
from menu_button_label import menu_button_label
from text_view import text_view


covers = "covers/"
thumbs = "thumbs/"
whishname = "db/wishlist.json"
playname = "db/playing.json"
viewname = "ui/GameListView"

WhishGames = GameList("Wishlist")
NowPlaying = GameList("Now Playing")
ActualGame : Game
ActualGame = Game("Morrowind")


v = ui.load_view(viewname)
tv = v['tableview1']

# Main navigator
nav = ui.NavigationView(v)
nav.name = "Games Database"

current_view : ui.View
current_list : GameList
current_file : str

def edit_close(sender):
	did_update = False
	
	
	global tv
	global current_row
	
	current_view.close()
	show_details(tv, current_row)
	

def tv_iterator(tableview : ui.TableView):
	""" записал здесь свойства, попробовать их потом
	"""
	# tableview.paging_enabled
	# tableview.left_button_items
	pass
	
	
def save_all(sender):
	#did_update = True
	
	#get main scroll from editing
	vs = current_view.subviews
	
	#tv : ui.TableView
	
	#tv = (vs[0].subviews)[0]
	#print(tv.data_source.items)
	
	#tv_iterator(tv)
	
	#ActualGame.title = ds.items[0][1]
	#ActualGame.genre = ds.items[1][1]
	#ActualGame.print_game()
	current_view.close()
	
	global tv
	global current_row
	tv.data_source.items[current_row] = ActualGame
	tv.reload()
	
	current_list.save(current_file)
	show_details(tv, current_row)
	
	
class MyTextFieldDelegate (object):
		
	def textfield_did_end_editing(self, textfield):
		
		key = textfield.name.lower()
		value = textfield.text
		global ActualGame
		if ActualGame.__dict__[key] != value:
			ActualGame.__dict__[key] = value
			hud_alert(key +" : " +value)
			did_update = True
			
		pass
		

class MyTextViewDelegate (object):
	
	def textview_did_end_editing(self, textview):
		global ActualGame
		value = textview.text
		if ActualGame.notes != value:
			ActualGame.notes = value
			hud_alert('Done')
			did_update = True
	

	
def tableview_cell_edit(tableview, section, row):
    data = tableview.data_source.items[row]
    cell = ui.TableViewCell()
    #cell.text_label.text = data[0]
    w = (cell.content_view.width-4)/2
    #w = (cell.content_view.width)
    h = cell.content_view.height
    
    col2 = ui.Label(frame=(24,0,w,h))
    col2.alignment = ui.ALIGN_LEFT
    col2.text = data[0]
    cell.content_view.add_subview(col2)
    
    col1 = ui.TextField(frame=(24+w, 3,w+48,h))
    col1.delegate = MyTextFieldDelegate()
    col1.name = data[0]
    col1.bordered = False
    col1.clear_button_mode = "while_editing"
    col1.text = str(data[1])
    cell.content_view.add_subview(col1)
    
    # Mark the table header
    if row%2== 0:
        col1.text_color = 'black' #'gray'
    else:
        col1.text_color = 'orange'
    return cell


def show_edit(tableview : ui.TableView, row : int) :
#def show_edit(game1 : Game) :
	
	game1 : Game
	game1 = tableview.data_source.items[row]
	global ActualGame
	ActualGame = game1
	
	data = []
	
	#for p in ve.Data.__dict__.items():
		#print(p)
		#data.append(p)
	data.append(('Title', game1.title))
	data.append(('Genre', game1.genre))
	data.append(('Platform', game1.platform))
	data.append(('Released', game1.released))
	data.append(('Rating', str(game1.rating)))
	data.append(('Interest', str(game1.interest)))
	
	if game1.finished:
		data.append(('Finished', 'Yes'))
	else:
		data.append(('Finished', 'Not yet'))
		
	data.append(('Cover', game1.image))
	
	# print(data)

	ve = ui.View(frame=(0,0,420,768))
	ve.background_color = 'white'
	ve.name = "Edit Game"
	
	vs = ui.ScrollView(frame=(0,0,420,768))
	#vs = ui.ScrollView(frame=(0,0,420, 1080))
	vs.content_size = 400, 1080

	vs.scroll_enabled=True
	vs.background_color="#ffffff"
	
	rbtn1= ui.ButtonItem(title='Done')
	rbtn1.action = save_all
	lbtn2 = ui.ButtonItem(title='Cancel')
	lbtn2.action = edit_close
	
	tv1 = ui.TableView()
	
	#!!!
	tv1.scroll_enabled = False
	tv1.data_source = ui.ListDataSource(items=data)
	tv1.data_source.tableview_cell_for_row = tableview_cell_edit
	
	
	#tv.frame = (0,40,400, 320)
	tv1.frame = (0,40,400, 380)
	
	tv1.name = 'Editor table'
	vs.add_subview(tv1)
	#ve.add_subview(tv)
	
	b = text_view('Details', 0,0)
	vs.add_subview(b)
	#ve.add_subview(b)
	
	c = text_view('Notes', 0,40+360-5)
	vs.add_subview(c)

	d = ui.TextView(frame=(2, 445,400,360))
	d.background_color = "white"
	d.font = ("<System>",12)
	d.text = game1.notes
	d.delegate = MyTextViewDelegate()
	vs.add_subview(d)
	
	ve.right_button_items = rbtn1, 
	ve.left_button_items = lbtn2,
	
	ve.add_subview(vs)

	global current_view
	current_view = ve
	ve.present('sheet', hide_close_button=True)
	#ve.wait_modal()
	#print('Modaled window')
	
	#tableview.data_source.items[row] = ActualGame
	#tableview.reload()
	nav.pop_view()
	
	
def btn_edit_clicked(sender):
	#ActualGame.print_game()
	global tv
	global current_row
	show_edit(tv,  current_row)


def show_details(tableview, row):
#def show_details(game1 : Game):
	vu = ui.load_view("ui/details")
	
	global current_row
	current_row = row
	game1 = tableview.data_source.items[row]
	global ActualGame
	ActualGame = game1
	
	if game1:
		if game1.image != "":
			img = ui.Image(covers+game1.image)
		else:
			img = ui.Image(covers+"unknown_game.png")
			
		imv = vu['imageview1']
		w, h = img.size
		if h > w:
			imv.width = 96
			imv.height = 128
		if h < w:
			imv.width = 128
			imv.height = 96
		else:
			imv.width = 128
			imv.height = 128
			
		imv.image = img
		
		btn_edit = vu['btn_edit']
		btn_edit.action = btn_edit_clicked
		
		vu['labelTitle'].text = game1.title
		
		
		if game1.finished:
			vu['labelFinished'].text = "Finished"
		else:
			vu['labelFinished'].text = "Not yet"
			
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


def button_tapped(sender):
	'@type sender: ui.Button'
	sender.superview.close()
	pass


### Функции для работы с основным списком игр
def tableview_did_select( tableview, section, row):
		# Called when a row was selected.
	global ActualGame
	ActualGame = tableview.data_source.items[row]
	
	show_details(tableview, row)
	#show_details(ActualGame)
	

def tableview_cell_for_row(tableview, section, row):
		# Create and return a cell for the given section/row
	# print("test")
	#global ActualGame
	
	data = tableview.data_source.items[row]
	#ActualGame = data
	
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
			
			
def view_playing(sender):
	global current_list
	current_list = NowPlaying
	global current_file
	current_file = playname
	
	v.name = NowPlaying.title
	
	tv = v['tableview1']
	tds = ui.ListDataSource(items=NowPlaying.games)
	tv.data_source = tds
	tv.data_source.tableview_cell_for_row = tableview_cell_for_row
	
	tv.reload()
	#hud_alert('Button!')
	

def view_whishlist(sender):
	global current_list
	current_list = WhishGames
	global current_file
	current_file = whishname
	
	v.name = WhishGames.title
	
	tv = v['tableview1']
	tds = ui.ListDataSource(items=WhishGames.games)
	tv.data_source = tds
	tv.data_source.tableview_cell_for_row = tableview_cell_for_row
	
	tv.reload()
	#hud_alert('Button!')	

#!TODO фабрика списков - возвращает нужный
	
def main():
	
	WhishGames.load(whishname)
	NowPlaying.load(playname)
	
	global current_list
	current_list = WhishGames
	global current_file
	current_file = whishname
	
	v.name = current_list.title
	# tv = v['tableview1']
	# tv.delegate = MyTableViewDelegate()
	tv.delegate.tableview_did_select = tableview_did_select
	
	tds = ui.ListDataSource(items=current_list.games)
	tv.data_source = tds
	tv.data_source.tableview_cell_for_row = tableview_cell_for_row
	
	tv.reload()

	tv.editable = True

	ff = bottom_menu(0, 572, 420, 56)
	btn1 = menu_button(28, 0, 48, 48, 'iob:game_controller_b_32')
	
	btn1_label = menu_button_label(32, 35, 48,16, 'Playing')
	btn1.action = view_playing
	
	ff.add_subview(btn1)
	ff.add_subview(btn1_label)
	
	btn2 = menu_button(130, 0, 48, 48,'iob:ios7_star_32')
	btn2_label = menu_button_label(134, 35, 48,16, 'Favorite')
	btn2.action = view_whishlist
	ff.add_subview(btn2)
	ff.add_subview(btn2_label)
	
	btn3 = menu_button(230, 0, 48, 48,'iob:ios7_box_outline_32')
	btn3_label = menu_button_label(234, 35, 48,16, 'Games')
	#btn3.action = helloer
	ff.add_subview(btn3)
	ff.add_subview(btn3_label)
	
	btn4 = menu_button(324, 0, 48, 48,'iob:ios7_cog_outline_32')
	btn4_label = menu_button_label(328, 35, 48,16, 'Setting')
	#btn4.action = helloer
	ff.add_subview(btn4)
	ff.add_subview(btn4_label)
	
	v.add_subview(ff)
	#nav = ui.NavigationView(v)
	nav.present(style='fullscreen', hide_title_bar=False, hide_close_button=False)


	
if __name__ == "__main__":
	main()
