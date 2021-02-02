
import pygame as pg
import sys
import random
from pygame.constants import *
from math import exp
from settings import *
from sprites import *
from sound import *

def terminate():
    pg.quit()
    sys.exit()

class Game:
    def __init__(self):
        #INITIALIZATION
        pg.init()
        pg.font.init()
        self.display = pg.display.set_mode(aspect_ratio)
        pg.display.set_caption(GAMENAME)
        self.clock = pg.time.Clock()
        self.font_name = pg.font.match_font('Arial')

    def logo_screen(self):
        #LOGO SCREEN
        logo = True
        fade = True
        transp=0
        transp2=0
        transp_d=25
        while logo:
            for event in pg.event.get():
                if event.type == QUIT:
                    terminate()
                    break
                elif event.type == KEYDOWN:
                    logo = False
                    break
                elif transp < 0:
                    logo = False
                    break
            if fade:
                if transp <= 255:
                    transp += transp_d
                elif transp > 255 and transp2 <= 255:
                    transp2 += transp_d
                else:
                    fade = False
            else:
                transp -= transp_d
                transp2 -= transp_d
            self.display.fill(BLACK)
            logo_01.set_alpha(transp)
            logo_02.set_alpha(transp2)
            self.display.blit(logo_01, origin)
            self.display.blit(logo_02, origin)
            pg.display.flip()
            pg.time.delay(120)

    def start_screen(self):
        bgm('sfx/gameover.wav')
        #START SCREEN
        intro = True
        title_iter = 0
        title_loop = True
        title_loop2 = True
        title_pos1 = HEIGHT*4//3
        title_pos2 = 0
        title_mod = HEIGHT//48
        cloud_iter = 0
        cloud_loop = True
        while intro:
            self.display.fill(BLACK)
            cloud_iter = ambiency(cloud_loop, cloud_iter, 49, 10)[1]
            cloud_loop = ambiency(cloud_loop, cloud_iter, 49, 10)[2]
            cloud_num = ambiency(cloud_loop, cloud_iter, 49, 10)[0]
            self.display.blit(main_screen[cloud_num], origin)
            title_iter = ambiency(title_loop, title_iter, 19, 10)[1]
            title_loop = ambiency(title_loop, title_iter, 19, 10)[2]
            title_num = ambiency(title_loop, title_iter, 19, 10)[0]
            title_pos1 = sliding(title_loop2, title_pos1, title_pos2, title_mod)[0]
            title_loop2 = sliding(title_loop2, title_pos1, title_pos2, title_mod)[1]
            self.display.blit(main_title[title_num], (0, title_pos1))
            mouse = pg.mouse.get_pos()
            if button_w1 < mouse[0] and button_w2 > mouse[0] and button_h1 < mouse[1] and button_h2 > mouse[1]:
                onstart = True
                self.display.blit(main_start[1], button_pos)
            else:
                onstart = False
                self.display.blit(main_start[0], button_pos)
            for event in pg.event.get():
                if event.type == QUIT:
                    terminate()
                    break
                elif event.type == MOUSEBUTTONDOWN:
                    if onstart:
                        intro = False
                        break
                    else:
                        pass
            pg.display.flip()
            pg.time.delay(12)

    def instructions(self):
        #INSTRUCTIONS
        instruction = True
        scroll_loop = True
        scroll_mod = 5
        scroll_pos1 = 0
        scroll_pos2 = -5400
        instruct_loop = True
        instruct_iter = 0
        while instruction:
            self.display.fill(BLACK)
            scroll_pos1 = sliding(scroll_loop, scroll_pos1, scroll_pos2, scroll_mod)[0]
            scroll_loop = sliding(scroll_loop, scroll_pos1, scroll_pos2, scroll_mod)[1]
            self.display.blit(main_scroll, (0, scroll_pos1))
            if scroll_pos1 < 0 and scroll_pos1 >= -2400:
                instruct_num = ambiency(instruct_loop, instruct_iter, 19, 10)[0]
                instruct_iter = ambiency(instruct_loop, instruct_iter, 19, 10)[1]
                instruct_loop = ambiency(instruct_loop, instruct_iter, 19, 10)[2]
                self.display.blit(main_instructions[instruct_num], origin)
            elif scroll_pos1 < -2400 and scroll_pos1 >= -3600:
                self.display.blit(main_instructions[3], origin)
            elif scroll_pos1 < -3600 and scroll_pos1 >= -4800:
                self.display.blit(main_instructions[2], origin)
            else:
                instruction = False
            
            for event in pg.event.get():
                if event.type == QUIT:
                    terminate()
                    break
                elif event.type == KEYDOWN:
                    instruction = False
                    break
            pg.display.flip()
            pg.time.delay(12)

    def countdown(self):
        self.display.fill(BLACK)
        self.display.blit(countdown[3], origin)
        sfx('sfx/beep.wav')
        pg.display.flip()
        pg.time.delay(1000)
        self.display.fill(BLACK)
        self.display.blit(countdown[2], origin)
        sfx('sfx/beep.wav')
        pg.display.flip()
        pg.time.delay(1000)
        self.display.fill(BLACK)
        self.display.blit(countdown[1], origin)
        sfx('sfx/beep.wav')
        pg.display.flip()
        pg.time.delay(1000)
        self.display.fill(BLACK)
        self.display.blit(countdown[0], origin)
        sfx('sfx/start.wav')
        pg.display.flip()
        pg.time.delay(1000)

    def start(self):
        self.countdown()
        self.sprites = pg.sprite.Group()
        self.background_scroll = Background()
        self.blocks = pg.sprite.Group()
        self.player = Player(self)
        self.covid19 = COVID()
        self.masks = Mask()
        self.sprites.add(self.background_scroll)
        self.sprites.add(self.player)
        self.sprites.add(self.covid19)
        self.sprites.add(self.masks)
        
        #block_list = []
        o_x = WIDTH//2 - block_width//2
        o_y = HEIGHT - block_height
        self.r_x = o_x + random.randrange(int(-block_width*self.player.param), int(block_width*self.player.param))
        o_block = Block(o_x, o_y)
        o_block.type == 0
        self.sprites.add(o_block)
        self.blocks.add(o_block)
        for i in range(num_block):  
            r_dx = random.randrange(int(-block_width*self.player.param), int(block_width*self.player.param))
            self.r_x += r_dx
            if self.r_x > WIDTH - block_width:
                rw = self.r_x - 2*abs(r_dx)
            elif self.r_x < block_width:
                rw = self.r_x + 2*abs(r_dx)
            else:
                rw = self.r_x + r_dx
            r_block = Block(rw, HEIGHT*(num_block-i)//num_block)
            r_block.type = 0
            r_block.image = pg.transform.scale(blocktypes[r_block.type], (r_block.w, r_block.h))
            self.r_x = rw
            self.sprites.add(r_block)
            self.blocks.add(r_block)
        self.main_game()

    def main_game(self):
        self.game_over = False
        while not self.game_over:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        self.game_end()

    def events(self):
        for event in pg.event.get():
            if event.type == QUIT:
                if not self.game_over:
                    self.game_over = True
                terminate()
                break
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    self.player.jump()
    
    def update(self):
        self.sprites.update()
        if self.player.vy > 0:
            collide = pg.sprite.spritecollide(self.player, self.blocks, False)
            if collide:
                if self.player.y - player_height//2 < collide[0].rect.top:  
                    if collide[0].type == 0:
                        self.player.y = collide[0].rect.top
                        self.player.vy = 0
                    elif collide[0].type == 1:
                        self.player.y = collide[0].rect.top
                        sfx('sfx/powerup.wav')
                        self.player.vy = -BOOSTJUMP
                    elif collide[0].type == 2:
                        self.player.y = collide[0].rect.top
                        self.player.vy = 0
                        if self.masks.life < 2 and collide[0].resource > 0:
                            self.masks.life += 1
                            collide[0].resource -= 1
                            self.masks.image = masks[self.masks.life]
                        else:
                            pass
                    elif collide[0].type == 3:
                        self.player.vy = -1
                    elif collide[0].type == 4:
                        self.player.y = collide[0].rect.top
                        self.player.vy = 0
                        self.player.x += collide[0].locomotion
                        collide[0].rect.x += collide[0].locomotion
        if self.player.rect.top <= HEIGHT // 4:
            self.player.y += abs(self.player.vy)
            self.covid19.rect.y += abs(self.player.vy) #10*(1-exp(-abs(self.player.vy)//10))
            self.background_scroll.rect.y += abs(self.player.vy)//GAMELENGTH
            #self.background_scroll.image = main_scroll
            for b in self.blocks:
                b.rect.y += abs(self.player.vy)
                if b.rect.top >= HEIGHT:
                    b.kill()
                    self.player.score += 10
                    self.player.scorecount += 10
                    self.player.param = (self.player.score/5000 + 1)
        try:
            self.covid19.vy = (exp(abs(self.player.y-self.covid19.rect.y)/COVID_COEFF) * self.player.param)+0.5
        except:
            self.covid19.vy = self.player.param
        self.covid19.rect.y -= self.covid19.vy

        if self.player.y > self.covid19.rect.y and self.masks.life > -1:
            self.masks.life -= 1
            self.player.vy = 0
            self.masks.image = masks[self.masks.life]
            self.player.y = 100
            for i in range(10):
                if i%2 == 0:
                    self.player.y = 100
                    self.player.vy = 0
                    self.player.ay = 0
                    self.player.image = damaged
                    pg.time.delay(12)
                    pg.display.flip()
                else:
                    self.player.y = 100
                    self.player.vy = 0
                    self.player.ay = 0
                    self.player.image = standing[0]
                    pg.time.delay(12)
                    pg.display.flip()

            
        elif self.player.y > self.covid19.rect.y and self.masks.life <= -1:
            self.masks.image = masks[0]
            for b in self.blocks:
                b.rect.y -= max(self.player.vy, 10)
                if b.rect.y < 0:
                    b.kill()
        elif self.background_scroll.rect.y > 0:
            self.game_over = True
        if len(self.blocks) == 0:
            self.game_over = True

        while len(self.blocks) < num_block:
            r_dx = random.randrange(int(-block_width*self.player.param), int(block_width*self.player.param))
            if self.r_x > WIDTH - block_width:
                rw = self.r_x - 2*abs(r_dx)
            elif self.r_x < block_width:
                rw = self.r_x + 2*abs(r_dx)
            else:
                rw = self.r_x + r_dx
            b_new = Block(rw, random.randrange(-10, 0))
            self.r_x = rw
            self.blocks.add(b_new)
            self.sprites.add(b_new)

    def draw(self):
        #self.display.fill(BLACK)
        self.sprites.draw(self.display)
        self.scoreboard(str(self.player.score), 22, WHITE, WIDTH//2, 15)
        self.scoreboard('Double Jump Every 100 Points', 22, WHITE, 150, 45)
        self.scoreboard('Double Jump:'+str(self.player.double_jump), 22, WHITE, 150, 75)
        self.scoreboard('Current Date: '+self.background_scroll.calendar(), 22, WHITE, WIDTH-120, 15)
        self.scoreboard('Life:'+str(self.masks.life), 22, WHITE, WIDTH-100, 75)
        #self.display.blit(main_scroll, (self.background_scroll.x, self.background_scroll.y))
        pg.display.flip()

    def game_end(self):
        end_replay = True
        end_credit = True
        if self.masks.life < 0:
            sfx('sfx/death.wav')
            end_credit = False
        elif self.masks.life >= 0:
            end_replay = False
        while end_replay:
            self.display.fill(BLACK)
            self.scoreboard('YOU HAVE SURVIVED', 100, WHITE, WIDTH//2, HEIGHT//2 - 200)
            self.scoreboard('UNTIL', 100, WHITE, WIDTH//2, HEIGHT//2 - 100)
            self.scoreboard(self.background_scroll.calendar(), 100, WHITE, WIDTH//2, HEIGHT//2)
            mouse = pg.mouse.get_pos()
            if button_w1 < mouse[0] and button_w2 > mouse[0] and button_h1 < mouse[1] and button_h2 > mouse[1]:
                onstart = True
                self.game_over = False
                self.display.blit(main_start[1], button_pos)
            else:
                onstart = False
                self.display.blit(main_start[0], button_pos)
                pass
            for event in pg.event.get():
                if event.type == QUIT:
                    terminate()
                    break
                elif event.type == MOUSEBUTTONDOWN:
                    if onstart:
                        end_replay = False
                        self.start()
                        break
                    else:
                        pass
            pg.time.delay(120)
            pg.display.flip()
        while end_credit:
            self.display.fill(WHITE)
            self.scoreboard('HAPPY NEW 2021!!!', 120, BLACK, WIDTH//2, HEIGHT//2 - 200)
            for event in pg.event.get():
                if event.type == QUIT:
                    terminate()
                    break
                else:    
                    pass
            pg.time.delay(120)
            pg.display.flip()
        
    def scoreboard(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surf = font.render(text, True, color)
        text_rect = text_surf.get_rect()
        text_rect.midtop = (x, y)
        self.display.blit(text_surf, text_rect)
        
if __name__ == "__main__":
    Game().logo_screen()
    Game().start_screen()
    Game().instructions()
    Game().start()
    terminate()
