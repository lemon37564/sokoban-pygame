import pygame.mixer

__shootingplayer = pygame.mixer.Sound("data/bgm/shooting.ogg")


def play(loop_times):
    __shootingplayer.play(loops=loop_times)


def stop():
    __shootingplayer.stop()
