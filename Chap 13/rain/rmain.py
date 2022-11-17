import sys
import pygame
from rsettings import Settings
from rain import Rain



class Rain_Drop:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Star")
        self.rain = pygame.sprite.Group()
        self._create_rain_drop()
        self.bg_color = (255, 255, 255)

    def run_game(self):
        while True:
            self._update_screen()
            self._update_rain()
            self._check_events()
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
    def _create_rain_drop(self):
        rain = Rain(self)
        rain_width, rain_height = rain.rect.size
        available_space_x = self.settings.screen_width - rain_width
        number_rain_x = available_space_x // (2 * rain_width)
        available_space_y = (self.settings.screen_height - rain_height)
        number_rows = available_space_y // (2 * rain_height)
        for row_number in range(number_rows):
            for rain_number in range(number_rain_x):
                self._create_rain(rain_number, row_number)
    def _create_rain(self, rain_number, row_number):
        rain = Rain(self)
        rain_width, rain_height = rain.rect.size
        rain.x = rain_width + 2 * rain_width * rain_number
        rain.rect.x = rain.x
        rain.rect.y = rain_height + 2 * rain.rect.height * row_number
        self.rain.add(rain)
    def _update_rain(self):
        self.rain.update()
        self._check_rain_edges()

    def _check_rain_edges(self):
        for rain in self.rain.sprites():
            if rain.check_edges():
                self._change_drop_direction()
                break
    def _change_drop_direction(self):
        for rain in self.rain.sprites():
            rain.rect.y += self.settings.drop_drop_speed
        self.settings.drop_direction *= -1
    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.rain.draw(self.screen)
        pygame.display.flip()
if __name__ == '__main__':
    ai = Rain_Drop()
    ai.run_game()
