
import pygame as pg
from pygame.constants import *


#GAMESETTINGS

WIDTH = 1600
HEIGHT = 900
aspect_ratio = (WIDTH, HEIGHT)
FPS = 60

#COLORGAMUT

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50 , 50)
GREEN = (0, 255, 0)
BLUE = (50, 50 , 255)

class Game:
    def __init__(self):
        #INITIALIZATION
        pg.init()
        pg.font.init()
        self.font1 = pg.font.SysFont('Comic Sans MS', 100)
        self.font2 = pg.font.SysFont('Comic Sans MS', 50)
        self.title = self.font1.render('SNAKE 2P', False, BLUE, RED)
        self.press = self.font2.render('PRESS ANY KEY', False, BLACK, GREEN)
        self.textpos1 = self.title.get_rect(center=(asp_x//2, asp_y//4*1))
        self.textpos2 = self.press.get_rect(center=(asp_x//2, asp_y//4*3))
        
        pg.display.set_caption('SNAKE 2P')
        self.display = pg.display.set_mode(aspect_ratio)
        self.game_over = False
        self.clock = pg.time.Clock()

    def start_new(self):
        #NEW GAME
        self.sprites = pg.sprite.Group()

    def start_screen(self):
        intro = True
        while intro:
            self.display.fill(GREEN)
            self.display.blit(self.title, self.textpos1)
            self.display.blit(self.press, self.textpos2)
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    break
                elif event.type == KEYDOWN:
                    intro = False
                    break
            pg.display.update()
    
    def play(self):
        

        
if __name__ == "__main__":
    Game().start_screen()
    Game().play()
