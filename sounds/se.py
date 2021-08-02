import pygame.mixer

__se = pygame.mixer.Sound("data/bgm/se.ogg")


def play(loop):
    __se.play(loops=loop)


def stop():
    __se.stop()
