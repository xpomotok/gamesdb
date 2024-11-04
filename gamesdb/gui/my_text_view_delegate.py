import ui


class MyTextViewDelegate (object):
	
	def textview_did_end_editing(self, textview):
		# global ActualGame
		value = textview.text
		# if ActualGame.notes != value:
			# ActualGame.notes = value
			# hud_alert('Done')
			# did_update = True
