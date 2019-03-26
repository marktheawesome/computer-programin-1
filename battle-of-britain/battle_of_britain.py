'''
battle of britan is a creative take on the real battle.
'''
# pylint: disable=import-error
# pylint: disable=wrong-import-position

# Imports
import pygame

# Initialize game engines
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()


# Imports
import settings
settings.init()
import game_loop



# Game loop
game_loop.setup()
game_loop.game_loop()



# Close window and quit
pygame.quit()
