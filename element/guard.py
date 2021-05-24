import pygame.image
import pygame.transform
import pygame.sprite

from element.obj import Object, ObjectID
from element import direction
import parameter

# 初始化圖片
imgs = [_ for _ in range(4)]

img = pygame.image.load("imgs/guard/up.webp").convert_alpha()
imgs[direction.UP] = img
img = pygame.image.load("imgs/guard/down.webp").convert_alpha()
imgs[direction.DOWN] = img
img = pygame.image.load("imgs/guard/right.webp").convert_alpha()
imgs[direction.RIGHT] = img
img = pygame.transform.flip(img, True, False)
imgs[direction.LEFT] = img


class Guard(Object):
    def __init__(self, x, y):
        super().__init__()
        self.set_dir(direction.DOWN)
        self.set_img(self.__img())
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.__velocity = parameter.GUARD_VELOCITY

        self.__inerita = 0
        self.__sleep = 0

        current = direction.random_dir()
        self.set_dir(current)

    def set_dir(self, dir):
        self.__dir = dir
        super().set_img(self.__img())

    def update(self, all_objects: dict):
        """更新"""
        if self.__sleep < parameter.GUARD_SLEEP:
            self.__sleep += 1
            return
        elif self.__sleep == parameter.GUARD_SLEEP:
            current = direction.random_dir()
            self.set_dir(current)
            self.__sleep += 1

        if self.__inerita > parameter.GUARD_INERITA:
            self.__inerita = 0
            self.__sleep = 0

        self.__behavior(all_objects)
        self.__inerita += 1

    def __behavior(self, all_objects: dict) -> None:
        """移動"""
        if self.__dir == direction.DOWN:
            move_x, move_y = 0, self.__velocity
        elif self.__dir == direction.UP:
            move_x, move_y = 0, -self.__velocity
        elif self.__dir == direction.LEFT:
            move_x, move_y = -self.__velocity, 0
        elif self.__dir == direction.RIGHT:
            move_x, move_y = self.__velocity, 0
        else:
            move_x, move_y = 0, 0
        super().move(move_x, move_y)
        if self.__is_collide(all_objects):
            super().move(-move_x, -move_y)

    def __is_collide(self, all_objects: dict) -> bool:
        collided = pygame.sprite.spritecollide(self, all_objects[ObjectID.BORDER], dokill=False)
        if collided:
            return True
        collided = pygame.sprite.spritecollide(self, all_objects[ObjectID.WALL], dokill=False)
        if collided:
            return True
        collided = pygame.sprite.spritecollide(self, all_objects[ObjectID.BOX], dokill=False)
        if collided:
            return True
        collided = pygame.sprite.spritecollide(self, all_objects[ObjectID.GUARD], dokill=False)
        if len(collided) > 1:  # 扣掉自己
            return True
        collided = pygame.sprite.collide_rect(self, all_objects[ObjectID.PLAYER])
        if collided:
            all_objects[ObjectID.PLAYER].Set_Dead()
            return True
        return False

    def __img(self):
        return imgs[self.__dir]


if __name__ == "__main__":
    g = Guard(10, 10)
    print(g.pos())
