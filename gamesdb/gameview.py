import ui
from console import hud_alert
from models.game import Game

viewname = "ui/GameView"

def button_tapped(sender):
	'@type sender: ui.Button'
	# Get the button's title for the following logic:
	t = sender.title
	
	# label = sender.superview['label1']
	if t == 'Save':
		s1 = sender.superview['textfield1']
		s2 = sender.superview['textfield2']
		s3 = sender.superview['textfield3']
		
		new_game = Game(sender.superview['label1'].text)
		new_game.genre = s1.text
		new_game.platform = s2.text
		new_game.released = s3.text
		
		hud_alert('Done.')
		new_game.print_game()
		
		sender.superview.close()
		
def main():
	g = Game("Dark Cloud 2")
	g.image = "covers/Dark Cloud 2.jpg"
	g.genre = ""
	g.platform = ""
	
	
	v = ui.load_view(viewname)
	#slider_action(v['slider1'])
	s = v['imageview1']
	v['label1'].text = g.title
	s.image = ui.Image(g.image)
	
	
	
	#v.corner_radius = 10
	#v.background_color = '#d5d5d5'
	#v.tint_color = '#d5d5d5'
	#v['tableview1'].data_source = MyList
	
	if ui.get_screen_size()[1] >= 768:
		# iPad
		v.present('sheet')
	else:
		# iPhone
		v.present('popover')
		
	
if __name__ == "__main__":
	main()

