__author__ = 'Sergey Kuzmin <@gmail.com>'
__date__ = '31.06.2022'

import ui
from ui_config import ui_config
from menu_button import menu_button
from menu_button_label import menu_button_label


class BottomMenu(ui.View):
	''' Класс для создания нижнего меню (пока только нижнего). Через него создаются кнопочки с картинками и подписями '''
	
	def __init__(self):
# This will also be called without arguments when the view is loaded from a UI file.
# You don't have to call super. Note that this is called *before* the attributes
# defined in the UI file are set. Implement `did_load` to customize a view after
# it's been fully loaded from a UI file.
		self.buttons = list()
		self.count = 0
		
		# set space between buttons
		self.separator_w = 24
		
		# set left position for menu
		self.left = 24
		
		self.top = 2
		
		# set size for menu items
		self.button_w = 64
		self.button_h = 64
		
		self.background_color = ui_config.bottom_menu_bg_color
		# simple transparency
		self.alpha = 0.9
		self.alpha = 1
	
		self.border_width=1
		self.border_color="#c0c0c0"
		
		pass
		
	def add_button(self, name, pic, action):
		button_w = self.button_w
		button_h = self.button_h
		
		x = self.bounds[0]
		y = self.bounds[1]
		
		position_x = (x + self.left) + (button_w + self.separator_w) * self.count
		position_y = self.top
		
		b = menu_button(position_x, position_y, button_w, button_h, pic)
		
		b.action = action
		
		self.buttons.append(b)
		self.add_subview(self.buttons[self.count])
		self.count += 1
		
		if name != '':
			label = menu_button_label(position_x, button_h - 16, 64, 16, name)
			self.add_subview(label)
		else:
			pass
			
			
