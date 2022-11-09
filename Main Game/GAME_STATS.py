class GameStats:
    """game stats"""
    def __init__(self, ai_game):
        """initialize"""
        self.settings = ai_game.settings
        self.reset_stats()
        #starts the game in an active state
        self.game_active = True
    def reset_stats(self):
        self.ships_left = self.settings.ship_limit