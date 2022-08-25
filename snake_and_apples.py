import pygame
from pygame.locals import *


#-------------- initialize pygame parameters
pygame.init()

#-------------colors--------------
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
LIGHTBLUE = (173,216,230)
#---------------- set title for the window -------------
pygame.display.set_caption('Snake and Apples')

#----------------- define game display-------------------
WINDOW_SIZE = (800,600)

game_display = pygame.display.set_mode(WINDOW_SIZE, 0, 32)


#------------------ game loop ----------------------
exit_game = 0
head_x = 300
head_y = 300

x_movement = 0
y_movement = 0

clock = pygame.time.Clock()
FPS = 30
while not exit_game:
    #--------------------- event handling -----------------------
    for event in pygame.event.get():
        print(event)
        if event.type == QUIT:
            exit_game = 1
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_movement = -2
                y_movement = 0

            if event.key == pygame.K_RIGHT:
                x_movement= 2
                y_movement = 0

            if event.key == pygame.K_UP:
                y_movement = -2
                x_movement = 0

            if event.key == pygame.K_DOWN:
                y_movement = 2
                x_movement = 0

        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        #         x_movement = 0
        #
        #     if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        #         y_movement = 0


    head_x += x_movement
    if head_x > 800:
        head_x = 0

    if head_x < 0:
        head_x = 800

    head_y += y_movement
    if head_y > 600:
        head_y = 0

    if head_y < 0:
        head_y = 600

    #filling the whole game display with the color blue
    game_display.fill(LIGHTBLUE)
    #---------------------- drawing rectangles -----------------------
    #drawing rectangles using draw
    pygame.draw.rect(game_display, BLACK, [head_x,head_y, 10, 10])
    #drawing rectangles using fill (this is much faster for graphics)
    game_display.fill(RED, rect=[400,300, 10,10])

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit()