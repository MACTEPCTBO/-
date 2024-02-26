import pygame
from random import randint
import random

WIDTH,HEIGHT,cell,FPS = 600,600,2,10
screen,time = pygame.display.set_mode((WIDTH,HEIGHT)),pygame.time.Clock()

bots = []
bot_id = 0

pressed = True
time_pressed = 0

def bots_id():
    global bot_id
    bot_id += 1