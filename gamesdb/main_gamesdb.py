__version__ = '0.1.4.5'

__all__ = ["App"]

__author__ = 'Sergey Kuzmin <@gmail.com>'

from ui_config import Config
import ui
from models.game import Game
from models.gamelist import GameList
from form_main import FormMain


config = Config()


class Controller(object):

    def __init__(self) -> None:
        super().__init__()
        self.model = None
        self.view = None

    @staticmethod
    def update_view(name, model):
        if name == 'details':
            print(name)
        pass


class App(object):
    id: int

    def __init__(self):
        self.Controller = Controller()
        # instance attributes
        self.CurrentList = None
        self.CurrentGame = None
        self.CurrentFile = ""

        self.lists = []
        for k, v in config.database:
            game_list = GameList(config.database[k])
            game_list.load(config.database[k])
            self.lists.append(game_list)

        self.wish_games = GameList(config.database[1])
        self.now_playing = GameList(config.database[2])
        self.game_collection = GameList(config.database[3])
        self.fav_games = GameList(config.database[4])
        self.wish_games.load(config.data_files[1])
        self.now_playing.load(config.data_files[2])
        self.game_collection.load(config.data_files[3])
        self.fav_games.load(config.data_files[4])
        
        # self.CurrentList = self.wish_games
        # self.CurrentFile = config.wish_name
        self.change_list(0)
        self.MainWindow = FormMain(self)

    def change_list(self, index):
        self.id = 333
        self.CurrentList = self.lists[index]
        self.CurrentFile = config.data_files[index]

    def run(self):
        self.MainWindow.show()

    def save_all(self, sender):

        for i, gl in self.lists:
            gl.save(config.data_files[i])

        self.game_collection.save(config.all_name)
        self.wish_games.save(config.wish_name)
        self.now_playing.save(config.play_name)
        self.fav_games.save(config.fav_name)


def main():
    games_db = App()
    games_db.run()


if __name__ == "__main__":
    main()
