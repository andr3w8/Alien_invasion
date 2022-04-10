import pygame
from pygame.sprite import Sprite

class Star(Sprite):

    def __init__(self, sg_game):
        super().__init__()
        self.screen = sg_game.screen
        self.settings = sg_game.settings

        self.image = pygame.image.load('images/space5.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.star_speed
        self.rect.topleft = round(self.x), round(self.y)