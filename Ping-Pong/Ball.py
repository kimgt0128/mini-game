import pygame

class Ball:
    def __init__(self, screen, color, time_sec, screen_width, screen_height):
        self.screen = screen
        self.color = color
        self.time_sec = time_sec

        self.speed_x = -screen_width / 1.28
        self.speed_y = -screen_height / 1.92

        self.radious = 9
        self.diameter = self.radious * 2

        self.x = 400
        self.y = 300
    def draw_circle(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radious)

    def move(self):
        self.x += self.speed_x * self.time_sec
        self.y += self.speed_y * self.time_sec