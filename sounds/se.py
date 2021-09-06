import pygame.mixer

__se = pygame.mixer.Sound("data/bgm/se.ogg")


def play(loop_times):
    __se.play(loops=loop_times)


def stop():
    __se.stop()
