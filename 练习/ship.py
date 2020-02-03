import pygame


class Ship():
    def __init__(self, scree):
        super().__init__()
        self.scree = scree
        # 加载飞船外形以及外接矩形
        self.image = pygame.image.load('外星人游戏/img/ship.bmp')
        self.rect = self.image.get_rect()
        self.scree_rect = scree.get_rect()
        # 将飞船放在屏幕底部中间
        self.rect.centerx = self.scree_rect.centerx
        self.rect.centery = self.scree_rect.centery
        # 在飞船中间存储小数值
        self.center = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        # 持续移动变量
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    # 创建飞船
    def biltme(self):
        self.scree.blit(self.image, self.rect)

    # 更新位置
    def update(self):
        # 更新飞船的中心点值
        if self.moving_right and self.rect.right < self.scree_rect.right:
            self.center += 3
        if self.moving_left and self.rect.left > 0:
            self.center -= 3
        if self.moving_up and self.rect.top > 0:
            self.centery -= 3
        if self.moving_down and self.rect.bottom < self.scree_rect.bottom:
            self.centery += 3

        # 根据self.center值更新rect对象
        self.rect.centerx = self.center
        self.rect.centery = self.centery
