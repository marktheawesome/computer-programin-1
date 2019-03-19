
import os
import pygame

os.chdir("./assets/viedos/all_frames/")
fileNames = []
for filename in os.listdir('.'):

    fileNames.append(filename)
fileNames.sort()



try:
    os.remove("order.txt")
except:
    pass
with open("order.txt", "a") as f:
    for Name in fileNames:
        f.write(Name + "\n")




WIDTH = 1280
HEIGHT = 720
SIZE = (WIDTH, HEIGHT)
TITLE = "Battle of Britain"
SCREEN = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

CLOCK = pygame.time.Clock()
REFRESH_RATE = 24
DONE = False
i = 1



'''
This is the game loop
'''
while not DONE:

    im = fileNames[i]

    im1 = pygame.image.load(im).convert()
    SCREEN.blit(im1, [0, 0])



    pygame.display.flip()
    CLOCK.tick(REFRESH_RATE)
    i += 1
