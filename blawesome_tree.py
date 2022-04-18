# import pygame package
import pygame
import sys
import random
from settings import Settings
from basket import Basket


def run_game():
    # initializing imported module
    pygame.init()

    ai_settings = Settings()

    # displaying a window of height
    # 500 and width 400
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    basket = Basket(screen)
    pygame.display.set_caption("Blawesome Tree")

    #Making background image
    tree_bg = pygame.image.load('tree1.png')

    #sky background
    #sky_blue = (135,206,235)

    #display_surface.fill(sky_blue)

    #pygame.Surface.set_colorkey (image, [255,255,255])
    #pygame.Surface.set_colorkey (image, [128,128,128])

    #displaying tree to background
    screen.blit(tree_bg,(0,0))

    #update display
    pygame.display.flip()

    # keep game running till running is true
    while True:

        # Check for event if user has pushed
        # any event in queue
        for event in pygame.event.get():

            # if event is of type quit then
            # set running bool to false
            if event.type == pygame.QUIT:
                sys.exit()
        basket.blitme()
        pygame.display.flip()
run_game()
