import pygame.image
import pygame.sprite
import pygame.transform

from element.obj import Object, ObjectID
from element import direction
import parameter

img_right = pygame.image.load("data/img/player/Kunai.png").convert_alpha()
img_left = pygame.transform.flip(img_right, True, False)
img_up = pygame.transform.rotate(img_right, 90)
img_down = pygame.transform.flip(img_up, False, True)

class Bullet(Object):
    def __init__(self, x, y, bullet_dir):
        super().__init__()

        self.__velocity = parameter.BULLET_VELOCITY
        self.__direction = bullet_dir

        if self.__direction == direction.DOWN:
            self.set_img(img_down)
            self.__movement = (0, self.__velocity)
        elif self.__direction == direction.UP:
            self.set_img(img_up)
            self.__movement = (0, -self.__velocity)
        elif self.__direction == direction.LEFT:
            self.set_img(img_left)
            self.__movement = (-self.__velocity, 0)
        elif self.__direction == direction.RIGHT:
            self.set_img(img_right)
            self.__movement = (self.__velocity, 0)
    
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    # 依據移動速度向目前的方向移動
    def update(self, all_ojects: dict):
        delta_x, delta_y = self.__movement
        super().move(delta_x, delta_y)
        self.__check_collide(all_ojects)

    # 檢查碰撞，若碰撞警衛則殺死警衛。碰撞其他物件則刪除自身
    def __check_collide(self, all_objects: dict):
        collided = pygame.sprite.spritecollide(
            self, all_objects[ObjectID.GUARD], dokill=True)
        if collided:
            all_objects[ObjectID.BULLET].remove(self)
        collided = pygame.sprite.spritecollide(
            self, all_objects[ObjectID.WALL], dokill=False)
        if collided:
            all_objects[ObjectID.BULLET].remove(self)
        collided = pygame.sprite.spritecollide(
            self, all_objects[ObjectID.BORDER], dokill=False)
        if collided:
            all_objects[ObjectID.BULLET].remove(self)
        collided = pygame.sprite.spritecollide(
            self, all_objects[ObjectID.BOX], dokill=False)
        if collided:
            all_objects[ObjectID.BULLET].remove(self)


if __name__ == "__main__":
    pass
