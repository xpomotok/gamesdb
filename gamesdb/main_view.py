from ui_config import Config
import ui
from models.game import Game
from models.gamelist import GameList
from gui.bottom_menu import BottomMenu
from form_edit import FormEdit
from form_details_new import FormDetails


class MainView:

    def __init__(self, app) -> None:
        self.FormEdit = None
        self.MainWindow: ui.NavigationView
        self.app = app
        self.FormListView = ui.View()

    def create(self) -> ui.View:
        # Load gui from file and insert into Main window
        self.FormListView = ui.load_view("gui/GameListView.pyui")
        self.Edit = ui.View()
        self.TableView = self.FormListView['tableview1']
        self.MainWindow = ui.NavigationView(self.FormListView)
        self.FormListView.navigation_bar_hidden = True

        # Configure Main window appearance
        self.MainWindow.name = Config.app_name
        self.MainWindow.title_color = Config.color_main_title
        self.MainWindow.tint_color = Config.color_main_title
        self.MainWindow.background_color = Config.color_main_back
        self.MainWindow.frame = Config.main_frame
        self.TableView.row_height = Config.tv_row_height
        self.MainWindow.bg_color = Config.color_main_back

        right_button = ui.ButtonItem(title='Save')
        right_button.action = self.app.save_all

        add_button = ui.ButtonItem(title='Add')
        add_button.action = self.view_new_game

        self.MainWindow.right_button_items = add_button, right_button,
        self.change_current_view(self.app.CurrentList)

        tv = self.TableView
        tv.delegate.tableview_did_select = self.tableview_did_select
        tv.delegate.tableview_delete = self.tableview_delete

    def get_gui(self):
        return self.MainWindow

    def show(self):
        self.MainWindow.present(style='fullscreen',
                                hide_title_bar=False,
                                hide_close_button=False)

    def add_menu(self, menu):
        # Set Main Window frame
        menu_x = self.MainWindow.bounds[0]
        menu_w = self.MainWindow.bounds[2]
        menu_y = self.MainWindow.bounds[3]
        menu_h = 56

        # Add new bottom menu
        ff = BottomMenu()
        ff.frame = (menu_x, menu_y - 80 - (menu_h), menu_w, menu_h + 56)

        # Add bottom buttons
        ff.add_button(menu.get_caption(0), 'iow:game_controller_b_32',
                      menu.menu_item(0))
        ff.add_button(menu.get_caption(1), 'iob:ios7_heart_outline_32',
                      menu.menu_item(1))
        ff.add_button(menu.get_caption(2), 'iob:ios7_cart_outline_32',
                      menu.menu_item(2))
        ff.add_button(menu.get_caption(3), 'iob:ios7_box_outline_32',
                      menu.menu_item(3))

        self.FormListView.add_subview(ff)


    # Функции для работы с основным списком игр
    def tableview_did_select(self, tableview, section, row):
        # Called when a row is selected.
        self.app.CurrentGame = tableview.data_source.items[row]
        self.show_view(self.app.CurrentGame, FormDetails)

    def tableview_delete(self, tableview, section, row):
        # Called when the user confirms deletion of the given row.
        self.app.CurrentGame = tableview.data_source.items[row]
        print(self.app.CurrentGame)

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
        cell.detail_text_label.text = ''.join(
            [data.platform, ", ", data.released])

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
        self.FormListView.name = 'Heeellloooo'
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

    def view_favorite(self, sender):
        self.app.CurrentFile = Config.fav_name
        self.app.CurrentList = self.app.fav_games
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

        self.FormEdit.background_color = Config.color_main_back
        self.FormEdit.present('sheet', hide_close_button=True)

    def change_current_view(self, games):
        self.app.CurrentList = games
        self.app.CurrentFile = games.title
        self.MainWindow.name = self.app.CurrentList.title

        tv = self.TableView

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

