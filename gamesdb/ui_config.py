__all__ = ["Config"]

class ui_config():
# Main app	
	#btn_label_color = "#929292"
	btn_icon_color = "black"
	btn_label_color = btn_icon_color
	bottom_menu_bg_color = "#e2e2e2"
	covers_path = "../assets/covers/"
	thumbs_path = "../assets/thumbs"

# Form Edit
	form_color = 'white'
	edit_table_col1_color = 'black'
	edit_table_col2_color = 'orange'
	edit_textview_color = 'white'
	edit_textview_font_face = '<System>'
	edit_textview_font_size = 12


class Config:
	app_name = "GamesDB"
	covers_path = "../assets/covers/"
	thumbs_path = "../assets/thumbs/"
	db_path = "../assets/db"
	default_image = "unknown_game.png"
	color_main_title = 'orange'
	color_main_back = '#e7e7e7'
	main_frame = (0, 0, 390, 734)
	tv_row_height = 64  # 64
	
	database = {1: "Wishlist", 2: "Now playing", 3: "Collection", 4: "Favorite"}
	data_files = {1: "db/wishlist.json",
				  2: "db/playing.json",
				  3: "db/games.json",
				  4: "db/favorite.json"}

