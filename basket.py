from re import X
import pygame
#from settings import Settings
from Blossom import Blossom
class Basket(pygame.sprite.Sprite):

    def __init__(self, screen):
        super().__init__()
        #make basket and location
        
        self.screen = screen


        #load bmp and get rectangle
        self.image = pygame.image.load('IMG/basket.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #puts basket on bottom of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False
  
        #if self.rect.right > screen.get_rect().right:
            #self.rect.right = screen.get_rect().right
        #if self.rect.left > screen.get_rect().left:
            #self.rect.left = screen.get_rect().left
        
    def blitme(self):
        #RED = (255,0,0)
        #put basket at specific location
        self.screen.blit(self.image, self.rect)
        #pygame.draw.rect(self.screen, RED, self.rect, 1)

    def update(self):
        if self.moving_right:
            self.rect.centerx +=5
        if self.moving_left:
            self.rect.centerx -=5
        

