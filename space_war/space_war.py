'''
Space Wars is a take on the old classic game space invaders.
'''

# Imports
import pygame


# Initialize game engine
pygame.init()


# Window
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
TITLE = "Space War"
SCREEN = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
CLOCK = pygame.time.Clock()
REFRESH_RATE = 60


# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (100, 255, 100)

# Global Varibles
STAGE = 0
DONE = False

# Fonts
FONT_SM = pygame.font.Font(None, 24)
FONT_MD = pygame.font.Font(None, 32)
FONT_LG = pygame.font.Font(None, 64)
FONT_XL = pygame.font.Font("assets/fonts/spacerangerboldital.ttf", 96)


# Images
ship_IMG =  pygame.image.load('assets/images/player.png').convert_alpha()
LASER_IMG = pygame.image.load('assets/images/laserRed.png').convert_alpha()
ENEMY_IMG = pygame.image.load('assets/images/enemyShip.png').convert_alpha()


# Sounds
EXPLOSION = pygame.mixer.Sound('assets/sounds/explosion.ogg')
SHOOT_SOUND = pygame.mixer.Sound('assets/sounds/shoot.wav')


# Stages
START = 0
PLAYING = 1
END = 2


# Game classes
class ship(pygame.sprite.Sprite):
    '''
    This is the class of the ship. It will
    handle movement, decteding weather it was shhot. and updating.
    '''
    def __init__(self, ship_x, ship_y, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = ship_x
        self.rect.y = ship_y

        self.speed = 3

    def move_left(self):
        '''
        moves space ship left
        '''
        self.rect.x -= self.speed

    def move_right(self):
        '''
        moves space ship right
        '''
        self.rect.x += self.speed

    def shoot(self):
        '''
        this will start the process of a laser being shot from the ship.
        '''

        laser = Laser(LASER_IMG)
        laser.rect.centerx = self.rect.centerx
        laser.rect.centery = self.rect.top
        lasers.add(laser)
        SHOOT_SOUND.play()

    def update(self):
        '''
        this will up date the ship.
            See if it has hit walls
        '''

        if self.rect.left < 0:
            self.rect.left = 0

        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH

class Laser(pygame.sprite.Sprite):
    '''
    This class will hold all the lasers shot. And will move and kill them.
    '''
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()

        self.speed = 5

    def update(self):
        '''
        Move the lasers up the screen and will delete them when appoiot
        '''
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()


class Mob(pygame.sprite.Sprite):
    '''
    This class will house all the enemies and update them.
    '''
    def __init__(self, mob_x, mob_y, image):
        super().__init__()

        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = mob_x
        self.rect.y = mob_y


    def update(self):
        '''
        This will check to see if the mobs have been hit.
        '''
        hit_list = pygame.sprite.spritecollide(self, lasers, True, pygame.sprite.collide_mask)
        if len(hit_list) > 0:
            self.kill()

class Bomb():
    pass

class Fleet(): # fleet of enemy ships
    '''
    This is a class of the mobs where it will process their movement.
    '''
    def __init__(self, mobes):
        self.mobs = mobes
        self.speed = 5
        self.moving_right = True


    def move(self):
        '''
        This function will move the fleet.
        '''
        hits_edge = False

        for _m in mobs:
            if self.moving_right:
                _m.rect.x += self.speed
                if _m.rect.right >= WIDTH:
                    hits_edge = True

            else:
                _m.rect.x -= self.speed
                if _m.rect.left <= 0:
                    hits_edge = True

        if hits_edge:
            self.reverse()
            self.move_down()

    def reverse(self):
        '''
        IDK WHY THIS HAS TO BE A FUNCTION
        '''
        self.moving_right = not self.moving_right

    def move_down(self):
        '''
        This runs through all the mobs, then moves them down.
        '''
        for mob in self.mobs:
            mob.rect.y += 5

    def update(self):
        '''
        updates the fleet
        '''
        self.move()


# Game helper functions
def show_title_screen():
    '''
    This will show the start screen.
    '''
    title_text = FONT_XL.render("Space War!", 1, WHITE)
    SCREEN.blit(title_text, [128, 204])

# def show_stats(player):
#     pass

def setup():
    '''
    this sets up the whole thing.
    '''
    global STAGE, DONE
    global PLAYER, ship, lasers, mobs, fleet
    # ''' Make game objects '''
    ship = ship(384, 536, ship_IMG)

    # ''' Make sprite groups '''
    PLAYER = pygame.sprite.GroupSingle()
    PLAYER.add(ship)

    lasers = pygame.sprite.Group()

    mob1 = Mob(100, 100, ENEMY_IMG)
    mob2 = Mob(300, 100, ENEMY_IMG)
    mob3 = Mob(500, 100, ENEMY_IMG)

    mobs = pygame.sprite.Group()
    mobs.add(mob1, mob2, mob3)



    fleet = Fleet(mobs)

    # ''' set stage '''
    STAGE = START
    DONE = False



# Game loop
setup()

while not DONE:
    # Input handling (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            DONE = True
        elif event.type == pygame.KEYDOWN:
            if STAGE == START:
                if event.key == pygame.K_SPACE:
                    STAGE = PLAYING

            elif STAGE == PLAYING:
                if event.key == pygame.K_w:
                    ship.shoot()

    # ''' poll key states '''
    STATE = pygame.key.get_pressed()
    A = STATE[pygame.K_a]
    S = STATE[pygame.K_s]
    D = STATE[pygame.K_d]

    if STAGE == PLAYING:
        if A:
            ship.move_left()
        elif D:
            ship.move_right()
        else:
            block1_vx = 0

        if S:
            ship.shoot()

    # Game logic (Check for collisions, update points, etc.)
    if STAGE == PLAYING:
        PLAYER.update()
        lasers.update()
        fleet.update()
        mobs.update()

    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    if STAGE == START:
        show_title_screen()
    elif STAGE == PLAYING:
        SCREEN.fill(BLACK)
        lasers.draw(SCREEN)
        PLAYER.draw(SCREEN)
        mobs.draw(SCREEN)
    else:
        print("else")

    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop
    CLOCK.tick(REFRESH_RATE)


# Close window and quit
pygame.quit()
