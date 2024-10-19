# 16.06.2022 - Initial import


__author__ = "Sergey Kuzmin"


import ui
from ui_config import ui_config
from my_text_field_delegate import MyTextFieldDelegate

sections = ["Backlog", "Information"]
labels = [('Title','Interest', 'Rating', 'Finished'), ('Platform', 'Genre', 'Released', 'Cover')]
sec_rows = [4, 4]


class MyTableEditDataSource (object):
	
	# здесь должен быть какой-то контейнер, с помощью которого сохранятся результаты ввода изменений
	def __init__(self):
		self.input_provider = list()
		
	def tableview_number_of_sections(self, tableview):
		# Return the number of sections (defaults to 1)
		return 2

	def tableview_number_of_rows(self, tableview, section):
		# Return the number of rows in the section
		
		return sec_rows[section]

	def tableview_cell_for_row(self, tableview, section, row):
		# Create and return a cell for the given section/row
		cell = ui.TableViewCell()
		# cell.text_label.text = 'Foo Bar'
		sect_label = labels[section]
		# cell.text_label.text = sect_label[row]#str(lst[row])
		
		data = tableview.data_source.items[section]
		
		w = (cell.content_view.width-4)/2
		#w = (cell.content_view.width)
		h = cell.content_view.height
	
		col2 = ui.Label(frame=(24, 0, w-8, h))
		col2.alignment = ui.ALIGN_LEFT
		col2.text = sect_label[row]
		cell.content_view.add_subview(col2)
	
		
		col1 = ui.TextField(frame=(w-24, 3,w+32,h -8))
		self.input_provider.append(col1)
		
		col1.delegate = MyTextFieldDelegate()
		col1.name = sect_label[row]
		col1.bordered = False
		col1.clear_button_mode = "while_editing"
		col1.text = str(data[row])
		cell.content_view.add_subview(col1)	
		
		# Mark the table header
		if row%2== 0:
			col1.text_color = ui_config.edit_table_col1_color
		else:
			col1.text_color = ui_config.edit_table_col2_color

		return cell

	def tableview_title_for_header(self, tableview, section):
		# Return a title for the given section.
		# If this is not implemented, no section headers will be shown.
		### return 'Section ' + str(section)
		return sections[section]

	def tableview_can_delete(self, tableview, section, row):
		# Return True if the user should be able to delete the given row.
		return True

	def tableview_can_move(self, tableview, section, row):
		# Return True if a reordering control should be shown for the given row (in editing mode).
		return True

	def tableview_delete(self, tableview, section, row):
		# Called when the user confirms deletion of the given row.
		pass

	def tableview_move_row(self, tableview, from_section, from_row, to_section, to_row):
		# Called when the user moves a row with the reordering control (in editing mode).
		pass
