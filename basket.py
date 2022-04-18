import pygame
class Basket():

    def __init__(self,screen):
        #make basket and location
        self.screen = screen

        #load bmp and get rectangle
        self.image = pygame.image.load('IMG/basket.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #puts basket on bottom of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        #put basket at specific location
        self.screen.blit(self.image, self.rect)
