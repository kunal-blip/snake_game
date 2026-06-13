# imports for the game 
import pygame as pg
import time as t
import random as rd

# pygame init 
pg.init()
red = (255,0,0)
blue = (51,153,255)
grey = (192,192,192)
green = (51, 102,0)

# window height and width 
win_width = 600
win_height = 400

# window caption and display
window = pg.display.set_mode((win_width, win_height))
pg.display.set_caption("Snake Game")
t.sleep(5)

# snake block and speed of the snake 
snake = 10  # snake block size 
# later to be calculated based on the level of the game

snake_speed = 15 # snake base speed 

# font styles for the game
font_style = pg.font.SysFont("comicsans", 20)
score_font = pg.font.SysFont("calibri", 26)