import pygame

def draw_block(screen, color, position):
    block = pygame.Rect((position[1] * 20, position[0] * 20),
                        (20, 20))
    pygame.draw.rect(screen, color, block)



def isIn(position, size):
    #한 칸의 크기가 20이므로 position 계산시 이를 고려
    if position[0]*20 < 0 or position[0]*20 >= size[1] or position[1]*20 < 0 or position[1]*20 >= size[0]:
        return True
    return False
