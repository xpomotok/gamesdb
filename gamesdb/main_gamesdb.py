__version__ = '0.1.3.4'

__all__ = ["App","load_image"]

__author__ = 'Sergey Kuzmin <@gmail.com>'

from ui_config import Config
import ui
from models.game import Game
from models.gamelist import GameList
# from gui.bottom_menu import BottomMenu
# from form_edit import FormEdit
# from form_details_new import FormDetails
from form_main import FormMain

config = Config()

class Controller(object):
    @staticmethod
    def update_view(name, model):
        if name == 'details':
            print(name)
        pass

class App(object):

    def __init__(self):
        self.Controller = Controller()

        self.CurrentList: GameList
        self.CurrentGame: Game = None
        self.CurrentFile: str = ""

        wish_games = GameList(config.database[1])
        now_playing = GameList(config.database[2])
        game_collection = GameList(config.database[3])

        wish_games.load(config.data_files[1])
        now_playing.load(config.data_files[2])
        game_collection.load(config.data_files[3])

        self.MainWindow = FormMain()

    def run(self):
        self.MainWindow.show()

    def save_all(self, sender):
        game_collection.save(config.all_name)
        wish_games.save(config.wish_name)
        now_playing.save(config.play_name)


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
