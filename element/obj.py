import enum
import pygame.sprite
import pygame.image


# 物件原形，其他物件繼承此物件
class Object(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    # 移動
    def move(self, delta_x, delta_y):
        x = self.rect.center[0] + delta_x
        y = self.rect.center[1] + delta_y
        self.set_pos(x, y)

    def set_pos(self, x, y):
        self.rect.center = (x, y)

    def pos(self):
        return self.rect.center

    def update(self) -> None:
        pygame.sprite.Sprite.update(self)

    def img(self):
        return self.image

    def set_img(self, image):
        self.image = image

    def name(self):
        return self.__class__


class ObjectID(enum.Enum):
    ARROW = 0
    BORDER = 1
    BOX = 2
    BULLET = 3
    GOAL = 4
    PLAYER = 5
    PORTAL = 6
    GUARD = 7
    MASK = 8
    WALL = 9


if __name__ == "__main__":
    o = Object(1, 1)
    print(o.pos())
