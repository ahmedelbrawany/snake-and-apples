import pygame
import time
import random



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

#-----------------clock and font-----------------------
clock = pygame.time.Clock()
FPS = 30
font = pygame.font.SysFont(None, 25)
#------------------ game loop ----------------------



def message_display(msg, x,y,color):
    screen_txt = font.render(msg, True, color)
    game_display.blit(screen_txt, [x,y])



def get_apple_coordinates(apple_w, apple_h):
    x = random.randrange(0, WINDOW_SIZE[0] / 2 - apple_w)
    y = random.randrange(0, WINDOW_SIZE[1] / 2 - apple_h)
    return (x, y)

def game_loop():
    exit_game = False
    game_over = False
    head_x = WINDOW_SIZE[0] /2
    head_y = WINDOW_SIZE[1] /2

    x_movement = 0
    y_movement = 0

    movement = 2
    snake_w = 10
    snake_h = 10
    apple_w = 10
    apple_h = 10

    apple_x, apple_y = get_apple_coordinates(apple_w, apple_h)

    while not exit_game:

        while game_over:
            game_display.fill(WHITE)
            message_display("Game Over",WINDOW_SIZE[0] / 2 - 30, WINDOW_SIZE[1] / 2-30, RED)
            message_display("if you want to play again click S, to quit click q",WINDOW_SIZE[0] / 2 - 180, WINDOW_SIZE[1] / 2 , BLUE)
            pygame.display.update()
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    exit_game = True
                    game_over = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        exit_game = True
                        game_over = False

                    if event.key == pygame.K_s:
                        game_loop()



        #--------------------- event handling -----------------------
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                exit_game = 1
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if x_movement <= 0:
                        x_movement = -movement
                        y_movement = 0

                elif event.key == pygame.K_RIGHT:
                    if x_movement >= 0:
                        x_movement= movement
                        y_movement = 0

                elif event.key == pygame.K_UP:
                    if y_movement <= 0:
                        y_movement = -movement
                        x_movement = 0

                elif event.key == pygame.K_DOWN:
                    if y_movement >= 0 :
                        y_movement = movement
                        x_movement = 0

            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            #         x_movement = 0
            #
            #     if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            #         y_movement = 0


        head_x += x_movement
        if head_x  > WINDOW_SIZE[0]-snake_w/2:
            head_x = 0
            game_over = True

        if head_x < 0-snake_w/2:
            head_x = WINDOW_SIZE[0]-snake_w/2

        head_y += y_movement
        if head_y > WINDOW_SIZE[1]-snake_w/2:
            head_y = 0

        if head_y < 0-snake_w/2:
            head_y = WINDOW_SIZE[1]-snake_w/2

        #filling the whole game display with the color blue
        game_display.fill(LIGHTBLUE)
        #---------------------- drawing rectangles -----------------------
        #drawing rectangles using draw
        pygame.draw.rect(game_display, RED, [apple_x, apple_y, apple_w, apple_h])
        pygame.draw.rect(game_display, BLACK, [head_x,head_y, snake_w, snake_h])
        #drawing rectangles using fill (this is much faster for graphics)
        #game_display.fill(RED, rect=[400,300, 10,10])

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()

game_loop()