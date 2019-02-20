# Imports
import pygame
import intersects
import random

# Initialize game engine
pygame.init()
check = 0 

# Stages
START = 0
PLAYING = 1
END = 2
PAUSED = 3

# winning pic
win = pygame.image.load('pic/youwin.jpg')

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
my_font = pygame.font.Font("fonts/Precious.ttf",50)

#Sounds
coin_sound = pygame.mixer.Sound("sounds/coin_sound.ogg")

def setup():
    screen.fill(BLACK)
    global score
    score = 0
    # Make a player
    global block, vx, vy, block_speed, player, stage
    block =  [0, 0, 50, 50]
    player = pygame.image.load('pic/mickey50x50.png')
    vx = 0
    vy = 0
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
    global num_coins
    coins = []
    num_coins = 10 
    
    while len(coins) < num_coins:
        check = 0 
        local_s = 50

        local_x = random.randint(0,X)
        local_y = random.randint(0,Y)
        coin_temp = [local_x,local_y,local_s,local_s]
        coins.append(coin_temp)  
    stage = START
          


def show_start():
    text1 = my_font.render("maze", True, WHITE)
    text2 = my_font.render("(Press space to play.)", True, WHITE)
    w1 = text1.get_width()
    w2 = text2.get_width()
    screen.blit(text1, [X/2 - w1/2, 150])
    screen.blit(text2, [X/2 - w2/2, 200])

def show_end():
    screen.fill(BLACK)
    text1 = my_font.render("Good job!", True, WHITE)
    text2 = my_font.render("(Press space to restart.)", True, WHITE)
    w1 = text1.get_width()
    w2 = text2.get_width()
    screen.blit(text1, [X/2 - w1/2, 150])
    screen.blit(text2, [X/2 - w2/2, 200])

def show_pause():
    screen.fill(BLACK)
    text1 = my_font.render("Paused", True, WHITE)
    text2 = my_font.render("(Press p to restart.)", True, WHITE)
    w1 = text1.get_width()
    w2 = text2.get_width()
    screen.blit(text1, [X/2 - w1/2, 150])
    screen.blit(text2, [X/2 - w2/2, 200])

def play_field():
    
    pygame.mixer.music.stop()
    pygame.mixer.music.load("sounds/Deadpool OST - Angel of the morning.ogg")
    pygame.mixer.music.play(-1)

# Drawing functions
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


# Logic Funtions
def move_and_check_walls(block,walls):
    ''' move the block in horizontal direction '''
    block[0] += vx
    for wall in walls:
        if intersects.rect_rect(block,wall):
            if vx >0:
                block[0] = wall[0] - block[2]
            elif vx < 0:
                block[0] = wall[0] + wall[2]


    ''' move the block in horizontal direction '''
    block[1] += vy
    
    ''' resolve collisions with each wall '''
    for wall in walls:
        if intersects.rect_rect(block,wall):
            if vy >0:
                block[1] = wall[1] - block[3]
            elif vy < 0:
                block[1] = wall[1] + wall[3]


def check_screen_edges(player):
    ''' if the block is moved out of the window, nudge it back on. '''
    if player[1] < 0:
        player[1] = 0 
    elif player[1] + player[3] > Y:
        player[1] = Y - player[3]

    if player[0] > X - player[2]: player[0] = X - player[2]
    elif player[0] < 0: player[0] = 0

def process_coins(block):
    global score
    global coins
    for coin in coins:
        if intersects.rect_circle(block, coin):
            print("Coin sound!")
            score += 1
            coin_sound.play()
        
            
        ''' remove collected coins '''
        coins = [coin for coin in coins if not intersects.rect_circle(block, coin)]



play_field()

# Game loop
setup()
done = False

while not done:
    # Input handling (React to key presses, mouse clicks, etc.)
    ''' process events '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        elif event.type == pygame.KEYDOWN:
            if stage == START:
                if event.key == pygame.K_SPACE:
                    stage = PLAYING
                    
            elif stage == PLAYING:
                if event.key == pygame.K_LEFT:
                    vx -= 2
                elif event.key == pygame.K_RIGHT:
                    vx += 2
                elif event.key == pygame.K_UP:
                    vy -= 2
                elif event.key == pygame.K_DOWN:
                    vy += 2
                elif event.key == pygame.K_p:
                    stage = PAUSED
                    

            elif stage == END:
                if event.key == pygame.K_SPACE:
                    setup()       

            elif stage == PAUSED:
                if event.key == pygame.K_p:
                    stage = PLAYING
    # Game logic (Check for collisions, update points, etc.)
    process_coins(block)
    move_and_check_walls(block,walls)
    check_screen_edges(block)

    ''' change game to end'''
    if score == num_coins:
        stage = END

    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    if stage == PLAYING:
        screen.fill(WHITE)
        draw_coins()      
        draw_walls(BLACK) 
        draw_player(player) 
        draw_score(score)

    elif stage == START:
        show_start()
    elif stage == END:
        show_end()
    elif stage == PAUSED:
        show_pause()

    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)

# Close window and quit
pygame.quit()