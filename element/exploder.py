import pygame.image

from element.obj import Object, ObjectID

# 初始化所有圖片
imgs = []
for i in range(11):
    img = pygame.image.load(f"data/img/explosion/1/{i}.png").convert_alpha()
    imgs.append(img)


class Exploder(Object):
    def __init__(self, x, y):
        super().__init__()
        self.__img_index = 0
        self.__frame = 0  # 播放的幀數
        self.set_img(imgs[self.__img_index])
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self, all_objects):
        self.__frame += 1
        # 每隔 protal_delay個幀，更新下一個圖片
        if self.__frame >= 4:
            self.__frame = 0
            self.__img_index += 1
            super().set_img(imgs[self.__img_index % len(imgs)])
        
        if self.__img_index == len(imgs) - 1:
            all_objects[ObjectID.BULLET].remove(self)


if __name__ == "__main__":
    pass
