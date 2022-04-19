# import pygame package
import pygame
import sys
import random
from settings import Settings
from basket import Basket
import game_functions as gf


def run_game():
    WIDTH = 850
    HEIGHT = 600
    # initializing imported module
    pygame.init()
    ai_settings = Settings()
    #Making background image
    tree_bg = pygame.image.load('tree1.png')
    # displaying a window of height
    # 500 and width 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    basket = Basket(screen,ai_settings)
    pygame.display.set_caption("Blawesome Tree")

    # keep game running till running is true
    while True:
        #if basket.rect.left > WIDTH:
            #basket.rect.right = 0
        if basket.rect.left < 0:
            basket.rect.left = 0
        if basket.rect.right > WIDTH:
            basket.rect.right = WIDTH
        gf.check_events(basket)
        screen.blit(tree_bg,(0,0))
        basket.update()
        basket.blitme()
        pygame.display.update()
run_game()
