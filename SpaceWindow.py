import arcade
from SpaceHelpers import WINDOW_WIDTH
from SpaceHelpers import WINDOW_HEIGHT
class SpaceWidnow(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, "Space This Time")
        self.player = None
        self.rocks = None

    def setup(self):
        self.player = arcade.Sprite("Blue-05.png")
        self.player.center_x = 100
        self.player.center_y = WINDOW_HEIGHT/2

    def on_update(self, delta_time: float):
        pass
    def on_draw(self):
        arcade.start_render()