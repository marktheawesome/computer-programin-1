# Imports
import pygame
import intersects
import random


# Initialize game engine
pygame.init()
check = 0 

# winning pic
win = pygame.image.load('/home/mark/computer-programin-1/wall-collisions/youwin.jpg')
# Window
global X
global Y
X = 900  
Y = 700

SIZE = (X, Y)
TITLE = "Mickey Mouse Clubhouse"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
global Black 
global GOLD
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255,0,0)
GOLD = (255,215,0)

# Fonts
my_font = pygame.font.Font("/home/mark/computer-programin-1/wall-collisions/fonts/Precious.ttf",50)

#Sounds
coin_sound = pygame.mixer.Sound("/home/mark/computer-programin-1/wall-collisions/coin_sound.ogg")

# Make a player
block =  [0, 0, 50, 50]
player = pygame.image.load('/home/mark/computer-programin-1/wall-collisions/mickey50x50.png')
block_vx = 0
block_vy = 0
block_speed = 5

# walls
global walls 
wall1 =  [300, 275, 200, 50]
wall2 =  [400, 450, 200, 50]
wall3 =  [100, 100, 50, 200]
wall4 =  [200, 100, 50, 200]
wall5 =  [300, 100, 50, 70]
wall6 =  [400, 100, 50, 70]
wall7 =  [500, 100, 50, 200]
wall8 =  [600, 100, 50, 200]
wall9 =  [100, 500, 300, 60]
wall10 = [700, 300, 100, 60]

walls = [wall1, wall2, wall3,wall4,wall5,wall6,wall7,wall8,wall9,wall10]

# make coins
global coins
coins = []
num_coins = 10 

while len(coins) < num_coins:
    check = 0 
    local_s = 50
    local_x = random.randint(0,X)
    local_y = random.randint(0,Y)
    coin_temp = [local_x,local_y,local_s,local_s]
    # for wall in walls:
        # if intersects.rect_circle(wall,coin_temp):
        # if intersects.rect_rect(wall,coin_temp):
        #     check +=1
        # else:
        #     pass
    
    # if check == len(walls):
    coins.append(coin_temp)
    # else:
    #     pass

# Game statistics
score = 0
gg = False


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


def play_field():
    
    pygame.mixer.music.stop()
    pygame.mixer.music.load("/home/mark/computer-programin-1/wall-collisions/Deadpool OST - Angel of the morning.ogg")
    pygame.mixer.music.play(-1)


def draw_walls(BLACK):
    for w in walls:
         pygame.draw.rect(screen, BLACK, w)

def draw_coins():
    for coin in coins:
        pygame.draw.circle(screen, GOLD, [coin[0],coin[1]], 25)

def draw_score(score):
    score_txt = my_font.render(str(score),1,RED)
    screen.blit(score_txt,[20,20])

def draw_player(player):
    screen.blit(player,(block[0],block[1]))

def keep_in():
    ''' if the block is moved out of the window, nudge it back on. '''
    if block[1] < 0:
        block[1] = 0 
    elif block[1] + block[3] > Y:
        block[1] = Y - block[3]

    if block[0] > X - block[2]: block[0] = X - block[2]
    elif block[0] < 0: block[0] = 0 
play_field()
# Game loop
done = False

while not done:
    # Input handling (React to key presses, mouse clicks, etc.)
    ''' process events '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if gg != True:                
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

        if score == num_coins:
            gg = True
        
        ''' move the block in horizontal direction '''
        block[0] += block_vx
        ''' detect coin colisions '''
        for coin in coins:
            if intersects.rect_circle(block, coin):
                print("Coin sound!")
                score += 1
                coin_sound.play()
                
        ''' remove collected coins '''
        coins = [coin for coin in coins if not intersects.rect_circle(block, coin)]

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

        keep_in()    
        # Drawing code (Describe the picture. It isn't actually drawn yet.)
        screen.fill(WHITE)
        draw_coins()      
        draw_walls(BLACK) 
        draw_player(player) 
        draw_score(score)

        # Update screen (Actually draw the picture in the window.)
        pygame.display.flip()


        # Limit refresh rate of game loop 
        clock.tick(refresh_rate)
    
    else:
        screen.blit(win,(0,0))
        pygame.display.flip()
        clock.tick(refresh_rate)
        
        # pygame.quit()
        print("Congraulations you best this game onto the next one!")


# Close window and quit
pygame.quit()