import pygame
from pygame.sprite import Sprite

class Rain(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/raindrop.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.settings.rain_speed * self.settings.drop_direction)
        self.rect.x = self.x
        # self.y += 1
        # self.rect.y = self.y
        w, h = pygame.display.get_surface().get_size()
        self.rect.y = self.rect.y % h
        # if self.rect.top > self.screen.get_rect().bottom:
        #     self.rect.bottom = 0