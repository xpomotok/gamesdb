import ui

def edit_factory(text: str, left=0, top=10) ->ui.TextView:
	d = ui.TextView(frame=(left, top, 420, 40))
	
	d.background_color="#e2e2e2"
	d.font= ("<System>",17)
	d.auto_content_inset = True
	d.paging_enabled = True
	d.text = text
	d.scroll_enabled = False
	d.border_width = 1
	d.border_color = '#c0c0c0'
	
	return d


# v = ui.load_view('test_edit')
v = ui.ScrollView(frame=(0,0,420,1080))
v.scroll_enabled=True
v.background_color="#ffffff"
btn1 = ui.ButtonItem(title='+')
btn2 = ui.ButtonItem(title='Bye!')
img = ui.Image('iob:plus_32')
btn1.image = img

#img = v['imageview1']
#img.frame=(69, 92, 69+32, 92+32)
#print(img.__dict__)

b = edit_factory('Double')
v.add_subview(b)

c = edit_factory('Triple', 0,60)
v.add_subview(c)

v.right_button_items = btn1, 
#v.left_button_items = btn2,
#v.navigation_bar_hidden = True


ed = ui.TextField(frame=(10, 300, 420, 40))
ed.placeholder = "123"
ed.bordered = False
v.add_subview(ed)

# Bottom menu
v1 = ui.View()
v1.name = 'v1'
v1.background_color = "#e2e2e2"
v1.frame=(0, 610, 420, 64)
v1.alpha = 0.5
v1.border_width=2
v1.border_color="#c0c0c0"


# Buttons
btn = ui.Button()
btn.title = ''
btn.tint_color="#000000"
btn.autoresizing='WH'
btn.background_color="#00ff00"
btn.frame = (200,4, 48, 48)
img = ui.Image('iob:archive_32')
btn.image = img

# Populate views
v1.add_subview(btn)
v.add_subview(v1)

#d = ui.TextView(frame=(0, 380, 420, 40))
#d.background_color="#e2e2e2"
#d.font= ("<System>",17)
#d.auto_content_inset = True
#d.paging_enabled = True
#d.text = 'Double'
#d.scroll_enabled = False
#d.border_width = 1
#d.border_color = '#c0c0c0'

#w = (cell.content_view.width-4)/3
#h = cell.content_view.height
#col1 = ui.Label(frame=(4,0,w,h))
#col1.text = data[0]
#cell.content_view.add_subview(col1)
#v.add_subview(d)
v.present()
