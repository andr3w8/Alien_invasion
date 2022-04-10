import pygame
from pygame.sprite import Sprite


class Raindrop(Sprite):

    def __init__(self, screen):

        #load image
        super(Raindrop, self).__init__()
        self.screen = screen
        self.pic = pygame.image.load('rain.jpg')
        self.image = pygame.transform.smoothscale(self.pic,(50,60))
        self.rect = self.image.get_rect()

        #starting position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def blit(self):
        raindrop.draw(screen)
        self.screen.blit(self.image, self.rect)
