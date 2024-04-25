import pygame
import random
from function import draw_block


class Apple:
    def __init__(self, screen, color):
        self.position = self.reset()
        self.screen = screen
        self.color = color

    def reset(self):
        return (random.randint(0, 20), random.randint(0, 20)) 

    def draw(self):
        draw_block(self.screen, self.color, self.position)

