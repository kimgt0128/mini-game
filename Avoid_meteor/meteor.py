import pygame
import random

class Meteor(pygame.sprite.Sprite):
    def __init__(self, image_path, size):
        super().__init__()
        #self.image = pygame.image.load('./object_images/meteor.png')
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.left = random.randint(0, 600)
        self.rect.top = -100
        self.dy = random.randint(3, 9)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.top += self.dy
        if self.rect.top > 800:
            self.rect.left = random.randint(0, 600)
            self.rect.top = -100
            self.dy = random.randint(3, 9)
