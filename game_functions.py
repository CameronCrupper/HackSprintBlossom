import sys
import pygame

def check_events(basket):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #move right
                basket.moving_right = True
            if event.key == pygame.K_LEFT:
                #move left
                basket.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                basket.moving_right = False
            if event.key == pygame.K_LEFT:
                basket.moving_left = False
    #responds to keyboard and mouse
    # Check for event if user has pushed
    # any event in queue
    #for event in pygame.event.get():
        # if event is of type quit then
        # set running bool to false
        #if event.type == pygame.QUIT:
            #sys.exit()
        #elif event.type == pygame.KEYDOWN:
            #if event.key == pygame.K_RIGHT:
                #move right
                #basket.moving_right = True
        #elif event.type == pygame.KEYUP:
            #if event.key == pygame.K_RIGHT:
                #basket.moving_right = False
