import pygame
from pygame.locals import QUIT, KEYDOWN, KEYUP
import sys
from meteor import Meteor
from plane import Airplane

# 게임 실행 함수
def runGame(done, screen, color):
    global game_start_time, size, sysfont, clock
    meteors = [Meteor() for _ in range(5)] 
    airplane = Airplane()

    while not done:
        clock.tick(60)
        screen.fill(color)

        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
                break
            elif event.type == KEYDOWN:
                if event.key == pygame.K_LEFT:
                    airplane.dx = -5
                elif event.key == pygame.K_RIGHT:
                    airplane.dx = 5
                elif event.key == pygame.K_UP:
                    airplane.dy = -5
                elif event.key == pygame.K_DOWN:
                    airplane.dy = 5
                
            elif event.type == KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    airplane.dx = 0
                elif event.key in (pygame.K_UP, pygame.K_DOWN):
                    airplane.dy = 0

        for meteor in meteors:
            meteor.update()

        airplane.update()

        # 충돌 감지
        collisions = pygame.sprite.spritecollide(airplane, meteors, False, pygame.sprite.collide_mask)
        if collisions:
            print("충돌")
            text = sysfont.render("충돌!!!!", True, (255, 0, 0))
            screen.blit(text, (200, 200))
            done = True

        for meteor in meteors:
            screen.blit(meteor.image, meteor.rect)

        screen.blit(airplane.image, airplane.rect)

        elapsed_time = (pygame.time.get_ticks() - game_start_time) // 1000
        time_text = sysfont.render(f"진행 시간: {elapsed_time}초", True, (0, 0, 0))
        screen.blit(time_text, (size[0] - 500, 20))

        pygame.display.update()