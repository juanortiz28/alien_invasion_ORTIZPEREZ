import pygame


class Ship:
    """manage the ship"""
    def __init__(self, ai_game):
        """ship's starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #load up ship
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # start each ship at the bottom and center
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """draw ship at current location"""
        self.screen.blit(self.image, self.rect)