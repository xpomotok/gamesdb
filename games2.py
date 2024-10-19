#import console


from game import Game
from gamelist import GameList

def test_case_equality():
	g = Game("g")
	d = Game("g")
	
	print(g == d) # False
	# print(dir(g))
	
def test_case_new_list():
	Emu = GameList("PS2 on emu")
	em = Game("Dragon Quest VIII: Journey of the cursed king")
	em.interest = 90
	em.finished = False
	em.genre = "RPG"
	em.platform = "PS2"
	Emu.add(em)
	# Emu.save("ps2classics.json")
	print(type(PsGames))


if __name__ == "__main__":
	# console.clear()
	
	PsGames = GameList("PS 2 classic games")
	PsGames.load("db/games.json")
		
	PsGames.inc_cursor()
	PsGames.move_up()
	
	#PsGames.dec_cursor()
	PsGames.move_up()
	#g = PsGames.get()
	#g.print_game()
	#PsGames.remove()
	PsGames.print_list()
	
	PsGames.save("games3.json")
