import logging
import pygame.mixer

pygame.mixer.init()

import sounds.shoot
import sounds.dead
import sounds.bgm
import sounds.se


LOOP_FOREVER = -1 # 循環播放
LOOP_ONCE = 0 # 播放一次

def stop_everything():
    try:
        sounds.shoot.stop()
        sounds.dead.stop()
        sounds.bgm.stop()
        sounds.se.stop()
    except Exception as err:
        logging.warning("cannot stop music,", err)
