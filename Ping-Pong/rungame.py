import pygame
from Bar import Bar
from Ball import Ball

pygame.init()

WHITE = (255, 255, 255)
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

    #탁구채 객체
    bar = Bar(screen, size[1], WHITE, size[1]/20)
    ball = Ball(screen, WHITE, clock.tick(30))

    # 탁구채 크기
    

    while not done:
        clock.tick(30)
        screen.fill(BLACK)
        
        #keyboard 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    bar.direction = -10
                elif event.key == pygame.K_s:
                    bar.direction = 10
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    bar.direction = 0
                elif event.key == pygame.K_s:
                    bar.direction = 0

        bar.move()
        bar.draw_block()
        ball.draw_circle()
        print(bar.positions[1])
        pygame.display.update()

runGame()
pygame.quit()