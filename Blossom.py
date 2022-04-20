import pygame
import sys
import random


carrot = pygame.image.load('carrot.png')
leaf = pygame.image.load('leaf1.png')

class Blossom(pygame.sprite.Sprite):
    def __init__(self, fruit):
        super().__init__()
        self.width = fruit.width
        self.height = fruit.height
        self.image = leaf
        # self.image.fill(fruit.color)
        self.speed = random.randrange(1, 3)
        self.updateTime = random.randrange(0, 30000)
        self.rect = self.image.get_rect()
        self.rect.x = fruit.rect.x - 10
        self.rect.y = fruit.rect.y

    def update(self, currentTime):
        # only drops fruit at random intervals
        if currentTime > self.updateTime:
            self.image = carrot
            # pygame.transform.scale(carrot, (40, 40), dest_surface=self.image)
            self.rect.y = self.rect.y + self.speed
