import pygame
import random

class Ball:
    def __init__(self, screen, color, time_sec, screen_width, screen_height):
        self.screen = screen
        self.color = color
        self.time_sec = time_sec

        self.speed_x = -screen_width / 1.28
        self.speed_y = -screen_height / 1.92

        self.radious = 9
        self.diameter = self.radious * 2

        self.x = random.randint(200, screen_width - self.radious)
        self.y = random.randint(200, screen_height - self.radious)
    def draw_circle(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radious)

    def move(self, time_sec):
        self.x += 2.5 * self.speed_x * time_sec
        self.y += 2.5 * self.speed_y * time_sec

        