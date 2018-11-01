# Imports
import pygame
import math
import time
import random

x = 1210
y = 720
r = 1 

# Initialize game engine
pygame.init()

#make objects
'''stars'''
num_stars = 400
stars = []
for i in range(num_stars):
    x2 = random.randrange(0,x)
    y2 = random.randrange(0,y)
    d = random.randrange(1,6)
    s = [x2,y2,d,d]
    stars.append(s)

#Random_usesfull_vars
def rect(screen,color,X1,Y1,X2,Y2):
    pygame.draw.rect(screen, color, [X1, Y1, X2, Y2])

def draw_stars():
    for s in stars:
        pygame.draw.ellipse(screen, WHITE,s)
def draw_cloud(x1, y1):
    pygame.draw.ellipse(screen, BLACK, [x1, y1 + 20, 40 , 40])
    pygame.draw.ellipse(screen, BLACK, [x1 + 60, y1 + 20, 40 , 40])
    pygame.draw.ellipse(screen, BLACK, [x1+ 20, y1 + 10, 25, 25])
    pygame.draw.ellipse(screen, BLACK, [x1+ 35, y1, 50, 50])
    pygame.draw.rect(screen, BLACK, [x1 + 20, y1 + 20, 60, 40])

def draw_fence(x1,y1):
    y = y1- 80
    x = 0 

    for x in range(5,x1,30):
        pygame.draw.polygon(screen, WHITE, [[x + 5,y],[x + 10,y + 5],[x + 10, y + 40],[x, y + 40], [x,y + 5]])
    
    pygame.draw.rect(screen,WHITE, [0,y+10,x1,5])
    pygame.draw.rect(screen,WHITE, [0,y+30,x1,5])

def draw_house():
    rect(screen, BROWN, 0+x*(1/3), y-40, 0+x*(1/3), -200)
    pygame.draw.polygon(screen, BLACK, [[0+x*(1/3), y-240], [x/2,y-400],[x*(2/3), y-240]])
    rect(screen, BLACK, 0+x*(3/6)-(0+x*(1/34)),y-40, 0+x*(1/17), -100)

def draw_grass():
    rect(screen, GREEN, 0, y, x, -40)

def draw_black_hole(z):
    pygame.draw.circle(screen, BLACK, [0,0], z)
    z+=1
# Window

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
    screen.fill(BLUE)
    draw_fence(1210,720)
    draw_grass()
    draw_house()
    
    draw_cloud(x/2, y/4)
    draw_cloud(x-x*(3/13), y/3)
    draw_cloud(x*(4/13), y/4)
    draw_stars()
    draw_black_hole(r)
    r+=1
    
    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()



    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)



# Close window and quit
pygame.quit()
