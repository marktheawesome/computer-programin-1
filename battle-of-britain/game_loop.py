'''
This will house the game loop
'''
# pylint: disable=import-error
# pylint: disable=global-at-module-level

import random
import time
import math
import pygame
import settings
import viedo
import game_objects


viedo.init()

global NEW_HEIGHT, KEYS
KEYS = []
NEW_HEIGHT = settings.HEIGHT * (-1/4)


# Game helper functions
def show_title_screen():
    '''
    This will show the start screen.
    '''
    settings.SCREEN.fill(settings.BLACK)
    title_text = settings.FONT_XL.render("Battle of Britain!", 1, settings.WHITE)
    title_text_width = title_text.get_width()
    title_text_height = title_text.get_height()

    settings.SCREEN.blit(title_text, [(settings.WIDTH/2) - (title_text_width/2),
                                      (settings.HEIGHT/2) - (title_text_height/ 2)])


def show_lost_screen():
    '''
    This will show the lost screen.
    '''
    global NEW_HEIGHT

    title_text = settings.FONT_XL.render("GAME OVER", 1, settings.WHITE)
    title_text_r = settings.FONT_XL.render("GAME OVER", 1, settings.RED)
    title_text_width = title_text.get_width()
    title_text_height = title_text.get_height()

    if NEW_HEIGHT - settings.HEIGHT - title_text_height <= (settings.HEIGHT/2 -
                                                            title_text_height/2):
        text_height = NEW_HEIGHT - settings.HEIGHT - title_text_height
        text_width = (settings.WIDTH/2) - (title_text_width/2)

        settings.SCREEN.blit(title_text, [text_width, text_height])
        NEW_HEIGHT += 5

    else:
        if settings.LOST_FRAME >= 200 and settings.ALFA <= 255:
            settings.SCREEN.blit(title_text, [(settings.WIDTH/2) - (title_text_width/2),
                                              settings.HEIGHT/2 - title_text_height/2])
            settings.SUFACE.blit(title_text_r, [(settings.WIDTH/2) - (title_text_width/2),
                                                settings.HEIGHT/2 - title_text_height/2])
        else:
            settings.SCREEN.blit(title_text, [(settings.WIDTH/2) - (title_text_width/2),
                                              settings.HEIGHT/2 - title_text_height/2])


    if settings.LOST_FRAME % 2 == 0 and settings.ALFA <= 255 and settings.LOST_FRAME >= 199:
        settings.ALFA += 1

    settings.LOST_FRAME += 1
    settings.SUFACE.set_alpha(settings.ALFA)

    settings.SCREEN.blit(settings.SUFACE, (0, 0))
    if settings.LOST_FRAME == 600:
        settings.STAGE = settings.END


def show_win_screen():
    '''
    This will show the win screen.
    '''
    settings.SCREEN.fill(settings.BLACK)
    settings.SCREEN.blit(settings.UNION_JACK_IMG, (0, 0))
    title_text = settings.FONT_XL.render("We Win!!!", 1, settings.WHITE)
    title_text_width = title_text.get_width()
    title_text_height = title_text.get_height()
    settings.SCREEN.blit(title_text, [(settings.WIDTH/2) - (title_text_width/2),
                                      settings.HEIGHT - title_text_height])
    settings.STAGE = settings.END


def show_end_screen():
    '''
    This will show the start screen.
    '''
    settings.SCREEN.fill(settings.BLACK)
    title_text = settings.FONT_XL.render("Would you like to replay?", 1, settings.WHITE)
    title_text_width = title_text.get_width()
    title_text_height = title_text.get_height()

    settings.SCREEN.blit(title_text, [(settings.WIDTH/2) - (title_text_width/2),
                                      (settings.HEIGHT/2) - (title_text_height/ 2)])

    under_title_text = settings.FONT_MD.render("Press any button.", 1, settings.WHITE)
    under_title_text_width = under_title_text.get_width()
    # under_title_text_height = under_title_text.get_height()

    settings.SCREEN.blit(under_title_text, [(settings.WIDTH/2) - (under_title_text_width/2),
                                            (settings.HEIGHT/2) + (title_text_height/2)])


def show_stats():
    '''
    will blit player heath of screen.
    '''

    fps = settings.FONT_SM.render(str(int(settings.CLOCK.get_fps())),
                                  True, pygame.Color('green'))

    # _hp = settings.FONT_MD.render(str(settings.SHIP.heath), 1, settings.WHITE)
    _kc = settings.FONT_MD.render(str(settings.KILLS_CONFIRMED), 1, settings.WHITE)

    # settings.SCREEN.blit(_hp, [0, 0])
    settings.SCREEN.blit(fps, (0 + fps.get_width(), 0 +  fps.get_height()))
    settings.SCREEN.blit(_kc, [settings.WIDTH-_kc.get_width(), 0])



def draw_hp():
    '''
    Draws the hp bar.
    '''
    hp_inner_rect = [7, settings.HEIGHT - 50, (settings.SHIP.heath/
                                               settings.SHIP_MAX_HEALTH) * 100, 25]
    pygame.draw.rect(settings.SCREEN, settings.GREEN, hp_inner_rect, 0)

    hp_outter_rect = [4, settings.HEIGHT - 53, 103, 28]
    pygame.draw.rect(settings.SCREEN, settings.BLACK, hp_outter_rect, 5)


def draw_stage_playing():
    '''
    This is all the code that will draw, blit, or fill.
    During the playing portion of the game.
    '''
    settings.SCREEN.fill(settings.BLACK)
    settings.SCREEN.blit(settings.BACKGROUND_IMG, (0, 0))
    settings.LASERS.draw(settings.SCREEN)
    settings.BOMBS.draw(settings.SCREEN)
    settings.PLAYER.draw(settings.SCREEN)
    settings.SENTRYS.draw(settings.SCREEN)
    settings.MOBS.draw(settings.SCREEN)
    settings.FIREBALL.draw(settings.SCREEN)
    settings.BULLETS.draw(settings.SCREEN)
    draw_hp()
    show_stats()

    if settings.SHOW_VIEDO:
        viedo.show_video()


def end_game_sound():
    '''
    This will dertemin weather to bring arounf the end game
    '''
    temp = random.randint(0, 1000)
    if temp == 5 and not settings.PLAYED_END_GAME and settings.KILLS_CONFIRMED > 50:
        settings.END_GAME_SOUND.play()
        settings.PLAYED_END_GAME = True
        settings.END_GAME_START_TIME = int(time.time())
        settings.END_GAME_START_TIME = math.ceil(settings.END_GAME_START_TIME)
        settings.SOUND_LENGTH = int(settings.END_GAME_SOUND.get_length())


    if (math.ceil(time.time()) - settings.END_GAME_START_TIME >=
            settings.SOUND_LENGTH and settings.PLAYED_END_GAME):
        settings.SHOW_VIEDO = True


def game_logic():
    '''
    This is all the code that will update the classes.
    During the playing portion of the game.
    '''

    if settings.STAGE == settings.PLAYING and not settings.VIEDO_DONE:
        settings.PLAYER.update()
        settings.LASERS.update()
        settings.BOMBS.update()
        settings.FLEET.update()
        settings.MOBS.update()
        settings.FIREBALL.update()
        end_game_sound()
        settings.SENTRYS.update()
        settings.BULLETS.update()


    elif settings.STAGE == settings.LOST:
        settings.LASERS.update()
        settings.BOMBS.update()
        settings.FLEET.update()
        settings.FIREBALL.update()

    if settings.SHIP.heath <= 0:
        settings.STAGE = settings.LOST

    if not settings.MOBS or settings.VIEDO_DONE:
        settings.STAGE = settings.WIN

    if not settings.CODE:
        check_code()


def ship_movement(_a, _d):
    '''
    Logic for moving the ship.
    During the playing portion of the game.
    '''
    if _a:
        settings.SHIP.move_left()
    elif _d:
        settings.SHIP.move_right()
    else:
        pass


def continuous_shooting(_s):
    '''
    Holding S will fire a continuous stream of bulletts.
    '''
    if _s:
        settings.SHIP.shoot()
        settings.A_10_SOUND.play()


def check_code():
    '''
    check to see if the code was entered.
    '''

    _up = 273
    _down = 274
    _left = 276
    _right = 275
    _b = 98
    _a = 97
    _enter = 13

    _code = [_up, _up, _down, _down, _left, _right, _left, _right, _b, _a, _enter]

    if len(KEYS) > 11:
        del KEYS[0]

    if KEYS == _code:
        settings.CODE = True
        print("GG")


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
        y_3 = random.randrange(-1000, -100)
        _p = [x_3, y_3]
        settings.MOBS.add(game_objects.Mob(x_3, y_3, settings.ENEMY_IMG))
        i = i


def game_loop():
    '''
    This is the game loop
    '''
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
                    if event.key == pygame.K_SPACE:
                        settings.SHIP.shoot()

                    elif event.key == pygame.K_k:
                        settings.STAGE = settings.LOST

                    elif event.key == pygame.K_SPACE:
                        settings.STAGE = settings.LOST

                if settings.STAGE == settings.END:
                    if event.key:
                        settings.STAGE = settings.RESTART


                KEYS.append(event.key)


        # ''' poll key states '''
        _state = pygame.key.get_pressed()
        if not settings.PLAYED_END_GAME:
            _a = _state[pygame.K_a]
            _s = _state[pygame.K_s]
            _d = _state[pygame.K_d]

        if settings.STAGE == settings.PLAYING:
            settings.PLAYING_FRAME += 1
            ship_movement(_a, _d)
            continuous_shooting(_s)

        elif settings.STAGE == settings.LOST:
            settings.FLEET.update()

        # Game logic (Check for collisions, update points, etc.)
        game_logic()

        # Drawing code (Describe the picture. It isn't actually drawn yet.)
        draw_stage_playing()


        if settings.STAGE == settings.START:
            show_title_screen()

        elif settings.STAGE == settings.LOST:
            show_lost_screen()

        elif settings.STAGE == settings.WIN:
            show_win_screen()
            # time.sleep(3)
            settings.STAGE = settings.END

        elif settings.STAGE == settings.END:
            show_end_screen()

        settings.FRAME_NUMBER += 1

        if settings.STAGE == settings.RESTART:
            settings.init()
            settings.STAGE = settings.START
            setup()


        # Update screen (Actually draw the picture in the window.)

        fps = settings.FONT_SM.render(str(int(settings.CLOCK.get_fps())),
                                      True, pygame.Color('green'))
        settings.SCREEN.blit(fps, (0 + fps.get_width(), settings.HEIGHT - fps.get_height()))
        pygame.display.flip()


        # Limit refresh rate of game loop
        settings.CLOCK.tick(settings.REFRESH_RATE)
