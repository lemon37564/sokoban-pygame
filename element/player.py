from element.obj import Object
from element.box import Box
from element.guard import Guard
from element.goal import Goal
from pygame import image, transform,quit
from element import direction
import parameter


import time

# 初始化圖片
up_imgs = []
down_imgs = []
left_imgs = []
right_imgs = []
dead_imgs = []

for i in range(3):
    img = image.load(f"imgs/player/up_{i}.png").convert_alpha()
    up_imgs.append(img)
    img = image.load(f"imgs/player/down_{i}.png").convert_alpha()
    down_imgs.append(img)
    img = image.load(f"imgs/player/right_{i}.png").convert_alpha()
    right_imgs.append(img)
    img = transform.flip(img, True, False)
    left_imgs.append(img)

for i in range(11):
    img = image.load(f"imgs/explosion/1/{i}.png").convert_alpha()
    dead_imgs.append(img)

imgs = [up_imgs, down_imgs, left_imgs, right_imgs]


class Player(Object):
    def __init__(self, x, y, skin: int):
        super().__init__(x, y)
        self.__deadframe = 0
        self.__dead_img_index = 0
        self.set_img(dead_imgs[self.__dead_img_index])

        self.__ammo = 3
        self.__isdead = False
        self.__skin = skin
        self.__dir = direction.DOWN
        super().set_img(self.__img())
        self.__cooldown = time.time()

    def set_dir(self, direction):
        self.__dir = direction
        super().set_img(self.__img())

    def direction(self):
        return self.__dir
    def isdead(self):
        return self.__isdead
    def Set_Dead(self):
        self.__isdead = True        
    # 增加子彈
    def add_ammo(self, delta):
        self.__ammo += delta

    # 攻擊，回傳是否成功（有沒有子彈）
    def shoot(self) -> bool:
        if self.__ammo < 0:
            return False
        now = time.time()
        if now - self.__cooldown > parameter.BULLET_COOLDOWN:
            self.__cooldown = now
            self.__ammo -= 1
            return True
        return False

    # 當前擁有子彈數
    def ammos(self) -> int:
        return self.__ammo

    def DeadAnime(self):
        self.__deadframe += 1
        if self.__deadframe >= parameter.DEAD_DELAY:
            self.__deadframe = 0
            self.__dead_img_index += 1
            if self.__dead_img_index >= len(dead_imgs):
                quit()
            super().set_img(dead_imgs[self.__dead_img_index])
        

        

    def move(self, delta_x, delta_y, world: list):
        super().move(delta_x, delta_y)
        if self.__is_collide(world, delta_x, delta_y):
            super().move(-delta_x, -delta_y)

    def __is_collide(self, world: list, delta_x, delta_y) -> bool:
        player_x, player_y = super().pos()
        for item in world:
            if item is self or isinstance(item, Goal):
                continue
            item_x, item_y = item.pos()
            if abs(item_x - player_x) < parameter.GAP and abs(item_y - player_y) < parameter.GAP:
                # 碰撞到的是箱子的情況
                if isinstance(item, Box):
                    prev_pos = item.pos()
                    item.move(delta_x, delta_y, world)
                    return prev_pos == item.pos()  # 如果箱子位置沒變，則箱子已經碰撞其他object
                if isinstance(item,Guard):
                    self.Set_Dead()
                return True
        return False

    def __img(self):
        return imgs[self.__dir][self.__skin]


if __name__ == "__main__":
    p = Player(1, 1, 2)
    print(p.img())
    # print(p.__ammo)
