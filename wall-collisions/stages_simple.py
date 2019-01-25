# Imports
import pygame

# Initialize game engine
pygame.init()

# Window
WIDTH = 800
HEIGHT = 600
TITLE = "Game Stages Demo"
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Stages
START = 0
PLAYING = 1
END = 2
PAUSED = 3

# Fonts
MY_FONT = pygame.font.Font("/home/mark/computer-programin-1/wall-collisions/fonts/Precious.ttf",50)

def setup():
    global block, vx, vy, stage
    
    ''' make block '''
    block = [375, 275, 50, 50]
    vx = 0
    vy = 0

    ''' set stage '''
    stage = START
    
def show_start():
    text1 = MY_FONT.render("Block", True, WHITE)
    text2 = MY_FONT.render("(Press space to play.)", True, WHITE)
    w1 = text1.get_width()
    w2 = text2.get_width()
    screen.blit(text1, [WIDTH/2 - w1/2, 150])
    screen.blit(text2, [WIDTH/2 - w2/2, 200])

def show_end():
    text1 = MY_FONT.render("Game Over", True, WHITE)
    text2 = MY_FONT.render("(Press space to restart.)", True, WHITE)
    w1 = text1.get_width()
    w2 = text2.get_width()
    screen.blit(text1, [WIDTH/2 - w1/2, 150])
    screen.blit(text2, [WIDTH/2 - w2/2, 200])

def show_pause():
    text1 = MY_FONT.render("Paused", True, WHITE)
    text2 = MY_FONT.render("(Press p to restart.)", True, WHITE)
    w1 = text1.get_width()
    w2 = text2.get_width()
    screen.blit(text1, [WIDTH/2 - w1/2, 150])
    screen.blit(text2, [WIDTH/2 - w2/2, 200])


# Game loop
setup()
done = False

while not done:
    # Event processing
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
            
    # Game logic
    if stage == PLAYING:
        ''' move block '''
        block[0] += vx
        block[1] += vy

        ''' end game on edge collision '''
        if block[0] < 0 or block[0] > WIDTH - block[2] or \
           block[1] < 0 or block[1] > HEIGHT - block[3]:
            stage = END
     
    # Drawing code
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, block) 

    if stage == START:
        show_start()
    elif stage == END:
        show_end()
    elif stage == PAUSED:
        show_pause()
        
    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)


# Close window on quit
pygame.quit()
