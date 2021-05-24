import pygame.image
from element.obj import Object

img = pygame.image.load("imgs/border.png").convert_alpha()


class Border(Object):
    def __init__(self, x, y):
        super().__init__()
        self.set_img(img)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


if __name__ == "__main__":
    b = Border(10, 10)
    print(b.pos())
