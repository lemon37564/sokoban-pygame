import pygame.image
import pygame.sprite
import parameter

img = pygame.image.load("imgs/mask.webp").convert_alpha()


class Mask(pygame.sprite.Sprite):
    """
    增加遊戲難度用的物件
    用來限制視野
    """
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.__img = img
        self.rect = self.__img.get_rect()
        self.rect.center = (x, y)

    def draw(self, screen):
        screen.blit(self.__img, self.rect)

    def update(self, player):
        player_x, player_y = player.pos()
        self.rect.center = (player_x, player_y)

if __name__ == "__main__":
    pass
