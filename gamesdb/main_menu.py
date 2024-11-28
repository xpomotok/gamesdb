from gamesdb.utils.command import MenuItem, Menu
from gamesdb.main_gamesdb import app


class WishListItem(MenuItem):
    def execute(self):
        app.change_list(0)


class PlayingItem(MenuItem):
    def execute(self):
        app.change_list(1)


class AllGamesItem(MenuItem):
    def execute(self):
        app.change_list(2)


class FavoriteItem(MenuItem):
    def execute(self):
        app.change_list(3)


class MainMenu(Menu):
    # add button glyphs specifically for iOS

    def __init__(self):
        super().__init__()
        self.set_name("MainMenu")
        self.add_menu_item(WishListItem("Wishlist"))
        self.add_menu_item(PlayingItem("Now playing"))
        self.add_menu_item(AllGamesItem("All Games"))
        self.add_menu_item(FavoriteItem("Favorite"))

