import pygame # 1. pygame 선언
import random

from snake import Snake
from apple import Apple
from obstacle import Obstacle
from function import isIn
 
pygame.init() # 2. pygame 초기화

from setting import *#init이후에 setting값 가져오기
# 4. pygame 무한루프
def runGame():
    global done, last_moved_time, screen
    #게임 시작 시, 뱀과 사과를 초기화, 객체 인스턴스 생성
    snake = Snake(screen, GREEN) 
    apple = Apple(screen, RED)
    obstacles = []
    obstacle1 = Obstacle(screen, BLACK, size, snake.positions, apple.position)
    obstacles.append(obstacle1)
    while not done:
        clock.tick(120)
        screen.fill(WHITE)



        level_info = 1
        #진행 시간 변경
        elapsed_time = (pygame.time.get_ticks() - game_start_time)// 1000

        if elapsed_time > 5:
            while len(obstacles) < 5:
                level_info = 1
                obstacle = Obstacle(screen, BLACK, size, snake.positions, apple.position)
                obstacles.append(obstacle) 
        if elapsed_time > 10:
            while len(obstacles) < 7:
                level_info = 2
                obstacle = Obstacle(screen, BLACK, size, snake.positions, apple.position)
                obstacles.append(obstacle) 

        
        time_text = sysfont.render(f"진행 시간: {elapsed_time}초", True, (0, 0, 0))
        level_text = sysfont.render(f"level{level_info}", True, (0, 0, 255))
        
        
        #keydown이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
            if event.type == pygame.KEYDOWN:
                if event.key in KEY_DIRECTION:
                    snake.direction = KEY_DIRECTION[event.key]
        #move이벤트 처리
        if timedelta(seconds=0.1) <= datetime.now() - last_moved_time:
            snake.move()
            last_moved_time = datetime.now()
        #grow이벤트 처리
        if snake.positions[0] == apple.position:
            snake.grow()    
            apple.position = (random.randint(0, 30), random.randint(0, 30))
        #예외 처리
        if ((snake.positions[0] in snake.positions[1:])):
            done = True
        elif isIn(snake.positions[0], size) == True:
            done = True
        
        #장애물들 충돌 바교
        for obstacle in obstacles:

            if obstacle.position[0] == snake.positions[0][0] and obstacle.position[1] == snake.positions[0][1]:
                done = True


        #screen 띄우기
        #screen.fill(WHITE)
        screen.blit(time_text, (200, 200))
        screen.blit(level_text, (0, 0))
        snake.draw()
        apple.draw()

        for obstacle in obstacles:
            obstacle.draw()

        #obstacle.draw()
        

        #변화된 정보 업데이트
        pygame.display.update()
 
