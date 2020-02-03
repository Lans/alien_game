import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_settings, scree, ship):
        super().__init__()
        self.scree = scree
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # 小数表示子单位置
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        # 向上移动子弹
        self.y -= self.speed_factor
        # 更新子弹的位置
        self.rect.y = self.y

    def draw_bullet(self):
        # 绘制子弹
        pygame.draw.rect(self.scree, self.color, self.rect)
