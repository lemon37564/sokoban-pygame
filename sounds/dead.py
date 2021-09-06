import pygame.mixer

__deadplayer = pygame.mixer.Sound("data/bgm/gameover.ogg")


def play(loop_times):
    __deadplayer.play(loops=loop_times)


def stop():
    __deadplayer.stop()
