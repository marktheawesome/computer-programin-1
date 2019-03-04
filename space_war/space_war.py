# Imports
import pygame


# show_up = pygame.sprite.
# Initialize game engine
pygame.init()


# Window
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
TITLE = "Space War"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (100, 255, 100)


# Fonts
FONT_SM = pygame.font.Font(None, 24)
FONT_MD = pygame.font.Font(None, 32)
FONT_LG = pygame.font.Font(None, 64)
FONT_XL = pygame.font.Font("assets/fonts/spacerangerboldital.ttf", 96)


# Images
ship_img = pygame.image.load('assets/images/player.png').convert_alpha()
laser_img = pygame.image.load('assets/images/laserRed.png').convert_alpha()
enemy_img = pygame.image.load('assets/images/enemyShip.png').convert_alpha()


# Sounds
EXPLOSION = pygame.mixer.Sound('assets/sounds/explosion.ogg')
SHOOT_SOUND = pygame.mixer.Sound('assets/sounds/shoot.wav')


# Stages
START = 0
PLAYING = 1
END = 2


# Game classes
class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 

        self.speed = 3

    def move_left(self):
        self.rect.x -= self.speed
    
    def move_right(self):
        self.rect.x +=self.speed

    def shoot(self):
        print('SHOOT!')

        laser = Laser(laser_img)
        laser.rect.centerx = self.rect.centerx
        laser.rect.centery = self.rect.top
        lasers.add(laser)

        SHOOT_SOUND.play()

    def update(self):
        # if self.rect.x < 0:
        #     self.rect.x = 0
        
        # elif self.rect.x + int(self.rect[2]) > WIDTH:
        #     self.rect.x = WIDTH - int(self.rect[2])

        if self.rect.left < 0:
            self.rect.left = 0 

        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH

class Laser(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()

        self.speed = 5


    def shoot(self):
        print('SHOOT!')
        SHOOT_SOUND.play()

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            # lasers.append(self)
            self.kill()
            print("Deleted")
        
class Mob(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        

    def update(self):
        hit_list = pygame.sprite.spritecollide(self,lasers,True,pygame.sprite.collide_mask)
        print(len(hit_list))
        if len(hit_list) > 0:
            self.kill()

class Bomb():
    pass

class Fleet():
    def __init__(self,mobs):
        pass
    
    def move(self):
        pass
    
    def reverse(self):
        pass

    def move_down(self):
        pass

    def update(self):
        pass


# Game helper functions
def show_title_screen():
    title_text = FONT_XL.render("Space War!", 1, WHITE)
    screen.blit(title_text, [128, 204])

def show_stats(player):
    pass

def setup():
    global stage, done
    global player, ship, lasers, mobs
    
    ''' Make game objects '''
    ship = Ship(384,536,ship_img)
    # laser = Laser()

    ''' Make sprite groups '''
    player = pygame.sprite.GroupSingle()
    player.add(ship)

    lasers = pygame.sprite.Group()

    mob1 = Mob(100,100,enemy_img)
    mob2 = Mob(300,100,enemy_img)
    mob3 = Mob(500,100,enemy_img)

    mobs = pygame.sprite.Group()
    mobs.add(mob1,mob2,mob3)

    ''' set stage '''
    stage = START
    done = False

    
# Game loop
setup()

while not done:
    # Input handling (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if stage == START:
                if event.key == pygame.K_SPACE:
                    stage = PLAYING
        
            elif stage == PLAYING:
                if event.key == pygame.K_w:
                    ship.shoot()
                    
    ''' poll key states '''
    state = pygame.key.get_pressed()
    a = state[pygame.K_a]
    s = state[pygame.K_s]
    d = state[pygame.K_d]
    
    if stage == PLAYING:
        if a:
            ship.move_left()
        elif d:
            ship.move_right()
        else:
            block1_vx = 0
    
        if s:
            ship.shoot()

    # Game logic (Check for collisions, update points, etc.)

    player.update()
    lasers.update()
    mobs.update()

    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)
    lasers.draw(screen)
    player.draw(screen)
    mobs.draw(screen)

    if stage == START:
        show_title_screen()

        
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
