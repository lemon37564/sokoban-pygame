import pygame.mixer

__bgm = pygame.mixer.Sound("data/bgm/bgm.ogg")


def play(loop_times):
    __bgm.play(loops=loop_times)


def stop():
    __bgm.stop()
