import pygame.mixer

__deadplayer = pygame.mixer.Sound("bgm/gameover.ogg")

def play(loop):
    __deadplayer.play(loops=loop)

def stop():
    __deadplayer.stop()
    