import ui
from ui_config import ui_config


def menu_button_label(left, top, width, height, text) -> ui.Label:
	btn1_label = ui.Label(frame=(left, top, width, height))
	btn1_label.font = ("<System>", 12)
	btn1_label.text_color = ui_config.btn_label_color or "#929292"
	btn1_label.text = text
	btn1_label.alignment = ui.ALIGN_CENTER
	
	return btn1_label
