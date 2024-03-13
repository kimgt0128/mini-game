import pygame

size = [600, 800]

class Plane(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./object_images/airplane.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.left = 250
        self.rect.top = 700
        self.dy = 0
        self.dx = 0
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.top += self.dy
        self.rect.left += self.dx
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > size[0]:
            self.rect.right = size[0]
        elif self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > size[1]:
            self.rect.bottom = size[1] 
