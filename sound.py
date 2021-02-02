import pygame as pg
from pygame.constants import *
from settings import *

pg.init()
display = pg.display.set_mode(aspect_ratio)
clock = pg.time.Clock()

def bgm(name):
    pg.mixer.init()
    pg.mixer.music.load(name)
    pg.mixer.music.play(loops=-1)

def sfx(name):
    pg.mixer.init()
    sound=pg.mixer.Sound(name)
    sound.play()
