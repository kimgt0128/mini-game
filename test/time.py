import pygame # 1. pygame 선언
import random
import time

pygame.init() # 2. pygame 초기화

# 3. pygame에 사용되는 전역변수 선언
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
large_font = pygame.font.SysFont(None, 72)
small_font = pygame.font.SysFont(None, 36)
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height)) 

done = False
clock = pygame.time.Clock()

# 4. pygame 무한루프
def runGame():
    global done

    ## 시작시간설정
    start_time = time.time()
    while not done:
        clock.tick(10)
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # [X] 종료키가 누르면, 게임 종료
                done=True
        
        cur_time = time.time()-start_time
        text = small_font.render("time : " + str(int(cur_time)), True, RED)
        screen.blit(text, (0, 0))
        pygame.display.update() #모든 화면 그리기 업데이트

runGame()
pygame.quit()