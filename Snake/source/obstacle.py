import pygame
import random
from function import draw_block


class Obstacle():
    def __init__(self, screen, color, size, snake_positions, apple_position):
        self.screen = screen
        self.size = size
        self.color = color
        self.snake_position = snake_positions
        self.apple_position = apple_position
        self.positions = []
        self.position = self.reset()


    def reset(self):
        return (random.randint(0, 20), random.randint(0, 20))

    def  draw(self):
        #예외처리 나중에 할거임
        draw_block(self.screen, self.color, self.position)