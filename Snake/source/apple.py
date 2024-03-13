import pygame
from function import draw_block


class Apple:
    def __init__(self, screen, color, position=(5, 5)):
        self.position = position
        self.screen = screen
        self.color = color
    def draw(self):
        draw_block(self.screen, self.color, self.position)

