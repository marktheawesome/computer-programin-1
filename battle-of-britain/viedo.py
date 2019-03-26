# pylint: disable-all
import os
import pygame
import settings

def init():
    global fileNames
    fileNames = []
    for filename in os.listdir('./assets/viedos/all_frames/'):

        fileNames.append('./assets/viedos/all_frames/' + filename)
    fileNames.sort()

    try:
        os.remove("order.txt")
    except:
        pass

    with open("order.txt", "a") as f:
        for Name in fileNames:
            f.write(Name + "\n")

global i
i = 1

def show_video():
    global fileNames, i
    if i  < len(fileNames):
        im = fileNames[i]

        im1 = pygame.image.load(im).convert()
        settings.SCREEN.blit(im1, [0, 0])

        i += 1
    else:
        settings.VIEDO_DONE = True
