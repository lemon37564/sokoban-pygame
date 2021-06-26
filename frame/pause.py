import time
import pygame

import parameter
import frame.render

RESUME = 0
RESTART = 1
EXIT = 2


class Pause():
    def __init__(self):
        self.__selection = 0
        self.__option1_pos = (parameter.WIN_WIDTH//2-100, parameter.WIN_HEIGHT//2-200)
        self.__option2_pos = (parameter.WIN_WIDTH//2-100, parameter.WIN_HEIGHT//2-100)
        self.__option3_pos = (parameter.WIN_WIDTH//2-100, parameter.WIN_HEIGHT//2)
        self.__cooldown = time.time()

    def update(self, screen):
        keys = pygame.key.get_pressed()
        now = time.time()
        if now - self.__cooldown > parameter.PAUSE_KEY_COOLDOWN:
            if self.__selection != 0 and keys[pygame.K_UP]:
                self.__selection -= 1
                self.__cooldown = now
            if self.__selection != 2 and keys[pygame.K_DOWN]:
                self.__selection += 1
                self.__cooldown = now

        self.__draw(screen)

        # press enter
        if keys[pygame.K_RETURN]:
            act = self.__selection
            self.__selection = 0
            return act

    def __draw(self, screen):
        text = frame.render.render_text(self.__selection, 0, "resume")
        screen.blit(text, self.__option1_pos)
        text = frame.render.render_text(self.__selection, 1, "restart")
        screen.blit(text, self.__option2_pos)
        text = frame.render.render_text(self.__selection, 2, "exit")
        screen.blit(text, self.__option3_pos)
