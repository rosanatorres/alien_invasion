import sys
import pygame

def check_keydown_events(event, ship):
     """Responde a pressionamentos de tecla"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event, ship):
    """Responde a solturas de tecla"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False  

def check_events(ship):
    """Responde a eventos pressionamento de teclas e de mouse"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # Move a ship para a direita ou esquerda quando a tecla eh pressionada
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        # Quando a tecla da direita ou esquerda eh solta a ship para
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship):
        """Update images on the screen and flip to the new screen."""
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip() 