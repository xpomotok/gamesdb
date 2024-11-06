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
	wish_name = "db/wishlist.json"
	play_name = "db/playing.json"
	all_name = "db/games.json"
	database = {1: "Wishlist", 2: "Now playing", 3: "Collection"}
	data_files = {1: wish_name, 2: play_name, 3: all_name}
	default_image = "unknown_game.png"
	color_main_title = 'orange'
	color_main_back = '#e7e7e7'
	main_frame = (0, 0, 390, 734)
	tv_row_height = 64 # 64
	
	
