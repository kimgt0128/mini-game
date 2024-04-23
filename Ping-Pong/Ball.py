import pygame

class Ball:
    def __init__(self, screen, color, tick):
        self.screen = screen
        self.color = color
        self.time_sec = tick / 1000.0
        self.x = 400
        self.y = 300

        self.radious = 9
        self.diameter = self.radious * 2

    def draw_circle(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radious)