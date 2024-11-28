from abc import ABC, abstractmethod
from gamesdb.main_gamesdb import app
# from gamesdb.main_view import MainView
from gamesdb.main_menu import MainMenu


class Form(ABC):

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def get_view(self):
        pass

    @abstractmethod
    def show(self):
        pass


class MainForm(Form):

    def create(self):
        # self.view = MainView(app)
        self.view.create()
        self.view.add_menu(self.menu)

    def get_view(self):
        return self.view

    def show(self):
        self.view.show()

    def __init__(self) -> None:
        super().__init__()
        self.menu = MainMenu()
        self.view = None

    def add_menu(self, menu):
        self.menu = menu
