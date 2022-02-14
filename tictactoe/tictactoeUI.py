import arcade

class tictactoeUI:
    def __init__(self):
        #constants
        self.SCREEN_WIDTH = 600
        self.SCREEN_HEIGHT = 600
        self.SCREEN_TITLE = "Welcome to Tic Tac Toe"

    def set_up_UI(self):
        arcade.open_window(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.SCREEN_TITLE)
        arcade.set_background_color(arcade.color.WHITE)

    def run_UI(self):
        arcade.start_render()
        arcade.finish_render()
        arcade.run()

