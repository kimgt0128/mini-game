#벽돌깨기 게임

import pygame
import random
import time
import sys
import threading

pygame.init() 
#색깔 지정
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
#render할 글꼴 설정
large_font = pygame.font.SysFont('malgungothic', 72)
small_font = pygame.font.SysFont('malgungothic', 36)
#화면 크기 설정
screen_width = 600
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height)) 

done = False

clock = pygame.time.Clock() 

#시작, 종료 시간
finish_time = None
countdown_timer = 3

def delayed_task():
    global done
    done = True

def runGame():
    global done
    global finish_time
    score = 0
    missed = 0
    #game_over 변수
    SUCCESS = 1
    FAILURE = 2
    game_over = 0
    
    bricks = []
    COLUMN_COUNT = 8
    ROW_COUNT = 10
    #2차원 배열로 벽돌 설정하기
    for column_index in range(COLUMN_COUNT):
        for row_index in range(ROW_COUNT):
            brick = pygame.Rect(column_index * (60 + 10) + 35, row_index * (16 + 5) + 35, 60, 16)
            bricks.append(brick)  #len 배열에 벽돌 추가     

    ball = pygame.Rect(screen_width // 2 - 16 // 2, screen_height // 2 - 30 // 2, 16, 16)
    #dy, dx가 5, -5중 하나 선택되도록 하기
    directions = [5, -5]
    ball_dx = random.choice(directions)
    ball_dy = random.choice(directions)
    #paddle설정
    paddle = pygame.Rect(screen_width // 2 - 80 // 2, screen_height - 16, 80, 5)
    paddle_dx = 0

    while not done: 
        clock.tick(60)
        screen.fill(BLACK)
        #파이게임 이벤트 설정
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    paddle_dx = -10
                elif event.key == pygame.K_RIGHT:
                    paddle_dx = 10
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    paddle_dx = 0
                elif event.key == pygame.K_RIGHT:
                    paddle_dx = 0        

        paddle.left += paddle_dx

        ball.left += ball_dx
        ball.top  += ball_dy
        #ball 충돌 설정
        if ball.left <= 0:
            ball.left = 0
            ball_dx *= -1
        elif ball.left >= screen_width - ball.width: 
            ball.left = screen_width - ball.width
            ball_dx *= -1
        if ball.top < 0:
            ball.top = 0
            ball_dy *= -1
        elif ball.top >= screen_height:
            missed += 1
            ball.left = screen_width // 2 - ball.width // 2
            ball.top = screen_height // 2 - ball.width // 2
            ball_dx = random.choice(directions)
            ball_dy = random.choice(directions)

        #3개 이상 놓치면 게임 종료
        if missed >= 3:
            game_over = FAILURE 
        #패들 범위 벗어나는 예외 설정
        if paddle.left < 0:
            paddle.left = 0
        elif paddle.left > screen_width - paddle.width:
            paddle.left = screen_width - paddle.width
        #공과 벽돌의 충돌 설정
        for brick in bricks:
            if ball.colliderect(brick):
                bricks.remove(brick)
                ball_dy = -ball_dy
                score += 1
                break
        #공과 패달의 충돌 설정
        if ball.colliderect(paddle):
            ball_dy += 0
            ball_dy = -ball_dy
            if ball.centerx <= paddle.left or ball.centerx > paddle.right:
                ball_dx = ball_dx * -1
            #패들에 충돌시 공의 속도를 증가시키기
            ball_dy -= 1
            if ball_dx < 0:
                ball_dx -= 1
            elif ball_dx > 0:
                ball_dx += 1
        #벽돌의 개수가 0이면 게임 종료
        if len(bricks) == 0:
            print('success')

            game_over = SUCCESS

        #화면 그리기
        for brick in bricks:
            pygame.draw.rect(screen, GREEN, brick)

        if(game_over != FAILURE):
            pygame.draw.circle(screen, WHITE, (ball.centerx, ball.centery), ball.width // 2)

        pygame.draw.rect(screen, BLUE, paddle)
        #화면에 점수 표시
        score_image = small_font.render('Point {}'.format(score), True, YELLOW)
        screen.blit(score_image, (10, 10))
        #화면에 놓친공 개수 표시
        missed_image = small_font.render('Missed {}'.format(missed), True, YELLOW)
        screen.blit(missed_image, missed_image.get_rect(right=screen_width - 10, top=10))
        #게임종료 조건 확인
        if game_over > 0:
            if game_over == SUCCESS:
                success_image = large_font.render('성공', True, GREEN)
                screen.blit(success_image, success_image.get_rect(centerx=screen_width // 2, centery=screen_height // 2))
            elif game_over == FAILURE:
                #실패 메시지 표시
                threading.Timer(3, delayed_task).start()
                failure_image = large_font.render('실패', True, RED)
                screen.blit(failure_image, failure_image.get_rect(centerx=screen_width // 2, centery=screen_height // 2 - 50))
                ball_dy = 0
                ball_dx = 0
                if(finish_time == None):
                    finish_time = pygame.time.get_ticks()
                remaining_time = countdown_timer - (pygame.time.get_ticks() - finish_time) // 1000
                
                print(remaining_time)
                exit_message = "{}초 후 종료".format(remaining_time)
                exit_image = small_font.render(exit_message, True, RED)
                screen.blit(exit_image, exit_image.get_rect(center=(screen_width // 2, screen_height // 2 + 50)))

        pygame.display.update()

runGame()
pygame.quit()