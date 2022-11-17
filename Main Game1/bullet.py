import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired"""
    def __init__(self, ai_game):
        """bullet at the ships location"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #create a bullet rect at (0,0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #store the bullet's position as a decimal value
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet up the screen"""
        #update the decimal position of the bullet
        self.x -= self.settings.bullet_speed
        #update the rect position
        self.rect.x = self.x
    def draw_bullet(self):
        #draw bullet on screen
        pygame.draw.rect(self.screen, self.color, self.rect)
