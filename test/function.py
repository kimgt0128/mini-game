import pygame


#posion = [10, 20]
def draw_block(screen, color, position):
    block = pygame.Rect((position[0] * 20, position[1] * 20), (20, 20))
    pygame.draw.rect(screen, color, block)


