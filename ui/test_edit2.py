import ui

def edit_factory(text: str, left=0, top=10) ->ui.TextView:
	d = ui.TextView(frame=(left, top, 420, 40))
	
	d.background_color="#e2e2e2"
	d.font= ("<System>",14)
	d.auto_content_inset = True
	d.paging_enabled = True
	d.text = text
	d.text_color = 'grey'
	d.scroll_enabled = False
	#d.border_width = 1
	d.border_color = '#c0c0c0'
	
	d.editable = False
	return d


def tableview_cell_for_row(tableview, section, row):
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
    
    col1 = ui.TextField(frame=(24+w, 3,w,h))
    col1.bordered = False
    col1.clear_button_mode = "while_editing"
    col1.text = data[1]
    cell.content_view.add_subview(col1)
    
    # Mark the table header
    if row%2== 0:
        col1.text_color = 'black' #'gray'
    else:
        col1.text_color = 'orange'
    return cell
    

lst = [('Title', 'Doom 2016'), ('Genre', 'Action'), ('Platform', 'PC'), ('Released', '2016'), ('Interest', '97'), ('Finished', 'No'), ('Image', 'Doom 2016.jpg')]

vmain= ui.View(frame=(0,0,420,768))
vmain.background_color = 'white'
vmain.name = "Edit Game"
#nav = ui.NavigationView(vmain)

v = ui.ScrollView(frame=(0,0,420,768))
v.content_size = 400, 1080
#print(v.content_size)

v.scroll_enabled=True
v.background_color="#ffffff"
btn1 = ui.ButtonItem(title='+')
btn2 = ui.ButtonItem(title='Bye!')
img = ui.Image('iob:ios7_plus_empty_32')
btn1.image = img

tv = ui.TableView()
#!!!
tv.scroll_enabled = False
tv.data_source = ui.ListDataSource(items=lst)
tv.data_source.tableview_cell_for_row = tableview_cell_for_row

tv.frame = (0,40,400, 320)
tv.name = 'Table'
v.add_subview(tv)


# for scroll testing
tv1 = ui.TableView()
#!!!
tv1.scroll_enabled = True
tv1.data_source = ui.ListDataSource(items=lst)
tv1.data_source.tableview_cell_for_row = tableview_cell_for_row

tv1.frame = (0,320+40+40,400, 340)
tv1.name = 'Table'
v.add_subview(tv1)


b = edit_factory('Details', 0,0)
v.add_subview(b)

c = edit_factory('Notes', 0,40+320-5)
v.add_subview(c)

vmain.right_button_items = btn1, 
#v.left_button_items = btn2,
#v.navigation_bar_hidden = True


ed = ui.TextField(frame=(10, 300, 420, 40))
ed.placeholder = "123"
ed.bordered = False
## v.add_subview(ed)

# Bottom menu
v1 = ui.View()
v1.name = 'v1'
v1.background_color = "#e2e2e2"
v1.frame=(0, 576, 420, 64)
v1.alpha = 0.9
v1.border_width=2
v1.border_color="#c0c0c0"


# Buttons
btn = ui.Button()
btn.title = ''
btn.tint_color="#000000"
btn.autoresizing='WH'
btn.background_color="#00ff00"
btn.frame = (180,4, 48, 48)
img = ui.Image('iob:archive_32')
btn.image = img

# Populate views
v1.add_subview(btn)
vmain.add_subview(v)
vmain.add_subview(v1)

#nav.push_view(v)
#nav.present()

# Cool !!!
#v.present('panel')
#vmain.present('sheet')
vmain.present('sheet')
