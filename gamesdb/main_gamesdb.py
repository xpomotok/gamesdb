__version__ = '0.1.3.4'

__all__ = ["App","load_image"]

__author__ = 'Sergey Kuzmin <@gmail.com>'

from ui_config import Config
import ui
from models.game import Game
from models.gamelist import GameList
from gui.bottom_menu import BottomMenu
#from form_details import FormDetails
from form_edit import FormEdit
from form_details_new import FormDetails

config = Config()

WishGames = GameList(config.database[1])
NowPlaying = GameList(config.database[2])
GameCollection = GameList(config.database[3])


class Controller(object):
    @staticmethod
    def update_view(name, model):
        if name == 'details':
            print(name)
        pass


def show_view(game, view):
    my_view = view(game)
    my_view.name = game.title # toje lishnee
    vu = my_view.show()
    vu.present('sheet', hide_close_button=False)


class App(object):

    def __init__(self):
        self.MainWindow = None
        self.TableView = None
        self.Edit = None
        self.FormListView = None
        # self.CurrentFile = None
        self.CurrentList = None
        self.Controller = Controller()

        self.MainWindow: ui.NavigationView

        self.FormEdit: ui.View = None
        self.FormDetails: ui.View = None
        self.FormListView: ui.View = None
        self.CurrentView: ui.View = None

        self.CurrentList: GameList
        self.CurrentGame: Game = None
        self.CurrentRow: int = 0
        self.CurrentFile: str = ""

        WishGames.load(config.data_files[1])
        NowPlaying.load(config.data_files[2])
        GameCollection.load(config.data_files[3])

        self.create_main_view()

        self.change_current_view(WishGames)

    def change_current_view(self, games):
        self.CurrentList = games
        self.CurrentFile = games.title
        self.FormListView.name = self.CurrentList.title

        tv = self.TableView
        tv.delegate.tableview_did_select = self.tableview_did_select

        tds = ui.ListDataSource(items=self.CurrentList.games)
        tv.data_source = tds
        tv.data_source.tableview_cell_for_row = self.tableview_cell_for_row
        tv.reload()
        tv.editable = True

    def create_main_view(self):
        self.FormListView = ui.View()
        self.FormListView = ui.load_view("gui/GameListView.pyui")
        self.Edit = ui.View()
        self.TableView = self.FormListView['tableview1']
        self.MainWindow = ui.NavigationView(self.FormListView)
        self.MainWindow.name = config.app_name
        self.MainWindow.title_color = config.color_main_title
        self.MainWindow.tint_color = config.color_main_title
        self.MainWindow.background_color = config.color_main_back
        self.MainWindow.frame = config.main_frame
        self.TableView.row_height = config.tv_row_height


        bmenu_x = self.MainWindow.bounds[0]
        bmenu_w = self.MainWindow.bounds[2]
        bmenu_y = self.MainWindow.bounds[3]

        bmenu_h = 56
        ff = BottomMenu()
        ff.frame = (bmenu_x, bmenu_y - 80 - (bmenu_h), bmenu_w, bmenu_h + 56)

        ff.add_button('Playing', 'iow:game_controller_b_32', self.view_playing)
        ff.add_button('Whishlist', 'iob:ios7_cart_outline_32', self.view_wishlist)
        ff.add_button('All games', 'iob:ios7_box_outline_32', self.view_collection)
        ff.add_button('Add new', 'iob:ios7_compose_outline_32', self.view_new_game)

        self.FormListView.add_subview(ff)

        rbtn1 = ui.ButtonItem(title='Save')
        # rbtn1= ui.ButtonItem(title='', image='iob:ios7_copy_outline_24')
        rbtn1.action = self.save_all

        self.MainWindow.right_button_items = rbtn1,
        
        self.MainWindow.bg_color = config.color_main_back
       # self.MainWindow.tint_color = 'grey'
        self.MainWindow.present(style='fullscreen', hide_title_bar=False, hide_close_button=False)

    def run(self):
        # tv = self.TableView
        # tv.delegate.tableview_did_select = self.tableview_did_select
        #
        # tds = ui.ListDataSource(items=self.CurrentList.games)
        # tv.data_source = tds
        # tv.data_source.tableview_cell_for_row = self.tableview_cell_for_row
        # tv.reload()
        # tv.editable = True
        pass

    # Функции для работы с основным списком игр
    def tableview_did_select(self, tableview, section, row):
        # Called when a row is selected.
        self.CurrentGame = tableview.data_source.items[row]
        show_view(self.CurrentGame, FormDetails)


    # self.Controller.update_view('details', model)

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
        #cell.image_view.content_mode = cell.image_view.flex = 'tb'
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
        self.CurrentFile = config.play_name
        self.change_current_view(NowPlaying)
        #sender.tint_color = 'orange'

    def view_wishlist(self, sender):
        self.CurrentFile = config.wish_name
        self.change_current_view(WishGames)
        #sender.tint_color = 'orange'

    def view_collection(self, sender):
        self.CurrentFile = config.all_name
        self.change_current_view(GameCollection)
        #sender.tint_color = 'orange'

    def view_new_game(self, sender):
        # определить текущий список и добавить в него новую игру
        # self.CurrentList = GameCollection
        # self.CurrentFile = allname

        new_game = Game('New')
        self.CurrentList.add(new_game)
        self.CurrentGame = new_game
        editor = FormEdit(self.CurrentGame)
        self.FormEdit = editor.Form
        self.FormEdit.present('sheet', hide_close_button=True)

    def save_all(self, sender):
        GameCollection.save(config.all_name)
        WishGames.save(config.wish_name)
        NowPlaying.save(config.play_name)


def load_image(image) -> ui.Image:
    if image != "":
        return ui.Image(''.join([config.covers_path, image]))
    else:
        return ui.Image(''.join([config.covers_path, config.default_image]))


def main():
    games_db = App()
    games_db.run()


if __name__ == "__main__":
    main()
