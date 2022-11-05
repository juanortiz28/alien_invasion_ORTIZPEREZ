import pygame
from pygame.sprite import Sprite
from random import randint

class Star(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()
        #start each alien top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #store alien's  x- position
        self.x = float(self.rect.x)
        self.random = randint(0, 5)
