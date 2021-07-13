import pygame.mixer

__shootingplayer = pygame.mixer.Sound("data/bgm/shooting.ogg")

def play(loop):
    __shootingplayer.play(loops=loop)

def stop():
    __shootingplayer.stop()
    