'''
    houses all global variables.
'''
# pylint: disable=import-error
# pylint: disable=global-variable-undefined

import pygame
import game_objects

def init(): # pylint: disable=too-many-statements
    '''
    This will initialize all variables.
    '''
    # Window
    global WIDTH, HEIGHT, SIZE, TITLE, SCREEN

    WIDTH = 1280
    HEIGHT = 720
    SIZE = (WIDTH, HEIGHT)
    TITLE = "Battle of Britain"
    SCREEN = pygame.display.set_mode(SIZE)
    pygame.display.set_caption(TITLE)


    # Timer
    global CLOCK, REFRESH_RATE

    CLOCK = pygame.time.Clock()
    REFRESH_RATE = 60

    # Colors
    global RED, WHITE, BLACK, YELLOW, GREEN, ALFA


    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    YELLOW = (255, 255, 0)
    GREEN = (100, 255, 100)

    ALFA = 0



    # Fonts
    global FONT_SM, FONT_MD, FONT_LG, FONT_XL

    FONT_SM = pygame.font.Font(None, 24)
    FONT_MD = pygame.font.Font(None, 32)
    FONT_LG = pygame.font.Font(None, 64)
    FONT_XL = pygame.font.Font("assets/fonts/times.ttf", 96)


    # Images
    global SHIP_IMG, LASER_IMG, ENEMY_IMG, BOMB_IMG
    global EXPLOSION, BACKGROUND_IMG, FIREBALL_IMG, UNION_JACK_IMG
    global END_GAME_IMG

    SHIP_IMG = pygame.image.load('assets/images/spitfire.png').convert_alpha()
    LASER_IMG = pygame.image.load('assets/images/laserRed.png').convert_alpha()
    ENEMY_IMG = pygame.image.load('assets/images/messerschmitt-bf-109-a1.png').convert_alpha()
    BOMB_IMG = pygame.image.load('assets/images/laserGreen.png').convert_alpha()
    EXPLOSION = pygame.image.load('assets/images/explosion.png').convert()
    BACKGROUND_IMG = pygame.image.load('assets/images/Background/ocean.jpg').convert()
    FIREBALL_IMG = pygame.image.load('assets/images/fireball-effect.png').convert_alpha()
    UNION_JACK_IMG = pygame.image.load('assets/images/UnionJack.png').convert()
    END_GAME_IMG = pygame.image.load('assets/images/nuckler.jpeg').convert()

    # Sounds
    global EXPLOSION_SOUND, SHOOT_SOUND, A_10_SOUND, END_GAME_SOUND, PLAYED_END_GAME
    global end_game_start_time, sound_length

    EXPLOSION_SOUND = pygame.mixer.Sound('assets/sounds/explosion_sound.ogg')
    SHOOT_SOUND = pygame.mixer.Sound('assets/sounds/shoot.wav')
    A_10_SOUND = pygame.mixer.Sound('assets/sounds/A-10_gun.ogg')
    END_GAME_SOUND = pygame.mixer.Sound('assets/sounds/MW2_TACTICAL_NUKE .ogg')
    PLAYED_END_GAME = False
    end_game_start_time = float(0)
    sound_length = float(100000000)


    # STATS
    global SHIP_MAX_HEALTH, KILLS_CONFIRMED

    SHIP_MAX_HEALTH = 100
    KILLS_CONFIRMED = 0


    # Stages
    global START, PLAYING, END, LOST, WIN, STAGE, DONE, SHOW_VIEDO


    START = 0
    PLAYING = 1
    END = 2
    LOST = 3
    WIN = 4

    STAGE = START

    DONE = False

    SHOW_VIEDO = False


    # Levels
    global LEVEL, LEVEL1

    LEVEL = 0
    LEVEL1 = 1


    # Money
    global MONEY

    MONEY = 100


    # Objects
    global PLAYER, LASERS, MOBS, FLEET, BOMBS, SHIP, FIREBALL, TEMP_MOB


    rect = SHIP_IMG.get_rect()
    rect_x = rect.centerx
    rect_y = rect.bottom
    SHIP = game_objects.Ship(WIDTH/2-rect_x, HEIGHT-rect_y, SHIP_IMG)


    PLAYER = pygame.sprite.GroupSingle()
    LASERS = pygame.sprite.Group()
    BOMBS = pygame.sprite.Group()
    FIREBALL = pygame.sprite.Group()
    MOBS = pygame.sprite.Group()
    FLEET = game_objects.Fleet(MOBS)
    TEMP_MOB = pygame.sprite.Group()


    # counter
    global LOST_FRAME, PLAYING_FRAME, FRAME_NUMBER

    PLAYING_FRAME = 0
    LOST_FRAME = 0
    FRAME_NUMBER = 0


    # Surface
    global SUFACE

    SUFACE = pygame.Surface(SIZE)
    SUFACE.fill(BLACK)
