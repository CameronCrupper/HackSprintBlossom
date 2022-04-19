# import pygame package
import pygame
import sys
import random
from settings import Settings
from basket import Basket
from Fruit import Fruit
from Blossom import Blossom
import game_functions as gf


def run_game():
    WIDTH = 850
    HEIGHT = 600
    # initializing imported module
    pygame.init()
    ai_settings = Settings()
    clock = pygame.time.Clock()
    #Making background image
    tree_bg = pygame.image.load('tree1.png')
    # displaying a window of height
    # 500 and width 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    basket = Basket(screen,ai_settings)
    pygame.display.set_caption("Blawesome Tree")

    fruitList = pygame.sprite.Group()
    blossomList = pygame.sprite.Group()
    for x in range(0, 10):
        blawesomFruit = Fruit(15, 15)
        fruitList.add(blawesomFruit)
        for i in range(0, 3):
            blawBlossom = Blossom(blawesomFruit)
            blossomList.add(blawBlossom)


    # keep game running till running is true
    while True:
        #if basket.rect.left > WIDTH:
            #basket.rect.right = 0
        if basket.rect.left < 0:
            basket.rect.left = 0
        if basket.rect.right > WIDTH:
            basket.rect.right = WIDTH
        currentTime = pygame.time.get_ticks()
        gf.check_events(basket)
        screen.blit(tree_bg,(0,0))
        fruitList.draw(screen)
        blossomList.draw(screen)
        fruitList.update()
        for blossom in blossomList:
            blossom.update(currentTime)
        basket.update()
        basket.blitme()
        pygame.display.update()
        clock.tick(60)
        
        print(currentTime)
run_game()
