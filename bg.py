from settings import *
import pygame

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = screen.copy()
# intro catch your dragon bg
forest = pygame.image.load('assets/images/bg_1.png').convert()
forest.set_colorkey((0, 0, 0))

# cut scene 1 bg
town = pygame.image.load('assets/images/bg_town.png').convert()
town.set_colorkey((0, 0, 0))

# skies
c1 = pygame.image.load('assets/images/clouds_1.png').convert()
c1.set_colorkey((0, 0, 0))
c2 = pygame.image.load('assets/images/clouds_2.png').convert()
c2.set_colorkey((0, 0, 0))
c3 = pygame.image.load('assets/images/clouds_3.png').convert()
c3.set_colorkey((0, 0, 0))
c4 = pygame.image.load('assets/images/clouds_4.png').convert()
c4.set_colorkey((0, 0, 0))
c5 = pygame.image.load('assets/images/clouds_5.png').convert()
c5.set_colorkey((0, 0, 0))
c6 = pygame.image.load('assets/images/clouds_6.png').convert()
c6.set_colorkey((0, 0, 0))
c7 = pygame.image.load('assets/images/clouds_7.png').convert()
c7.set_colorkey((0, 0, 0))
c8 = pygame.image.load('assets/images/clouds_8.png').convert()
c8.set_colorkey((0, 0, 0))

def draw_backround():
    background.blit(c5,(SCREEN_WIDTH,SCREEN_HEIGHT),)