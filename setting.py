class Settings():
       
       """A class to store all settings for Alien Invasion."""

       def __init__(self):
           """Initialize the game's settings."""
           # Screen settings
           self.screen_width = 900
           self.screen_height = 600
           self.bg_color = (230, 230, 230)
           self.ship_speed_factor = 1.5