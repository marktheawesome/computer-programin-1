# Imports
import pygame
import math
import time
import random

x = 1210
y = 720
r = 1 
num = 0 

growning = True


# Initialize game engine
pygame.init()

#make objects
'''stars'''
num_stars = 800
stars = []
for i in range(num_stars):
    x2 = random.randrange(0,x)
    y2 = random.randrange(-y,y)
    d = random.randrange(1,6)
    s = [x2,y2,d,d]
    stars.append(s)

'''clouds'''
num_clouds = 10
clouds = []
for i in range (num_clouds):
    x3 = random.randrange(0,2*x)
    y3 = random.randrange(0,math.ceil((y/3)))
    c = [x3,y3]
    clouds.append(c)

#Random_usesfull_vars

def rect(screen,color,X1,Y1,X2,Y2):
    pygame.draw.rect(screen, color, [X1, Y1, X2, Y2])

def draw_stars():
    for s in stars:
        pygame.draw.ellipse(screen, WHITE,s)

def draw_cloud(loc,cloud_color):
    

    x1 = loc[0]
    y1 = loc[1]

    pygame.draw.ellipse(screen, cloud_color, [x1, y1 + 20, 40 , 40])
    pygame.draw.ellipse(screen, cloud_color, [x1 + 60, y1 + 20, 40 , 40])
    pygame.draw.ellipse(screen, cloud_color, [x1+ 20, y1 + 10, 25, 25])
    pygame.draw.ellipse(screen, cloud_color, [x1+ 35, y1, 50, 50])
    pygame.draw.rect(screen, cloud_color, [x1 + 20, y1 + 20, 60, 40])

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

def draw_black_hole(z,colour):
    pygame.draw.circle(screen, colour, [0,0], z)
    
def person(num,person_color):
    x4 = num + 400 
    y4 = 550 

    pygame.draw.line(screen,person_color,[x4, y4], [x4,y4+100], 10)#Mid of person
    pygame.draw.line(screen,person_color,[x4,y4+100],[x4+30,y4+150],10)#Right leg of Person
    pygame.draw.line(screen,person_color,[x4,y4+100],[x4-30,y4+150],10)#Left leg of Person
    pygame.draw.line(screen,person_color,[x4,y4+20],[x4-30 ,y4+80],10)#Left arm of Person
    pygame.draw.line(screen,person_color,[x4,y4+20],[x4+30,y4+80],10)#Right arm of Person
    pygame.draw.ellipse(screen, person_color, [x4-50,y4-90,100,100])#Head
    

def snow():
    rect(screen, WHITE, 0, y, x, -40)
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

colors = [RED,GREEN,BLUE,WHITE,BLACK,ORANGE,SKY_BLUE,BROWN,YELLOW,GRAY,BLACK]

colour1 = RED
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
    for c in clouds:
        c[0]+= 1

        if c[0] > x + 100:
            c[0] = random.randrange(-x,-100)
            c[1] = random.randrange(0,math.ceil(y/3))

    for s in stars:
        s[1]+= 1

        if s[1] > y:
            s[0] = random.randrange(0,x)
            s[1] = random.randrange(-y,0)
  
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    
    
    screen.fill(BLUE)

    draw_fence(1210,720)
    draw_grass()
    draw_house()
    person(num,GRAY)

    for c in clouds:
        draw_cloud(c , BLACK)
            
    draw_stars()
    draw_black_hole(r,colour1)

    if growning:
        r +=1
        if r >=500:
            growning = False

    elif not growning:
        
        r -= 1 

        if r == 2:
            r +=1
            growning = True
            colour1 = random.choice(colors)
            
    snow()
            

    num+=1
    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()



    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)



# Close window and quit
pygame.quit()

