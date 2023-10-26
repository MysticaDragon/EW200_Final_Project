import pygame
import time
import random

import bg
from settings import *
from bg import *
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = screen.copy()
clock = pygame.time.Clock()

bg.draw_backround()
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Game ended')
            pygame.quit()



pygame.display.flip()
clock.tick(60)