import pygame
from pygame.locals import QUIT, KEYDOWN, KEYUP

from meteor import Meteor
from plane import Plane


# Pygame 초기화
pygame.init()

# 화면 설정
WHITE = (255, 255, 255)
size = [600, 800]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
sysfont = pygame.font.SysFont('malgungothic', 36)
done = False

#게임 진행 시간
game_start_time = pygame.time.get_ticks()

#이미지 로드
background1_image = pygame.image.load('./object_images/background1.jpg')
background1_image = pygame.transform.scale(background1_image, size)
background2_image = pygame.image.load('./object_images/background2.jpg')
background2_image = pygame.transform.scale(background2_image, size)
meteor1_image = './object_images/meteor1.png'
meteor2_image = './object_images/meteor2.png'


# 게임 실행 함수
def run_game():
    global done
    count = 5
    meteors = [Meteor(meteor1_image, (50, 50)) for _ in range(5)] 
    airplane = Plane()

    while not done:
        clock.tick(60)
        #screen.fill(WHITE)


        #진행 시간 변경

        elapsed_time = (pygame.time.get_ticks() - game_start_time)// 1000
        time_text = sysfont.render(f"진행 시간: {elapsed_time}초", True, (255, 255, 255))
        

        #이후 레벨에 따라 변수들 설정
        if elapsed_time < 3:
            screen.fill((45, 50, 65))
            pass
        elif elapsed_time <= 5:
            screen.blit(background1_image, (0, 0))
            while len(meteors) <= 8:
                meteors.append(Meteor(meteor2_image, (70, 70)))
        elif elapsed_time <= 8:
            screen.blit(background2_image, (0, 0))
            while len(meteors) <= 11:
                meteors.append(Meteor(meteor2_image, (90, 90)))
        elif elapsed_time <= 11:
            screen.blit(background2_image, (0, 0))
            while len(meteors) <= 13:
                meteors.append(Meteor(meteor2_image, (200, 200)))
        else:
            screen.blit(background2_image, (0, 0))
            while len(meteors) <= 13:
                meteors.append(Meteor(meteor2_image, (200, 200)))

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

        
        #배경 이미지, 운석, 비행기 화면에 띄우기
        screen.blit(time_text, (size[0] - 500, 20))

        for meteor in meteors:
            screen.blit(meteor.image, meteor.rect)

        screen.blit(airplane.image, airplane.rect)



        pygame.display.update()

# 게임 실행

def main():
    run_game()
    pygame.quit()

if __name__ == '__main__':
    main()

