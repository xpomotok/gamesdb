import ui
from ui_config import ui_config


def menu_button(left, top, width, height, pic='iob:archive_24') -> ui.Button:

	btn = ui.Button()
	btn.title = ''
	btn.tint_color = ui_config.btn_icon_color # "#929292"
	btn.autoresizing = 'WH'
	#btn.border_width = 1
	btn.frame = (left, top, width, height)

	img = ui.Image(pic)
	btn.image = img
	
	return btn
