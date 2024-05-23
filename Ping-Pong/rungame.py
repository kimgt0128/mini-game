import pygame
from Bar import Bar
from Ball import Ball

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
size = [800, 600]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

def runGame():
    global done
    #게임판 크기
    screen_width = size[0]
    screen_height = size[1]

    

    #탁구채, 탁구공 객체
    bar = Bar(screen, size[1], WHITE, size[1]/20)
    balls = []
    for i in range(0, 3):
        ball = Ball(screen, WHITE, 0, size[0], size[1])
        balls.append(ball)
   

    # 탁구채 크기
    
    while not done:
        time_passed = clock.tick(60)
        time_sec = time_passed / 1000.0
        clock.tick(30)
        screen.fill(BLACK)

        elapsed_time = pygame.time.get_ticks()


        ball.time_sec = time_sec
        print(elapsed_time)
        #keyboard 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    bar.direction = -20
                elif event.key == pygame.K_s:
                    bar.direction = 20
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    bar.direction = 0
                elif event.key == pygame.K_s:
                    bar.direction = 0
        
        #충돌이벤트 처리
        #1. bar에 닿았을 때

        for ball in balls:
            if ball.x - ball.radious <= bar.width:
                if (ball.y - ball.radious >= bar.positions[1]) and (ball.y - ball.radious <= bar.positions[1] + bar.height):
                    ball.x = bar.width + ball.radious
                    ball.speed_x = -ball.speed_x
            #위, 아래, 오른쪽, 왼쪽 벽면에 닿았을 때
            if ball.x - ball.radious <= 0:
                done = True
            elif ball.x + ball.radious > size[0]:
                ball.speed_x = -ball.speed_x
            if ball.y - ball.radious <= 0:
                ball.speed_y = -ball.speed_y
                ball.y = ball.radious
            elif ball.y + ball.radious >= size[1]:
                ball.speed_y = -ball.speed_y
                ball.y = size[1] - ball.radious



        for ball in balls:  
            ball.move(time_secs)
            ball.draw_circle()
        bar.move()
        bar.draw_block()
        #ball.draw_circle()
        pygame.display.update()

runGame()

pygame.quit()