'''
Space Wars is a take on the old classic game space invaders.
'''
# pylint: disable=import-error
# Imports
import game_objects
import pygame
import settings

# Initialize game engine
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
settings.init()



# Game helper functions
def show_title_screen():
    '''
    This will show the start screen.
    '''
    title_text = settings.FONT_XL.render("Battle of Britain!", 1, settings.WHITE)
    title_text_width = title_text.get_width()
    title_text_height = title_text.get_height()

    settings.SCREEN.blit(title_text, [(settings.WIDTH/2) - (title_text_width/2),
                                      (settings.HEIGHT/2) - (title_text_height/ 2)])


def show_stats():
    '''
    will blit player heath of screen.
    '''
    _hp = settings.FONT_MD.render(str(settings.SHIP.heath), 1, settings.WHITE)

    settings.SCREEN.blit(_hp, [0, 0])

def setup():
    '''
    this sets up the whole thing.
    '''
    # ''' add ship to player sprite groupe '''
    settings.PLAYER.add(settings.SHIP)

    mob_x_scale = 200
    mob_y_scale = 100


    for _x in range(100, settings.WIDTH-100, mob_x_scale):
        for _y in range(100, 300, mob_y_scale):
            settings.MOBS.add(game_objects.Mob(_x, _y, settings.ENEMY_IMG))



# Game loop
setup()

while not settings.DONE:
    # Input handling (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            settings.DONE = True
        elif event.type == pygame.KEYDOWN:
            if settings.STAGE == settings.START:
                if event.key == pygame.K_SPACE:
                    settings.STAGE = settings.PLAYING

            elif settings.STAGE == settings.PLAYING:
                if event.key == pygame.K_w:
                    settings.SHIP.shoot()

    # ''' poll key states '''
    STATE = pygame.key.get_pressed()
    A = STATE[pygame.K_a]
    S = STATE[pygame.K_s]
    D = STATE[pygame.K_d]

    if settings.STAGE == settings.PLAYING:
        if A:
            settings.SHIP.move_left()
        elif D:
            settings.SHIP.move_right()

        if S:
            settings.SHIP.shoot()
            settings.A_10_SOUND.play()

    # Game logic (Check for collisions, update points, etc.)
    if settings.STAGE == settings.PLAYING:
        settings.PLAYER.update()
        settings.LASERS.update()
        settings.BOMBS.update()
        settings.FLEET.update()
        settings.MOBS.update()
        settings.FIREBALL.update()

    if settings.SHIP.heath <= 0:
        settings.STAGE = settings.END


    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    if settings.STAGE == settings.START:
        show_title_screen()
    elif settings.STAGE == settings.PLAYING:
        settings.SCREEN.fill(settings.BLACK)
        settings.SCREEN.blit(settings.BACKGROUND_IMG, (0, 0))
        settings.LASERS.draw(settings.SCREEN)
        settings.BOMBS.draw(settings.SCREEN)
        settings.PLAYER.draw(settings.SCREEN)
        settings.MOBS.draw(settings.SCREEN)
        settings.FIREBALL.draw(settings.SCREEN)
        show_stats()


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop
    settings.CLOCK.tick(settings.REFRESH_RATE)


# Close window and quit
pygame.quit()
