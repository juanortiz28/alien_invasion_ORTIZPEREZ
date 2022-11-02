class Settings:
    """game settings"""
    def __init__(self):
        #screen
        # self.screen_width = 800
        # self.screen_height = 600
        self.bg_color = (230,230,230)
        #bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        #ship settings
        self.ship_speed = 1.5
