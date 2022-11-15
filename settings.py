class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialise the game's settings."""
        # Screen settings
        self.screen_width = 960
        self.screen_height = 640
        self.bg_color = (0, 0, 0)

        # Ship settings
        self.ship_speed = 1.5