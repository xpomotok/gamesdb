__version__ = '0.1.4.4'

__all__ = ["App"]

__author__ = 'Sergey Kuzmin <@gmail.com>'

from ui_config import Config
import ui
from models.game import Game
from models.gamelist import GameList
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

        self.wish_games = GameList(config.database[1])
        self.now_playing = GameList(config.database[2])
        self.game_collection = GameList(config.database[3])
        self.fav_games = GameList(config.database[4])
        self.wish_games.load(config.data_files[1])
        self.now_playing.load(config.data_files[2])
        self.game_collection.load(config.data_files[3])
        self.fav_games.load(config.data_files[4])
        
        self.CurrentList = self.wish_games
        self.CurrentFile = config.wish_name
        self.MainWindow = FormMain(self)

    def run(self):
        self.MainWindow.show()

    def save_all(self, sender):
        self.game_collection.save(config.all_name)
        self.wish_games.save(config.wish_name)
        self.now_playing.save(config.play_name)
        self.fav_games.save(config.fav_name)


def main():
    games_db = App()
    games_db.run()


if __name__ == "__main__":
    main()
