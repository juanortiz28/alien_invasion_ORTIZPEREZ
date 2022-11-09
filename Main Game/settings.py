class Settings:
    """game settings"""
    def __init__(self):
        #screen
        # self.screen_width = 800
        # self.screen_height = 600
        self.bg_color = (230,230,230)
        #bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 2.0
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
        #ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3
        #alien settings
        self.alien_speed = 0.5
        self.fleet_drop_speed = 10
        #fleet direction of 1 respresents right and -1 left
        self.fleet_direction = 1

