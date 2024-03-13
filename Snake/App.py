import pygame # 1. pygame 선언
import random

from snake import Snake
from apple import Apple
from setting import *
 
pygame.init() # 2. pygame 초기화

# 4. pygame 무한루프
def runGame():
    global done, last_moved_time
    #게임 시작 시, 뱀과 사과를 초기화
    snake = Snake(screen, GREEN) 
    apple = Apple(screen, RED)
 
    while not done:
        clock.tick(60)
        screen.fill(WHITE)
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
            if event.type == pygame.KEYDOWN:
                if event.key in KEY_DIRECTION:
                    snake.direction = KEY_DIRECTION[event.key]
 
        if timedelta(seconds=0.1) <= datetime.now() - last_moved_time:
            snake.move()
            last_moved_time = datetime.now()
 
        if snake.positions[0] == apple.position:
            snake.grow()    
            apple.position = (random.randint(0, 19), random.randint(0, 19))
        
        if snake.positions[0] in snake.positions[1:]:
            done = True
 
 
        snake.draw()
        apple.draw()
        pygame.display.update()
 
