# A class to store all settings for Alien Invasion.

class Settings:
    def __init__(self):
        """Initialize the game's static settings."""
        #Screen Setting.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (160, 160, 160)
        #Ship settings.
        self.ship_speed = 2
        self.ship_limit = 3
        # self.star_speed = 1.0

        #Alien settings.
        self.alien_speed = 1
        self.fleet_drop_speed = 10


        #Bullet settings.
        self.bullet_speed = 3
        self.bullet_width = 4
        self.bullet_height = 10
        self.bullet_color = (0, 0, 0)
        # Limiting the Number of Bullets
        self.bullets_allowed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

        # How quickly the alien point values increase
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 0.5
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        self.alien_points = 500
    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        # self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)