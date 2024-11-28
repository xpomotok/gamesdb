from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class MenuItem(Command):

    def __init__(self, caption):
        self.__caption__ = caption

    def execute(self):
        pass

    def get_caption(self) -> str:
        return self.__caption__


class Menu:

    def __init__(self):
        self.__name__ = ""
        self.__items__ = []

    def add_menu_item(self, menu_item):
        self.__items__.append(menu_item)

    def set_name(self, name: str):
        self.__name__ = name

    def get_name(self) -> str:
        return self.__name__

    def get_caption(self, index):
        return self.__items__[index].get_caption()

    def menu_item(self, index):
        self.__items__[index].execute()
