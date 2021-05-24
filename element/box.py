import random

import pygame.image
import pygame.rect
import pygame.sprite

from element.obj import Object, ObjectID
import parameter

# 初始化所有圖片
img = pygame.image.load("imgs/boxes.webp").convert_alpha()
imgs = [_ for _ in range(10)]
for i, _ in enumerate(imgs):
    offset = parameter.BOX_SIZE * i
    rect_ = pygame.rect.Rect(offset, 0, parameter.BOX_SIZE, parameter.BOX_SIZE)
    imgs[i] = img.subsurface(rect_)


class Box(Object):
    def __init__(self, x, y):
        super().__init__()
        __img = random.choice(imgs)
        self.set_img(__img)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move(self, delta_x: int, delta_y: int, all_objects: dict) -> bool:
        """回傳bool表示是否有移動"""
        super().move(delta_x, delta_y)
        if self.__is_collide(all_objects):
            super().move(-delta_x, -delta_y)
            return False
        return True

    def __is_collide(self, all_objects: dict) -> bool:
        collided = pygame.sprite.spritecollide(self, all_objects[ObjectID.WALL], dokill=False)
        if collided:
            return True
        collided = pygame.sprite.spritecollide(self, all_objects[ObjectID.BORDER], dokill=False)
        if collided:
            return True
        collided = pygame.sprite.spritecollide(self, all_objects[ObjectID.GUARD], dokill=False)
        if collided:
            return True
        collided = pygame.sprite.spritecollide(self, all_objects[ObjectID.BOX], dokill=False)
        if len(collided) > 1:  # 要扣掉自己與自己的碰撞
            return True
        return False


if __name__ == "__main__":
    b = Box(10, 10)
    print(b.pos())
    b.move(10, -20)
    print(b.pos())
