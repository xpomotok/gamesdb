import ui

class MyTextFieldDelegate (object):
		
	def textfield_did_end_editing(self, textfield):
		
		key = textfield.name.lower()
		value = textfield.text
		# global ActualGame
		# if ActualGame.__dict__[key] != value:
		# 	ActualGame.__dict__[key] = value
		# 	hud_alert(key +" : " +value)
		# 	did_update = True
			
		pass
