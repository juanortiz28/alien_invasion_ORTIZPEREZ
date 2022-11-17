import pygame.font

class Scoreboard:
    """a class to report scoring"""
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #font settings
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        #prepare initial score image
        self.prep_score()
    def prep_score(self):
        """render score image"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        #display the score at top right
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    def show_score(self):
        """draw score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)