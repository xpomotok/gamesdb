from ui_config import Config
import ui
from models.game import Game
from models.gamelist import GameList
from gui.bottom_menu import BottomMenu
from form_edit import FormEdit
from form_details_new import FormDetails


class FormMain:
    def __init__(self, app) -> None:
        self.FormEdit = None
        self.MainWindow: ui.NavigationView
        self.app = app

    def show(self):
        # Load gui from file and insert into Main window
        self.FormListView = ui.View()
        self.FormListView = ui.load_view("gui/GameListView.pyui")
        self.Edit = ui.View()
        self.TableView = self.FormListView['tableview1']
        self.MainWindow = ui.NavigationView(self.FormListView)

        # Configure Main window appearance
        self.MainWindow.name = Config.app_name
        self.MainWindow.title_color = Config.color_main_title
        self.MainWindow.tint_color = Config.color_main_title
        self.MainWindow.background_color = Config.color_main_back
        self.MainWindow.frame = Config.main_frame
        self.TableView.row_height = Config.tv_row_height
        self.MainWindow.bg_color = Config.color_main_back

        # Set Main Window frame
        bmenu_x = self.MainWindow.bounds[0]
        bmenu_w = self.MainWindow.bounds[2]
        bmenu_y = self.MainWindow.bounds[3]
        bmenu_h = 56

        # Add new bottom menu
        ff = BottomMenu()
        ff.frame = (bmenu_x, bmenu_y - 80 - (bmenu_h), bmenu_w, bmenu_h + 56)

        # Add bottom buttons
        ff.add_button('Playing', 'iow:game_controller_b_32', self.view_playing)
        ff.add_button('Wishlist', 'iob:ios7_cart_outline_32', self.view_wishlist)
        ff.add_button('All games', 'iob:ios7_box_outline_32', self.view_collection)
        ff.add_button('Add new', 'iob:ios7_compose_outline_32', self.view_new_game)

        self.FormListView.add_subview(ff)

        right_button = ui.ButtonItem(title='Save')
        right_button.action = self.app.save_all

        self.MainWindow.right_button_items = right_button,
        self.change_current_view(self.app.CurrentList)
        
        self.MainWindow.present(style='fullscreen', hide_title_bar=False, hide_close_button=False)

    # Функции для работы с основным списком игр
    def tableview_did_select(self, tableview, section, row):
        # Called when a row is selected.
        self.app.CurrentGame = tableview.data_source.items[row]
        self.show_view(self.app.CurrentGame, FormDetails)

    def tableview_cell_for_row(self, tableview, section, row):
        # Create and return a cell for the given section/row
        # print("test")
        # global ActualGame
        data: Game
        data = tableview.data_source.items[row]
        # ActualGame = data

        cell = ui.TableViewCell(style='subtitle')
        cell.accessory_type = 'disclosure_indicator'
        cell.text_label.text = data.title
        cell.detail_text_label.text = ''.join([data.platform, ", ", data.released])

        img = load_image(data.image)

        #
        # cell.image_view.content_mode = cell.image_view.flex = 'tb'
        cell.image_view.image = img

        cell.image_view.flex = 'tb'
        cell.image_view.corner_radius = 6
        cell.image_view.flex = 'tb'
        # print(cell.image_view.flex)
        return cell

    def button_tapped(self, sender):
        '@type sender: ui.Button'
        sender.superview.close()


    def view_playing(self, sender):
        self.app.CurrentFile = Config.play_name
        self.change_current_view(self.app.now_playing)
        sender.tint_color = 'orange'

    def view_wishlist(self, sender):
        self.app.CurrentFile = Config.wish_name
        self.change_current_view(self.app.wish_games)
        sender.tint_color = 'orange'

    def view_collection(self, sender):
        self.app.CurrentFile = Config.all_name
        self.app.CurrentList = self.app.game_collection
        self.change_current_view(self.app.CurrentList)
        sender.tint_color = 'orange'

    def view_new_game(self, sender):
        # определить текущий список и добавить в него новую игру
        # self.CurrentList = GameCollection
        # self.CurrentFile = allname

        new_game = Game('New')
        self.app.CurrentList.add(new_game)
        self.app.CurrentGame = new_game
        editor = FormEdit(self.app.CurrentGame)
        self.FormEdit = editor.Form
        self.FormEdit.present('sheet', hide_close_button=True)

    def change_current_view(self, games):
        self.app.CurrentList = games
        self.app.CurrentFile = games.title
        self.FormListView.name = self.app.CurrentList.title

        tv = self.TableView
        tv.delegate.tableview_did_select = self.tableview_did_select

        tds = ui.ListDataSource(items=self.app.CurrentList.games)
        tv.data_source = tds
        tv.data_source.tableview_cell_for_row = self.tableview_cell_for_row
        tv.reload()
        tv.editable = True
        
    # for a single game
    def show_view(self, game, view):
        my_view = view(game)
        my_view.name = game.title  # toje lishnee
        vu = my_view.show()
        vu.present('sheet', hide_close_button=False)
        

def load_image(image) -> ui.Image:
    if image != "":
        return ui.Image(''.join([Config.covers_path, image]))
    else:
        return ui.Image(''.join([Config.covers_path, Config.default_image]))