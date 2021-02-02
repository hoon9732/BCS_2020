##SPRITES
import pygame as pg
import random
import os
from datetime import date, timedelta
from pygame.constants import *
from settings import *
from sound import *

pg.init()
display = pg.display.set_mode(aspect_ratio)
clock = pg.time.Clock()

def load_img(name):
    img = pg.image.load(os.path.abspath(name)).convert_alpha()
    return img

def ambiency(loop, iter, margin, mod):
    if loop and iter < margin:
        iter += 1
    elif loop and iter == margin:
        loop = False
    elif not loop and iter > 0:
        iter -= 1
    else:
        loop = True
    num = (iter%(margin+1))//mod
    return num, iter, loop

def sliding(loop, start, end, mod):
    if loop and start < end:
        start += mod
    elif loop and end < start:
        start -= mod
    else:
        loop = False
        pass
    return start, loop

#BACKGROUND IMAGES

logo_01 = pg.transform.scale(load_img('vfx/logo_01.png'), aspect_ratio)
logo_02 = pg.transform.scale(load_img('vfx/logo_02.png'), aspect_ratio)
main_screen = []
main_screen.append(pg.transform.scale(load_img('vfx/main_01.png'), aspect_ratio))
main_screen.append(pg.transform.scale(load_img('vfx/main_02.png'), aspect_ratio))
main_screen.append(pg.transform.scale(load_img('vfx/main_03.png'), aspect_ratio))
main_screen.append(pg.transform.scale(load_img('vfx/main_04.png'), aspect_ratio))
main_screen.append(pg.transform.scale(load_img('vfx/main_05.png'), aspect_ratio))
main_scroll = pg.transform.scale(load_img('vfx/main_00.png'), (1600, 3600))
main_title = []
main_title.append(pg.transform.scale(load_img('vfx/title_01.png'), aspect_ratio))
main_title.append(pg.transform.scale(load_img('vfx/title_02.png'), aspect_ratio))
main_start = []
main_start.append(pg.transform.scale(load_img('vfx/start_01.png'), (560, 100)))
main_start.append(pg.transform.scale(load_img('vfx/start_02.png'), (560, 100)))
main_instructions = []
main_instructions.append(pg.transform.scale(load_img('vfx/instruction_01.png'), aspect_ratio))
main_instructions.append(pg.transform.scale(load_img('vfx/instruction_02.png'), aspect_ratio))
main_instructions.append(pg.transform.scale(load_img('vfx/instruction_03.png'), aspect_ratio))
main_instructions.append(pg.transform.scale(load_img('vfx/instruction_04.png'), aspect_ratio))
countdown = []
countdown.append(pg.transform.scale(load_img('vfx/count_00.png'), aspect_ratio))
countdown.append(pg.transform.scale(load_img('vfx/count_01.png'), aspect_ratio))
countdown.append(pg.transform.scale(load_img('vfx/count_02.png'), aspect_ratio))
countdown.append(pg.transform.scale(load_img('vfx/count_03.png'), aspect_ratio))

#OBJECT IMAGES

standing = []
standing.append(load_img('vfx/standing_01.png'))
standing.append(load_img('vfx/standing_02.png'))
standing.append(load_img('vfx/standing_03.png'))
standing.append(load_img('vfx/standing_04.png'))
standing.append(load_img('vfx/standing_05.png'))

falling = []
falling.append(load_img('vfx/falling_01.png'))
falling.append(load_img('vfx/falling_02.png'))
falling.append(load_img('vfx/falling_03.png'))

damaged = load_img('vfx/damaged.png')

blocktypes = []
blocktypes.append(load_img('vfx/block_normal.png'))
blocktypes.append(load_img('vfx/block_boost.png'))
blocktypes.append(load_img('vfx/block_heal.png'))
blocktypes.append(load_img('vfx/block_mud.png'))
blocktypes.append(load_img('vfx/block_moving.png'))

masks = []
masks.append(load_img('vfx/mask_00.png'))
masks.append(load_img('vfx/mask_01.png'))
masks.append(load_img('vfx/mask_02.png'))
masks.append(load_img('vfx/mask_03.png'))

covid = pg.transform.scale(load_img('vfx/covid.png'), aspect_ratio)

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.score = 0
        self.scorecount = 0
        self.param = 1
        self.image = standing[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.collide = pg.sprite.spritecollide(self, self.game.blocks, False)
        self.standing_iter = 0
        self.double_jump = 0
        self.pos = (WIDTH//2, HEIGHT - block_height -100)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0

    def jump(self):
        sfx('sfx/jump.wav')
        self.rect.x += 1
        #collide = pg.sprite.spritecollide(self, self.game.blocks, False)
        self.rect.x -= 1
        if self.scorecount > 100:
            self.scorecount -= 100
            self.double_jump += 1
        else:
            pass
        if abs(self.vy) < 1:
            self.vy = -JUMPPOWER
        elif self.double_jump > 0:
            self.double_jump -= 1
            self.vy = -JUMPPOWER
        else:
            pass
            
    def update(self):
        #ANIMATION
        if not self.collide:
            if self.standing_iter//5 < len(standing):
                self.standing_iter += 1
            else:
                self.standing_iter =0
            self.image = standing[(self.standing_iter-1)//5]
        if self.collide:
            if self.vy < 5 and self.vy > -5:
                self.image = falling[0]
            elif self.vy < 10 and self.vy > -10:
                self.image = falling[2]
            else:
                self.image = falling[1]
        
        #KEYBIND
        keys = pg.key.get_pressed()
        self.ax = 0
        self.ay = GRAVITY
        
        if keys[K_a]:
            if self.collide:
                self.ax = -player_acc * AIR_RESISTANCE
            else:
                self.ax = -player_acc
        elif keys[K_d]:
            if self.collide:
                self.ax = player_acc * AIR_RESISTANCE
            else:
                self.ax = player_acc
        else:
            pass
        
        self.f = FRICTION

        self.vx -= self.vx * self.f
        self.vx += self.ax
        self.vy += self.ay

        if not self.collide:
            if self.vy > 8:
                self.image = falling[2]
            elif self.vy > 4:
                self.image = falling[1]
            elif self.vy > 2:
                self.image = falling[0]

        if keys[K_LSHIFT]:
            maxspeed = player_maxspeed*2
            self.vx *= 2
        else:
            maxspeed = player_maxspeed

        if self.vx > maxspeed:
            self.vx = maxspeed
        elif self.vx < -maxspeed:
            self.vx = -maxspeed

        if self.x > WIDTH:
            self.x = WIDTH
            self.vx = -self.vx * ELASTICITY
        elif self.x < 0:
            self.x = 0
            self.vx = -self.vx * ELASTICITY

        self.x += self.vx + 0.5*self.ax
        self.y += self.vy + 0.5*self.ay

        self.pos = (self.x, self.y)
        self.rect.midbottom = self.pos
    
class Block(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.typenum = random.randrange(0, 1000)
        self.resource = 0
        if self.typenum % boost_mod == 0:
            self.type = 1
        elif self.typenum % heal_mod == 0:
            self.type = 2
            self.resource = 1
        elif self.typenum % mud_mod == 0:
            self.type = 3
        elif self.typenum % moving_mod == 0:
            self.type = 4
        else:
            self.type = 0
        self.w = random.randrange(200, 300)
        self.h = 20
        self.image = pg.transform.scale(blocktypes[self.type], (self.w, self.h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        if self.rect.x > WIDTH//2:
            self.locomotion = -locomotion_speed
        elif self.rect.x <= WIDTH//2:
            self.locomotion = locomotion_speed

class Background(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = main_scroll
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = -2880     
        self.date_origin = date(2020, 1, 1)
    def calendar(self):
        self.date = self.date_origin + timedelta(days=(2880+self.rect.y)//8)
        return self.date.strftime('%Y/%m/%d')

class Mask(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.life = 3
        if self.life >= 0:
            self.image = masks[self.life]
        else:
            self.image = masks[0]
        self.rect = self.image.get_rect()
        self.x = WIDTH - 100
        self.y = 105
        self.pos = (self.x, self.y)
        self.rect.topleft = self.pos

class COVID(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = covid
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = HEIGHT*3//2
        self.vy = 1

