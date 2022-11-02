import pygame
class Ship:
    """manage the ship"""
    def __init__(self, ai_game):
        """ship's starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load up ship
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # start each ship at the bottom and center
        self.rect.midbottom = self.screen_rect.midbottom

        #store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #movement
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """update the ship's position based on the movement flag"""
        #update the ships x value, not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed


        #update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y


    def blitme(self):
        """draw ship at current location"""
        self.screen.blit(self.image, self.rect)