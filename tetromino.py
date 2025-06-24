from settings import *
import random
class Block(pg.sprite.Sprite):
    def __init__(self, tetromino, pos):
        self.tetromino = tetromino
        self.pos = vec(pos) + INIT_POS_OFFSET
        self.alive = True

        super().__init__(tetromino.tetris.sprite_group)
        self.image = pg.Surface([TILE_SIZE, TILE_SIZE])
        pg.draw.rect(self.image, 'orange',(1,1,TILE_SIZE - 2, TILE_SIZE - 2), border_radius=8)
        self.rect = self.image.get_rect()

    def is_alive(self):
        if not self.alive:
            self.kill()
        
    def rotate(self, pivot_pos):
        translated = self.pos - pivot_pos
        rotated = translated.rotate(90)
        return rotated + pivot_pos

    def set_rect_pos(self):
        self.rect.topleft = self.pos * TILE_SIZE

    def update(self):
        self.is_alive()
        self.set_rect_pos()

    def is_collide(self, pos):
        x_pos, y_pos = int(pos.x), int(pos.y)
        if 0 <= x_pos <FIELD_W and y_pos < FIELD_H and (
            y_pos < 0 or not self.tetromino.tetris.field_array[y_pos][x_pos]
        ):
            return False
        return True

class Tetromino:
    def __init__(self, tetris):
        self.landing = False
        self.tetris = tetris
        self.shape = random.choice(list(TETROMINOES.keys()))
        self.blocks = [Block(self, pos) for pos in TETROMINOES[self.shape]]
        
    def rotate(self):
        pivot_pos = self.blocks[0].pos
        new_block_positions = [block.rotate(pivot_pos) for block in self.blocks]

        if not self.is_collide(new_block_positions):
            for interval, block in enumerate(self.blocks):
                block.pos = new_block_positions[interval]

    def is_collide(self, block_positions):
        return any(map(Block.is_collide, self.blocks, block_positions))

    def move(self, direction):
        move_direction = MOVE_DIRECTIONS[direction]
        new_block_positions = [block.pos + move_direction for block in self.blocks]
        is_collide = self.is_collide(new_block_positions)

        if not is_collide:
            for block in self.blocks:
                block.pos += move_direction
        elif direction == 'down':
            self.landing = True

    def update(self):
        self.move(direction='down')
        