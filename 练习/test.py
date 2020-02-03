import pygame
import sys
from ship import Ship


def start_game():
    pygame.init()
    scree = pygame.display.set_mode((360, 720))
    pygame.display.set_caption("test")
    ship = Ship(scree)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ship.moving_left = True
                elif event.key == pygame.K_RIGHT:
                    ship.moving_right = True
                elif event.key == pygame.K_UP:
                    ship.moving_up = True
                elif event.key == pygame.K_DOWN:
                    ship.moving_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    ship.moving_left = False
                elif event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                elif event.key == pygame.K_UP:
                    ship.moving_up = False
                elif event.key == pygame.K_DOWN:
                    ship.moving_down = False
        ship.update()
        update_scree(scree, ship)


# 更新屏幕图像，并切换到新屏幕
def update_scree(scree, ship):
    # 创建图像
    ship.biltme()
    # 让屏幕可见
    pygame.display.flip()


start_game()
