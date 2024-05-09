import pygame
from datetime import datetime
from datetime import timedelta

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

size = [800, 600]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()
last_moved_time = datetime.now()

game_start_time = pygame.time.get_ticks()


KEY_DIRECTION = {
    pygame.K_w: 'N',
    pygame.K_s: 'S',
    pygame.K_a: "W",
    pygame.K_d: "E"
}