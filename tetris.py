from settings import *
import math
from tetromino import Tetromino

class Tetris:
    def __init__(self, app):
        self.app = app
        self.field_array = self.get_field_array()
        self.sprite_group = pg.sprite.Group()
        self.tetromino = Tetromino(self)
        self.speed_up = False
    
    def check_full_lines(self):
        row = FIELD_H - 1
        for y_pos in range(FIELD_H - 1, -1, -1):
            for x_pos in range(FIELD_W):
                self.field_array[row][x_pos] = self.field_array[y_pos][x_pos]

                if self.field_array[y_pos][x_pos]:
                    self.field_array[row][x_pos].pos = vec(x_pos,y_pos)

            if sum(map(bool, self.field_array[y_pos])) < FIELD_W:
                row -= 1
            else:
                for x_pos in range(FIELD_W):
                    self.field_array[row][x_pos].alive = False
                    self.field_array[row][x_pos] = 0

    def put_tetromino_blocks_in_array(self):
        for block in self.tetromino.blocks:
            x_pos,y_pos = int(block.pos.x), int(block.pos.y)
            self.field_array[y_pos][x_pos] = block

    def get_field_array(self):
        return[[0 for x_pos in range(FIELD_W)] for y_pos in range(FIELD_H)]

    def check_tetromino_landing(self):
        if self.tetromino.landing:
            self.speed_up = False
            self.put_tetromino_blocks_in_array()
            self.tetromino = Tetromino(self)

    def control(self, pressed_key):
        if pressed_key == pg.K_a:
            self.tetromino.move(direction='left')
        elif pressed_key == pg.K_d:
            self.tetromino.move(direction='right')
        elif pressed_key == pg.K_w:
            self.tetromino.rotate()
        elif pressed_key == pg.K_s:
            self.speed_up = True

    def draw_grid(self):
        for x_direction in range(FIELD_W):
            for y_direction in range(FIELD_H):
                pg.draw.rect(self.app.screen, "black",
                             (x_direction * TILE_SIZE, y_direction * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    def update(self):
        trigger = [self.app.anim_trigger, self.app.fast_anim_trigger][self.speed_up]
        if trigger:
            self.check_full_lines()                
            self.tetromino.update()
            self.check_tetromino_landing()
        self.sprite_group.update()

    def draw(self):
        self.draw_grid()
        self.sprite_group.draw(self.app.screen)
