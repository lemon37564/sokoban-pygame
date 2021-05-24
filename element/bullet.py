import pygame.image
import pygame.sprite

from element.obj import Object, ObjectID
from element import direction
import parameter

img = pygame.image.load("imgs/bullet.webp").convert_alpha()


class Bullet(Object):
    def __init__(self, x, y, bullet_dir):
        super().__init__()
        self.set_img(img)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.__velocity = parameter.BULLET_VELOCITY
        self.__direction = bullet_dir

        if self.__direction == direction.DOWN:
            self.__movement = (0, self.__velocity)
        elif self.__direction == direction.UP:
            self.__movement = (0, -self.__velocity)
        elif self.__direction == direction.LEFT:
            self.__movement = (-self.__velocity, 0)
        elif self.__direction == direction.RIGHT:
            self.__movement = (self.__velocity, 0)

    def update(self, all_ojects: dict):
        delta_x, delta_y = self.__movement
        super().move(delta_x, delta_y)
        self.__check_collide(all_ojects)

    def __check_collide(self, all_objects: dict):
        collided = pygame.sprite.spritecollide(self, all_objects[ObjectID.GUARD], dokill=True)
        if collided:
            all_objects[ObjectID.BULLET].remove(self)
        collided = pygame.sprite.spritecollide(self, all_objects[ObjectID.WALL], dokill=False)
        if collided:
            all_objects[ObjectID.BULLET].remove(self)
        collided = pygame.sprite.spritecollide(self, all_objects[ObjectID.BORDER], dokill=False)
        if collided:
            all_objects[ObjectID.BULLET].remove(self)
        collided = pygame.sprite.spritecollide(self, all_objects[ObjectID.BOX], dokill=False)
        if collided:
            all_objects[ObjectID.BULLET].remove(self)


if __name__ == "__main__":
    pass
