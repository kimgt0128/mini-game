import pygame

class Bar:
    def __init__(self, screen, screen_height, color, position_y):
        self.screen = screen
        self.screen_height = screen_height
        self.positions =  [0, position_y]
        self.width = 9
        self.height = 50
        self.color = color
        self.direction = 0
        
    def draw_block(self):
        siz = (self.width, self.height)

        pygame.draw.rect(self.screen, self.color, (self.positions, siz)) 

    def move(self):
        self.positions[1] += self.direction
        if self.positions[1] + self.height >= self.screen_height:
            self.positions[1] = self.screen_height - self.height
        elif self.positions[1] <= 0:
            self.positions[1] = 0
    
        