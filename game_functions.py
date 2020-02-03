import sys
import pygame
from bullet import Bullet


def check_events(ai_settings, scree, ship, bullets):
    # 响应按键和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, scree, ai_settings, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


# 响应按下事件
def check_keydown_events(event, scree, ai_settings, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(scree, ai_settings, ship, bullets)


# 响应松开事件
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


# 更新子弹位置
def update_bullet(bullets):
    # 删除多余子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


# 开火
def fire_bullet(scree, ai_settings, ship, bullets):
    if len(bullets) < ai_settings.bullet_allow:
        new_bullet = Bullet(ai_settings, scree, ship)
        bullets.add(new_bullet)


# 更新屏幕图像，并切换到新屏幕
def update_scree(ai_settings, scree, ship, bullets):
    # 填充屏幕颜色
    scree.fill(ai_settings.bg_color)
    # 创建子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 创建图像
    ship.biltme()
    # 让屏幕可见
    pygame.display.flip()
