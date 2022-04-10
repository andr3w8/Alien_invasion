import sys
import pygame
from raindrop import Raindrop
from pygame.sprite import Group


def let_it_rain():
    '''initialize pygame, settings, and screen object'''
    pygame.init()
    screen_width = 1200
    screen_height = 800
    bg_color = (144, 177, 226)
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Let It Rain")

    raindrop = Raindrop(screen)
    raindrops = Group()

    #number of drops in a row
    spacex = screen_width - (2 * raindrop.rect.width)
    raindrop_number_x = int(spacex / (2 * raindrop.rect.width))


    #start window for raindrops
    while True:
        screen.fill(bg_color)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        for raindrop_number in range(raindrop_number_x):
            raindrop = Raindrop(screen)
            raindrop.rect.x = raindrop.rect.x + 2 * raindrop.rect.x * raindrop_number_x
            raindrops.add(raindrop)

        raindrops.draw(screen)
        pygame.display.flip()

        let_it_rain()