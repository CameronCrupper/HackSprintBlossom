import pygame
from settings import Settings
class Basket():

    def __init__(self, screen, ai_settings):
        #make basket and location
        self.screen = screen
        #self.Settings = ai_settings
        

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
        #put basket at specific location
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right:
            self.rect.centerx +=1
        if self.moving_left:
            self.rect.centerx -=1

