# 物件原形，其他物件繼承此物件
from pygame import sprite
class Object(sprite.Sprite):
    def __init__(self, x, y):
        self.__x, self.__y = x, y
    
    # 移動
    def move(self, delta_x, delta_y):
        self.__x += delta_x
        self.__y += delta_y

    def set_pos(self, x , y):
        self.__x, self.__y = x, y

    def pos(self):
        return self.__x, self.__y

    def name(self):
        return self.__class__

    def img(self):
        return self.__img

    def set_img(self, img):
        self.__img = img


if __name__ == "__main__":
    o = Object(1, 1)
    print(o.name())
