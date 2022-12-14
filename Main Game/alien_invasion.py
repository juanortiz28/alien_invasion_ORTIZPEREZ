import sys
import time
import pygame
from settings import Settings
from GAME_STATS import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        # self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Alien Invasion")
        self.stats = GameStats(self)

        self.sb = Scoreboard(self)
        self.angle = -90
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.bg_color = (230, 230, 230)
        self.play_button = Button(self, 'Play')


    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

            # #get rid of bullets that have disappeared
            # for bullet in self.bullets.copy():
            #     if bullet.rect.bottom <= 0:
            #         self.bullets.remove(bullet)
            # print(len(self.bullets))
    def _create_fleet(self):
        """create the fleet of aliens"""
        #create it and find how many in a row
        #spacing between each alien is equal to one alien width
        #make it
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_alien_x = available_space_x // (2 * alien_width)
        #determine number of rows
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        #create fleet
        for row_number in range(number_rows):
            #first row of aliens
            for alien_number in range(number_alien_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        #create an alien and place it in the row
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)
    def _check_events(self):
        """"respond to keys and mouse"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                # if event.key == pygame.K_q:
                #     sys.exit()
                # elif event.key == pygame.K_RIGHT:
                #     self.ship.moving_right = True
                # elif event.key == pygame.K_LEFT:
                #     self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                # if event.key == pygame.K_RIGHT:
                #     self.ship.moving_right = False
                # if event.key == pygame.K_LEFT:
                #     self.ship.moving_left = False

    def _check_keydown_events(self, event):
        """"respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.angle = -90
            self.ship.image = pygame.transform.rotate(self.ship.og_image, self.angle)
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.angle = 90
            self.ship.image = pygame.transform.rotate(self.ship.og_image, self.angle)
            self.ship.moving_left = True
        if event.key == pygame.K_UP:
            self.angle = 0
            self.ship.image = pygame.transform.rotate(self.ship.og_image, self.angle)
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.angle = 180
            self.ship.image = pygame.transform.rotate(self.ship.og_image, self.angle)
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()
        # if event.key == pygame.K_q:
        #     sys.exit()
        # elif event.key == pygame.K_RIGHT:
        #     self.ship.moving_right = True
        # elif event.key == pygame.K_LEFT:
        #     self.ship.moving_left = True
        # elif event.key == pygame.K_UP:
        #     self.ship.moving_up = True
        # elif event.key == pygame.K_DOWN:
        #     self.ship.moving_down = True
        # elif event.key == pygame.K_SPACE:
        #     self._fire_bullets()
    def _check_keyup_events(self, event):
        """respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
    def _check_play_button(self, mouse_pos):
        """start a new game when plaer clicks play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.stats.game_active = True
            self.stats.score = 0
            self.sb.prep_score()
            self.stats.ships_left = 3
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()


    def _fire_bullets(self):
        """create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    def _update_bullets(self):
        self.bullets.update()
        #get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()
    def _check_bullet_alien_collisions(self):
        #check if any bullets hit the aliens
        #if so, eliminate the alien and bullet
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            #destroy bullets and create a new fleet
            self.bullets.empty()
            self._create_fleet()
        if collisions:
            self.stats.score += self.settings.alien_points *len(self.aliens)
            self.sb.prep_score()
    def _update_aliens(self):
        """update the positions of aliens in the fleet"""
        self.aliens.update()
        #look for alien/ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_fleet_edges()
        self._check_aliens_bottom()

    def _ship_hit(self):
        """ship being hit by alien"""
        if self.stats.ships_left > 0:
            #ships left
            self.stats.ships_left -= 1
            #get rid of remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()
            #new fleet and ship
            self._create_fleet()
            self.ship.center_ship()
            #pause
            time.sleep(0.5)
        else:
            self.stats.game_active = False

    def _check_aliens_bottom(self):
        """checks if any ships has reached the bottom"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                ##treats as if ship gets hit
                self._ship_hit()
                break

    def _check_fleet_edges(self):
        """respond to aliens at edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        """drop the fleet and change direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    def _update_screen(self):
        """updates images1 on screen and flip to the new screen"""
        self.screen.fill(self.bg_color)
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()  #draws ship on screen
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        #draw sb
        self.sb.show_score()
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
