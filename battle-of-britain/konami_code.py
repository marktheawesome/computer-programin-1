# pylint: disable-all
# Imports
import pygame

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Sunny Day"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 30

up = 273
down = 274
left = 276
right = 275
b = 98
a = 97
enter = 13
index = 0

keys = []
code = [up, up, down, down, left, right, left, right, b, a, enter]
# Game loop
running = True

while running:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            keys.append(event.key)
            index += 1



    # Game logic
    if len(keys) <= len(code) and keys == code:
        print(keys)
        print('GG')

    elif keys[index-12:-1] == code:
        print(keys[index-12:-1])
        print("You did it.")


    # Drawing code

    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)
    # print(keys)

# Close window on quit
pygame.quit()