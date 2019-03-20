'''
Space Wars is a take on the old classic game space invaders.
'''
# pylint: disable=import-error
# pylint: disable=wrong-import-position

# Imports

import random
import pygame
import settings

# Initialize game engines
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
settings.init()

# Imports
import game_objects
import game_loop



def setup():
    '''
    this sets up the whole thing.
    '''
    # ''' add ship to player sprite groupe '''
    settings.PLAYER.add(settings.SHIP)

    mob_x_scale = 200
    mob_y_scale = 75

    for _x in range(100, settings.WIDTH-100, mob_x_scale):
        # makes y value for the location, based on scale
        for _y in range(-0, 300, mob_y_scale):
            # adds the enemy to the class
            settings.MOBS.add(game_objects.Mob(_x, _y, settings.ENEMY_IMG))


    num_planes = 100
    for i in range(num_planes):
        x_3 = random.randrange(100, settings.WIDTH-100)
        y_3 = random.randrange(-10000, -100)
        _p = [x_3, y_3]
        settings.MOBS.add(game_objects.Mob(x_3, y_3, settings.ENEMY_IMG))
        i = i

# Game loop
setup()
game_loop.game_loop()

# Close window and quit
pygame.quit()
