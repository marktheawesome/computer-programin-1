# Imports
import pygame
import math

# Initialize game engine
pygame.init()

#Random_usesfull_vars
def rect(screen,color,X1,Y1,X2,Y2):
    pygame.draw.rect(screen, color, [X1, Y1, X2, Y2])


def draw_cloud(x1, y1):
    pygame.draw.ellipse(screen, WHITE, [x1, y1 + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x1 + 60, y1 + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x1+ 20, y1 + 10, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [x1+ 35, y1, 50, 50])
    pygame.draw.rect(screen, WHITE, [x1 + 20, y1 + 20, 60, 40])

# Window
x = 1210
y = 720

SIZE = (x, y)
TITLE = "My Awesome Picture"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125 , 0)
SKY_BLUE = (135, 206, 235)    
BROWN = (139,69,19)
YELLOW =(255,255,0)
GRAY = (211,211,211)
BLACK = (0,0,0)

# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # Game logic (Check for collisions, update points, etc.)
    ''' leave this section alone for now ''' 

    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(SKY_BLUE)
    rect(screen, GREEN, 0, y, x, -40)
    rect(screen, BROWN, 0+x*(1/3), y-40, 0+x*(1/3), -200)
    pygame.draw.polygon(screen, BLACK, [[0+x*(1/3), y-240], [x/2,y-400],[x*(2/3), y-240]])
    pygame.draw.circle(screen, YELLOW, [0,0], 200)
    rect(screen, BLACK, 0+x*(3/6)-(0+x*(1/34)),y-40, 0+x*(1/17), -100)
    draw_cloud(x/2, y/4)
    draw_cloud(x-x*(3/13), y/3)
    draw_cloud(x*(4/13), y/4)
 
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()



    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
