import random

#GAMESETTINGS
GAMENAME = '2020.exe'
WIDTH = 1280
HEIGHT = 720
aspect_ratio = (WIDTH, HEIGHT)
FPS = 60
GAMELENGTH = 5 #STANDARD
COVID_COEFF = 400 #THE SMALLER, EXPONENTIALLY HARDER

#POSITIONING
origin = (0, 0)
center = (WIDTH//2, HEIGHT//2)
button_width = 560
button_height = 100
button_pos = (WIDTH//2-button_width//2, HEIGHT*7//8-button_height//2)
button_w1 = WIDTH//2-button_width//2
button_w2 = WIDTH//2+button_width//2
button_h1 = HEIGHT*7//8-button_height//2
button_h2 = HEIGHT*7//8+button_height//2

block_width = 200
block_height = 20
player_width = 48
player_height = 64

#PHYSICS
player_acc = 3
player_maxspeed = 3
JUMPPOWER = 20
BOOSTJUMP = 30
GRAVITY = 1
AIR_RESISTANCE = 0.1
FRICTION = 0.5
ELASTICITY = 0.2
locomotion_speed = 5

#BLOCK PARAMETERS
num_block = 10
boost_mod = 9
heal_mod = 21
mud_mod = 13
moving_mod = 11

#COLORGAMUT
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50 , 50)
GREEN = (0, 255, 0)
BLUE = (50, 50 , 255)
