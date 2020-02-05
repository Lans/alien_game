# 屏幕设置
class Settings():
    def __init__(self):
        super().__init__()
        self.scree_width = 360
        self.scree_height = 720
        self.bg_color = (65, 105, 225)
        self.ship_speed_factor = 1.5
        # 添加子弹
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allow = 3
