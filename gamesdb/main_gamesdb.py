__version__ = '0.1.6.0'

__all__ = ["app"]

__author__ = 'Sergey Kuzmin <@gmail.com>'

from ui_config import Config
from models.game import Game
from models.gamelist import GameList
from form import MainForm


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
        for k, v in config.database.items():
            game_list = GameList(Config.database[k])
            game_list.load(Config.data_files[k])
            self.lists.append(game_list)

        self.wish_games = GameList(config.database[0])
        self.now_playing = GameList(config.database[1])
        self.game_collection = GameList(config.database[2])
        self.fav_games = GameList(config.database[3])
        self.wish_games.load(config.data_files[0])
        self.now_playing.load(config.data_files[1])
        self.game_collection.load(config.data_files[2])
        self.fav_games.load(config.data_files[3])
        
        # self.CurrentList = self.wish_games
        # self.CurrentFile = config.wish_name

        self.MainForm = MainForm()
        self.change_list(0)

    def change_list(self, index):
        self.id = 333
        self.CurrentList = self.lists[index]
        self.CurrentFile = config.data_files[index]

        self.controller.model = self.CurrentList
        self.controller.update_view(app.controller.model)


    def run(self):
        # Uncomment for real app
        # self.MainWindow = form_main.FormMain(self)
        # self.MainWindow.show()
        pass

    def save_all(self, sender):

        for i, gl in self.lists:
            gl.save(config.data_files[i])

        self.game_collection.save(config.all_name)
        self.wish_games.save(config.wish_name)
        self.now_playing.save(config.play_name)
        self.fav_games.save(config.fav_name)


app = App()
app.run()
# def main():
#     games_db = App()
#     games_db.run()
#
#
# if __name__ == "__main__":
#     main()
