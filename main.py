from settings import *
import sys

class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Tetris')
        self.screen = pg.display.set_mode(FIELD_RES)
        self.clock = pg.time.Clock()

    def update(self):
        self.clock.tick(FPS)

    def draw(self):
        self.screen.fill(color=FIELD_COLOR)
        pg.display.flip()

    def check_events(self):
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key ==pg.K_ESCAPE):
            pg.quit()
            sys.exit()

if __name__ == "__main__":
    app = App()
    app.run()