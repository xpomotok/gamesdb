'''
	Пример для работы с табличным представлением, разбитым на секции
'''

import ui

lst =list(range(25))
# new
sections = ["Backlog", "Information", "Details"]

labels = [('Interest', 'Rating', 'Released'), ('Platform', 'Genre', 'Year', 'Finished'), ('Notes','','','')]

sec_rows = [3, 4, 4]
class MyTableViewDataSource (object):
	def tableview_number_of_sections(self, tableview):
		# Return the number of sections (defaults to 1)
		return 3

	def tableview_number_of_rows(self, tableview, section):
		# Return the number of rows in the section
		
		return sec_rows[section]

	def tableview_cell_for_row(self, tableview, section, row):
		# Create and return a cell for the given section/row
		cell = ui.TableViewCell()
		# cell.text_label.text = 'Foo Bar'
		sect_label = labels[section]
		cell.text_label.text = sect_label[row]#str(lst[row])
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
		
		
v = ui.View(frame=(0,0, 800, 800))
v.background_color = 'white'
tv = ui.TableView(frame=(0,0,400,800))

mt = MyTableViewDataSource()
tv.data_source = mt

v.add_subview(tv)
v.present()
