import pygame
import random
import math
# Initialize game engine
pygame.init()
# useful vars
night = False
# Window
x = 800
y = 600
SIZE = (x, y)
TITLE = "Sunny Day"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 30


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

'''rain'''
num_of_rain_drops = 1000
rain_drops = []
for i in range(num_of_rain_drops):
    x2 = random.randrange(0,x)
    y2 = random.randrange(-y,y)
    d = random.randrange(1,6)
    r = [x2,y2,d,d]
    rain_drops.append(r)

'''clouds'''
num_clouds = 10
clouds = []
for i in range (num_clouds):
    x3 = random.randrange(0,2*x)
    y3 = random.randrange(0,math.ceil((y/3)))
    c = [x3,y3]
    clouds.append(c)

def draw_cloud(loc,cloud_color):
    

    x1 = loc[0]
    y1 = loc[1]

    pygame.draw.ellipse(screen, cloud_color, [x1, y1 + 20, 40 , 40])
    pygame.draw.ellipse(screen, cloud_color, [x1 + 60, y1 + 20, 40 , 40])
    pygame.draw.ellipse(screen, cloud_color, [x1+ 20, y1 + 10, 25, 25])
    pygame.draw.ellipse(screen, cloud_color, [x1+ 35, y1, 50, 50])
    pygame.draw.rect(screen, cloud_color, [x1 + 20, y1 + 20, 60, 40])

def draw_rain():
    for r in rain_drops:
        pygame.draw.ellipse(screen, BLUE,r)

def update_clounds():
    for c in clouds:
        c[0]+= 1

        if c[0] > x + 100:
            c[0] = random.randrange(-x,-100)
            c[1] = random.randrange(0,math.ceil(y/3))
def update_rain():
    for r in rain_drops:
        r[1]+= 2

        if r[1] > y:
            r[0] = random.randrange(0,x)
            r[1] = random.randrange(-y,0)
     
def drawing_clounds():
    for c in clouds:
        draw_cloud(c , WHITE)

def draw_sun():
    pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])

def draw_grass():
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])
def draw_black():
    pygame.draw.rect(screen, BLACK,[0, 600, 800, -600 ])


# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                night = not night 

    if not night:
        '''Clouds'''
        update_clounds()

        '''rain'''
        update_rain()
        # Game logic

        # Drawing code
        ''' sky '''
        screen.fill(SKY_BLUE)


        '''clouds'''
        drawing_clounds()

        
        ''' sun '''
        draw_sun()


        ''' grass '''
        draw_grass()
        

        draw_rain()

        
    elif  night:
        draw_black()
    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)
# Close window on quit
pygame.quit()
