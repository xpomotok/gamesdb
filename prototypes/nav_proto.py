'''
	Пример работы с NavigationView
'''

__version__ = '1.0.0'

__author__ = '<sergey.a.kuzmin@gmail.com'

import ui
from console import hud_alert

if __name__ == "__main__":
	v = ui.View()
	v.background_color = 'white'
	nav = ui.NavigationView(v)
	nav.present()
	
	v1 = ui.View()
	v1.background_color = 'green'
	v1.name = 'View 1'
	nav.push_view(v1)
	
	v2 = ui.load_view('GameListView')
	v2.background_color = '#efefef'
	v2.name = 'View 2'
	nav.push_view(v2)
