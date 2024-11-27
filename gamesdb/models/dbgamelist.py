import codecs
import json
from game import Game
# Lists
# ListId Title
# 1      Whishlist
# 2      NowPlaying

# whishlist
# ListId GameId
# 1		 2
# 1      23
# 1      45

# NowPlaying
# ListId GameId
# 2		 2
# 2      23


class DbGameListItem:
    def __init__(self):
        self.id = 0
        self.game = None

    def set_game(self, id, game):
        self.id = id
        self.game = game

    def get_game(self):
        return self.game

    def __str__(self) -> str:
        return "ID: {}, GAME: {}".format(self.id, self.game.title)

    def __repr__(self) -> str:
        return "ID: {}, GAME: {}".format(self.id, self.game.title)


class DbGameList:
    def __init__(self, title):
        self.title = title
        self.auto_indexer = 0
        self.repo = []

    def add_game(self, game):
        game_item = DbGameListItem()
        index = self.auto_indexer
        game_item.set_game(index, game)
        self.auto_indexer += 1
        self.repo.append(game_item)

    def find_by_name(self, name: str):
        pass

    def get(self, id):
        return self.repo.pop(id)

    def __load_json__(self, fname):
        try:
            with codecs.open(fname, "rU", "utf-8") as fp:
                return json.load(fp)

        except OSError as E:
            print("Something '{}', actually, went wrong".format(E.strerror))
            return None

    def __load__(self, source):
        """ for initial imoprt only """
        json_map = self.__load_json__(source)

        if json_map is not None:
            version_map = json_map["version"]

            print(version_map)
            games_map = json_map["games"]

            for item in games_map:
                game = Game("")
                game.deserialize(item)
                self.add_game(game)

    def print_table(self):
        print("GAMES: {}".format(self.title))
        for gi in self.repo:
            print(gi)


games = DbGameList("All games")
games.__load__("../db/games.json")
games.print_table()