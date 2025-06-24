from settings import *
import math
from tetromino import Tetromino

class Tetris:
    def __init__(self, app):
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.tetromino = Tetromino(self)

    def draw_grid(self):
        for x_direction in range(FIELD_W):
            for y_direction in range(FIELD_H):
                pg.draw.rect(self.app.screen, "black",
                             (x_direction * TILE_SIZE, y_direction * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    def update(self):
        self.tetromino.update()
        self.sprite_group.update()

    def draw(self):
        self.draw_grid()
        self.sprite_group.draw(self.app.screen)