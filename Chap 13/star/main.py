import sys
import pygame
from settings1 import Settings
from star import Star
from random import randint



class Galaxy:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Star")
        self.stars = pygame.sprite.Group()
        self._create_galaxy()
        self.bg_color = (255, 255, 255)

    def run_game(self):
        while True:
            self._update_screen()
            self._check_events()
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
    def _create_galaxy(self):
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.settings.screen_width - star_width
        number_star_x = available_space_x // (2 * star_width)
        available_space_y = (self.settings.screen_height - star_height)
        number_rows = available_space_y // (2 * star_height)
        for row_number in range(number_rows):
            for star_number in range(number_star_x):
                self._create_star(star_number, row_number)
    def _create_star(self, alien_number, row_number):
        star = Star(self)
        star_width, star_height = star.rect.size
        random_x = randint(0, int(self.settings.screen_width - star_width))
        #star.x = star_width + 2 * star_width * alien_number
        star.x = star_width + random_x
        star.rect.x = star.x
        random_y = randint(0, self.settings.screen_height - star_height)
        #star.rect.y = star_height + 2 * star.rect.height * row_number
        star.rect.y = star_height + random_y
        self.stars.add(star)
    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.stars.draw(self.screen)
        pygame.display.flip()
if __name__ == '__main__':
    ai = Galaxy()
    ai.run_game()
