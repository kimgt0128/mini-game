import pygame
from function import draw_block

class Snake:
    def __init__(self, screen, color):
        self.positions = [(0,2),(0,1),(0,0)]  # 뱀의 위치
        self.direction = ''
        self.screen = screen
        self.color = color
 
    def draw(self):
        head_position = self.positions[0]
        for position in self.positions:
            if position[0] == head_position[0] and position[1] == head_position[1]:
                draw_block(self.screen, (255, 207, 64), position)
            else:
                draw_block(self.screen, self.color, position)
 
    def move(self):
        head_position = self.positions[0]
        y, x = head_position
        if self.direction == 'N':
            self.positions = [(y - 1, x)] + self.positions[:-1]
        elif self.direction == 'S':
            self.positions = [(y + 1, x)] + self.positions[:-1]
        elif self.direction == 'W':
            self.positions = [(y, x - 1)] + self.positions[:-1]
        elif self.direction == 'E':
            self.positions = [(y, x + 1)] + self.positions[:-1]
 
    def grow(self):
        tail_position = self.positions[-1]
        y, x = tail_position
        if self.direction == 'N':
            self.positions.append((y - 1, x))
        elif self.direction == 'S':
            self.positions.append((y + 1, x))
        elif self.direction == 'W':
            self.positions.append((y, x - 1))
        elif self.direction == 'E':
            self.positions.append((y, x + 1)) 