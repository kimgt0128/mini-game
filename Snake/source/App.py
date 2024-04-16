import pygame # 1. pygame 선언
import random

from snake import Snake
from apple import Apple
from function import isIn
 
pygame.init() # 2. pygame 초기화

from setting import *#init이후에 setting값 가져오기
# 4. pygame 무한루프
def runGame():
    global done, last_moved_time
    #게임 시작 시, 뱀과 사과를 초기화
    snake = Snake(screen, GREEN) 
    apple = Apple(screen, RED)
 
    while not done:
        clock.tick(100)
        screen.fill(WHITE)

        #진행 시간 변경

        elapsed_time = (pygame.time.get_ticks() - game_start_time)// 1000
        time_text = sysfont.render(f"진행 시간: {elapsed_time}초", True, (0, 0, 0))
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
            if event.type == pygame.KEYDOWN:
                if event.key in KEY_DIRECTION:
                    snake.direction = KEY_DIRECTION[event.key]
 
        if timedelta(seconds=0.05) <= datetime.now() - last_moved_time:
            snake.move()
            last_moved_time = datetime.now()
 
        if snake.positions[0] == apple.position:
            snake.grow()    
            apple.position = (random.randint(0, 19), random.randint(0, 19))
        
        if ((snake.positions[0] in snake.positions[1:])):
            done = True
        elif isIn(snake.positions[0], size) == True:
            done = True
        #done = 

        screen.blit(time_text, (200, 200))
        snake.draw()
        apple.draw()
        pygame.display.update()
 
