# Imports
import pygame
import intersects
import random


# Initialize game engine
pygame.init()


# Window
X = 600  
Y = 600

SIZE = (X, Y)
TITLE = "Collect Coins"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255,0,0)

# Fonts
my_font = pygame.font.Font(None,50)

#Sounds
coin_sound = pygame.mixer.Sound("/home/mark/computer-programin-1/wall-collisions/coin_sound.ogg")

# Make a player
block =  [200, 150, 50, 50]
block_vx = 0
block_vy = 0
block_speed = 5

# make coins
coins = []
num_coins = 5 

for i in range(num_coins):
    local_s = 50
    local_x = random.randint(0,X)
    local_y = random.randint(0,Y)
    coin_temp = [local_x,local_y,local_s,local_s]
    coins.append(coin_temp)

# Walls
wall1 =  [0, Y, -1, 0]
wall2 =  [400, 450, 200, 50]
wall3 =  [100, 100, 50, 200]

walls = [wall1, wall2, wall3]
# Game statistics
score = 0

#Grid
def draw_grid(width, height, scale):
    '''
    Draws a grid that can overlay your picture.
    This should make it easier to figure out coordinates
    when drawing pictures.
    '''
    for x in range(0, width, scale):
        pygame.draw.line(screen, WHITE, [x, 0], [x, height], 1)
    for y in range(0, height, scale):
        pygame.draw.line(screen, WHITE, [0, y], [width, y])

# Game loop
done = False

while not done:
    # Input handling (React to key presses, mouse clicks, etc.)
    ''' process events '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            

    ''' poll key states '''
    state = pygame.key.get_pressed()

    up = state[pygame.K_UP]
    down = state[pygame.K_DOWN]
    left = state[pygame.K_LEFT]
    right = state[pygame.K_RIGHT]

    if up:
        block_vy = -block_speed
    elif down:
        block_vy = block_speed
    else:
        block_vy = 0
        
    if left:
        block_vx = -block_speed
    elif right:
        block_vx = block_speed
    else:
        block_vx = 0

        
    # Game logic (Check for collisions, update points, etc.)
    ''' move the block in horizontal direction '''
    block[0] += block_vx

    ''' resolve collisions with each wall'''
    for wall in walls:
        if intersects.rect_rect(block,wall):
            if block_vx >0:
                block[0] = wall[0] - block[2]
            elif block_vx < 0:
                block[0] = wall[0] + wall[2]


    ''' move the block in horizontal direction '''
    block[1] += block_vy
    
    ''' resolve collisions with each wall '''
    for wall in walls:
        if intersects.rect_rect(block,wall):
            if block_vy >0:
                block[1] = wall[1] - block[3]
            elif block_vy < 0:
                block[1] = wall[1] + wall[3]
    
    ''' detect coin colisions '''
    for coin in coins:
        if intersects.rect_rect(block, coin):
            print("Coin sound!")
            score += 1
            coin_sound.play()
            
    ''' remove collected coins '''
    coins = [coin for coin in coins if not intersects.rect_rect(block, coin)]


          
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, block)

    for coin in coins:
        pygame.draw.rect(screen, YELLOW, coin)
    
    for w in walls:
        pygame.draw.rect(screen, RED, w)

    
    score_txt = my_font.render(str(score),1,RED)
    screen.blit(score_txt,[20,20])
    draw_grid(X,Y,50)


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
