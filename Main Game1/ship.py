import pygame
class Ship:
    """manage the ship"""
    def __init__(self, ai_game):
        """ship's starting position"""
        self.screen = ai_game.screen
        self.angle = ai_game.angle
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load up ship

        self.og_image = pygame.image.load('../images/ship.bmp')
        self.image = self.og_image
        self.rect = self.image.get_rect()

        rot_image = pygame.transform.rotate(self.image, 90)
        self.image = rot_image

        # start each ship at the bottom and center
        self.rect.midright = self.screen_rect.midright

        #store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #movement
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """update the ship's position based on the movement flag"""
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed


        #update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def center_ship(self):
        """center after collision"""
        self.rect.midright = self.screen_rect.midright
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    def blitme(self):
        """draw ship at current location"""
        self.screen.blit(self.image, self.rect)