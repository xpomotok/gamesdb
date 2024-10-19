import ui

from ui_config import ui_config


def text_view(text: str, left=0, top=10) ->ui.TextView:
	''' это разделитель такой '''
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
