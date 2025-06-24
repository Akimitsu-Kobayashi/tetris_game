from settings import *
import math

class Tetris:
    def __init__(self, app):
        self.app = app

    def draw_grid(self):
        for x_direction in range(FIELD_W):
            for y_direction in range(FIELD_H):
                pg.draw.rect(self.app.screen, "black",
                             (x_direction * TILE_SIZE, y_direction * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    def update(self):
        pass

    def draw(self):
        self.draw_grid()