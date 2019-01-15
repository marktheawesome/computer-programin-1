# Imports
import pygame
import intersects
import random


# Initialize game engine
pygame.init()
check = 0 

# Window
X = 800  
Y = 600

SIZE = (X, Y)
TITLE = "Mickey Mouse Clubhouse"
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
GOLD = (255,215,0)

# Fonts
my_font = pygame.font.Font(None,50)

#Sounds
coin_sound = pygame.mixer.Sound("/home/mark/computer-programin-1/wall-collisions/coin_sound.ogg")

# Make a player
block =  [200, 150, 50, 50]
player = pygame.image.load('/home/mark/computer-programin-1/wall-collisions/mickey50x50.png')
block_vx = 0
block_vy = 0
block_speed = 5

# maze 
wall1 =  [300, 275, 200, 50]
wall2 =  [400, 450, 200, 50]
wall3 =  [100, 100, 50, 200]

walls = [wall1, wall2, wall3]
# make coins

coins = []
num_coins = 10 

while len(coins) < num_coins:
# for i in range(num_coins):
    check = 0
    local_s = 50
    local_x = random.randint(0,X)
    local_y = random.randint(0,Y)
    coin_temp = [local_x,local_y,local_s,local_s]
    for wall in walls:
        if not intersects.circle_rect(block,coin_temp):
            check +=1
        else:
            pass
    if check >= len(walls):
        coins.append(coin_temp)
    else:
        pass

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
        pygame.draw.line(screen, BLACK, [x, 0], [x, height], 1)
    for y in range(0, height, scale):
        pygame.draw.line(screen, BLACK, [0, y], [width, y])



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

    ''' detect coin colisions '''
    for coin in coins:
        if intersects.circle_rect(block, coin):
            print("Coin sound!")
            score += 1
            coin_sound.play()
            
    ''' remove collected coins '''
    coins = [coin for coin in coins if not intersects.circle_rect(block, coin)]

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

    ''' if the block is moved out of the window, nudge it back on. '''
    if block[1] < 0:
        block[1] = 0 
    elif block[1] + block[3] > Y:
        block[1] = Y - block[3]

    if block[0] > X - block[2]: block[0] = X - block[2]
    elif block[0] < 0: block[0] = 0 

          
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(WHITE)

    pygame.draw.rect(screen, WHITE, block)

    for coin in coins:
        # pygame.draw.rect(screen, GOLD, coin)
        pygame.draw.circle(screen, GOLD, [coin[0],coin[1]], 25)

    for w in walls:
        pygame.draw.rect(screen, RED, w)
    
    screen.blit(player,(block[0],block[1]))

    
    score_txt = my_font.render(str(score),1,RED)
    screen.blit(score_txt,[20,20])
    draw_grid(X,Y,50)


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()