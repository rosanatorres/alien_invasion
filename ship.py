import pygame
class Ship():
    def __init__(self, screen, ai_settings):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Armazena um valor decimal para o centro da ship
        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Atualiza a posicao da ship de acordo com a flag de movimento"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        
        #Atualiza o objeto rect de acordo self.center
        self.rect.centerx = self.center
    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
