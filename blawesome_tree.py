# import pygame package
import pygame
import sys
import random

# initializing imported module
pygame.init()

# displaying a window of height
# 500 and width 400
display_surface = pygame.display.set_mode((850, 600))

#Making background image
image = pygame.image.load('tree1.png')

#sky background
sky_blue = (135,206,235)

display_surface.fill(sky_blue)

pygame.Surface.set_colorkey (image, [255,255,255])
#pygame.Surface.set_colorkey (image, [128,128,128])

#displaying tree to background
display_surface.blit(image,(0,0))

#update display
pygame.display.flip()

# creating a bool value which checks
# if game is running
running = True

# keep game running till running is true
while running:

    # Check for event if user has pushed
    # any event in queue
    for event in pygame.event.get():

        # if event is of type quit then
        # set running bool to false
        if event.type == pygame.QUIT:
            running = False
