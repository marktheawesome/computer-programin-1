# Imports
import pygame

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
ship_img = pygame.image.load('assets/images/player.png').convert()


# Sounds
EXPLOSION = pygame.mixer.Sound('assets/sounds/explosion.ogg')


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

    def move_left(self):
        self.rect.x -=5
    
    def move_right(self):
        self.rect.x +=5

    def shoot(self):
        print('SHOOT!')

    def update(self):
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x + int(self.rect[2]) > WIDTH:
            self.rect.x = WIDTH - int(self.rect[2])





# Game helper functions
def show_title_screen():
    title_text = FONT_XL.render("Space War!", 1, WHITE)
    screen.blit(title_text, [128, 204])

def show_stats(player):
    pass

def setup():
    global stage, done, player, ship
    
    ''' Make game objects '''
    ship = Ship(384,536,ship_img)

    ''' Make sprite groups '''
    player = pygame.sprite.GroupSingle()
    player.add(ship)

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
    s = state[pygame.K_s]
    a = state[pygame.K_a]
    
    # Game logic (Check for collisions, update points, etc.)
    if stage == PLAYING:
        ''' set velocity for player 1 '''
        if a:
            ship.move_left()
        elif d:
            ship.move_right()
        else:
            block1_vx = 0

    ship.update()
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)
    player.draw(screen)

    
    if stage == START:
        show_title_screen()

        
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
