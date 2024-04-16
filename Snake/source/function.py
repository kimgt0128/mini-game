import pygame

def draw_block(screen, color, position):
    block = pygame.Rect((position[1] * 20, position[0] * 20),
                        (20, 20))
    pygame.draw.rect(screen, color, block)


def isIn(position, size):
    if position[0] > size[1] or position[0] < 0 or position[1] > size[0] or position[1] < 0:
        return True
    return False