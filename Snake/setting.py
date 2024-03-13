import pygame
from datetime import datetime
from datetime import timedelta

# pygame에 사용되는 전역변수 선언
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
size = [400,400]
screen = pygame.display.set_mode(size)

# 파이게임 전역 변수들 선언
done= False
clock= pygame.time.Clock()
last_moved_time = datetime.now()
# 게임 진행 시간
game_start_time = pygame.time.get_ticks()


#font
#sysfont = pygame.font.SysFont('malgungothic', 36)


KEY_DIRECTION = {
    pygame.K_w: 'N',
    pygame.K_s: 'S',
    pygame.K_a: 'W',
    pygame.K_d: 'E',
}