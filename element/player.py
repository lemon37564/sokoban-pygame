import pygame.image
import pygame.time
import pygame.transform
import pygame.sprite

from element.obj import Object, ObjectID
from element import direction
import element.bullet
import parameter
import sounds

import time

# 初始化圖片
up_imgs = []
down_imgs = []
left_imgs = []
right_imgs = []
dead_imgs = []

for i in range(3):
    img = pygame.image.load(f"data/img/player/up_{i}.webp").convert_alpha()
    up_imgs.append(img)
    img = pygame.image.load(f"data/img/player/down_{i}.webp").convert_alpha()
    down_imgs.append(img)
    img = pygame.image.load(f"data/img/player/right_{i}.webp").convert_alpha()
    right_imgs.append(img)
    # 左面的圖片是右面的圖片的鏡射
    img = pygame.transform.flip(img, True, False)
    left_imgs.append(img)

for i in range(11):
    img = pygame.image.load(f"data/img/explosion/1/{i}.png").convert_alpha()
    dead_imgs.append(img)

imgs = [up_imgs, down_imgs, left_imgs, right_imgs]


class Player(Object):
    def __init__(self, x, y, skin: int):
        super().__init__()
        self.__deadframe = 0
        self.__dead_img_index = 0
        self.__ammo = parameter.INIT_BULLET_NUM
        self.__isdead = False
        self.__skin = skin
        self.__cooldown = time.time()
        self.__dont_port = False  # 避免傳送門重複觸發
        self.__goal_box = 0
        self.set_dir(direction.DOWN)
        

        self.set_img(self.__img())
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def set_dir(self, direction):
        self.__dir = direction
        self.set_img(self.__img())

    def direction(self):
        return self.__dir

    def Numberofbox_in_goal(self , all_objects): #檢查在終點的箱子數量
        self.__goal_box = 0
        for box in all_objects[ObjectID.BOX]:
            if  pygame.sprite.spritecollide(
                    box, all_objects[ObjectID.GOAL], dokill=False):
                self.__goal_box += 1
        return self.__goal_box

    def handle_keys(self, keys, all_objects: dict) -> None:
        # movement
        if keys[pygame.K_UP]:
            self.move(0, -parameter.PLAYER_VELOCITY, all_objects)
            self.set_dir(direction.UP)
        elif keys[pygame.K_DOWN]:
            self.move(0, parameter.PLAYER_VELOCITY, all_objects)
            self.set_dir(direction.DOWN)
        elif keys[pygame.K_LEFT]:
            self.move(-parameter.PLAYER_VELOCITY, 0, all_objects)
            self.set_dir(direction.LEFT)
        elif keys[pygame.K_RIGHT]:
            self.move(parameter.PLAYER_VELOCITY, 0, all_objects)
            self.set_dir(direction.RIGHT)

        # attack
        if keys[pygame.K_SPACE]:
            if self.shoot():
                sounds.shoot.play(sounds.LOOP_ONCE)
                player_x, player_y = self.rect.center
                all_objects[ObjectID.BULLET].add(
                    element.bullet.Bullet(player_x, player_y, self.__dir))

    def isdead(self):
        return self.__isdead

    def Set_Dead(self):
        self.__isdead = True

    def is_won(self, all_objects: dict) -> bool:
        # 雙向檢查
        # 檢查箱子
        for box in all_objects[ObjectID.BOX]:
            if not pygame.sprite.spritecollide(
                    box, all_objects[ObjectID.GOAL], dokill=False):
                return False
        # 檢查終點
        for goal in all_objects[ObjectID.GOAL]:
            if not pygame.sprite.spritecollide(
                    goal, all_objects[ObjectID.BOX], dokill=False):
                return False
        return True


    # 增加子彈
    def add_ammo(self, delta):
        self.__ammo += delta

    # 攻擊，回傳是否成功（有沒有子彈）
    def shoot(self) -> bool:
        if self.__ammo <= 0:
            return False
        now = time.time()
        # 攻擊的冷卻時間
        if now - self.__cooldown > parameter.BULLET_COOLDOWN:
            self.__cooldown = now
            self.__ammo -= 1
            return True
        return False

    # 當前擁有子彈數
    def ammos(self) -> int:
        return self.__ammo

    def DeadAnime(self) -> bool:
        # 如果放完則回傳true
        pygame.time.delay(50)
        sounds.dead.play(sounds.LOOP_ONCE)
        self.__deadframe += 1
        if self.__deadframe >= parameter.DEAD_DELAY:
            self.__deadframe = 0
            self.__dead_img_index += 1
            if self.__dead_img_index >= len(dead_imgs):
                return True
            super().set_img(dead_imgs[self.__dead_img_index])
        return False

    def draw(self, screen):
        screen.blit(self.img(), self.rect)

    def move(self, delta_x: int, delta_y: int, all_objects: dict) -> bool:
        # 先移動，判斷若碰撞到物體才移動回到原位
        super().move(delta_x, delta_y)
        if self.__is_collide(delta_x, delta_y, all_objects):
            super().move(-delta_x, -delta_y)
            return False
        return True

    # 判斷是否碰撞
    def __is_collide(self, delta_x: int, delta_y: int, all_objects: dict) -> bool:
        collided_portal = pygame.sprite.spritecollide(self, all_objects[ObjectID.PORTAL], dokill=False)
        # 碰撞傳送門且並非重複觸發
        if collided_portal and (not self.__dont_port):
            # 在地圖上尋找下一個傳送門的位置
            current_index = 0
            for i, p in enumerate(all_objects[ObjectID.PORTAL]):
                if p is collided_portal[0]:
                    current_index = i
            port_index = (current_index + 1) % len(all_objects[ObjectID.PORTAL].sprites())
            portal_pos_x, portal_pos_y = all_objects[ObjectID.PORTAL].sprites()[port_index].pos()

            # 設定自身位置到目標傳送門位置
            self.set_pos(portal_pos_x, portal_pos_y)
            self.__dont_port = True
        # 已經沒有跟傳送門碰撞則將dont_port設為False，表示可以再進行傳送
        if not collided_portal:
            self.__dont_port = False
        
        # 與箱子的碰撞
        collided_boxes = pygame.sprite.spritecollide(self, all_objects[ObjectID.BOX], dokill=False)
        for box in collided_boxes:
            box_moved = box.move(delta_x, delta_y, all_objects)
            if not box_moved:
                return True
        
        # 與牆壁的碰撞
        collided = pygame.sprite.spritecollide(self, all_objects[ObjectID.WALL], dokill=False)
        if collided:
            return True

        # 與邊界的碰撞
        collided = pygame.sprite.spritecollide(self, all_objects[ObjectID.BORDER], dokill=False)
        if collided:
            return True

        # 與警衛的碰撞
        collided = pygame.sprite.spritecollide(self, all_objects[ObjectID.GUARD], dokill=False)
        if collided:
            # 與警衛碰撞則將自身狀態設為死亡
            self.Set_Dead()
            return True
        return False

    def __img(self):
        return imgs[self.__dir][self.__skin]


if __name__ == "__main__":
    p = Player(1, 1, 2)
    print(p.img())
    # print(p.__ammo)
