import time
import pygame

import parameter

NEXTLEVEL = 0
RESTART = 1
EXIT = 2


class Victory():
    def __init__(self):
        self.__selection = 0
        self.__normal_font = pygame.font.SysFont("default", 32)
        self.__selected_font = pygame.font.SysFont("default", 60)
        self.__option1_pos = (parameter.WIN_WIDTH//2-100, parameter.WIN_HEIGHT//2-200)
        self.__option2_pos = (parameter.WIN_WIDTH//2-100, parameter.WIN_HEIGHT//2-100)
        self.__option3_pos = (parameter.WIN_WIDTH//2-100, parameter.WIN_HEIGHT//2)
        self.__cooldown = time.time()

    def update(self, screen):
        keys = pygame.key.get_pressed()
        now = time.time()
        if now - self.__cooldown > parameter.PAUSE_KEY_COOLDOWN:
            self.__cooldown = now
            
            if keys[pygame.K_UP]:
                self.__selection -= 1
            elif keys[pygame.K_DOWN]:
                self.__selection += 1

            if self.__selection < 0 or self.__selection > 2:
                self.__selection %= 3

        self.__draw(screen)

        # press enter
        if keys[pygame.K_RETURN]:
            act = self.__selection
            self.__selection = 0
            return act

    def __draw(self, screen):
        text = self.__render_text("next level", 0)
        screen.blit(text, self.__option1_pos)
        text = self.__render_text("restart", 1)
        screen.blit(text, self.__option2_pos)
        text = self.__render_text("exit", 2)
        screen.blit(text, self.__option3_pos)

    def __render_text(self, text, target_selection):
        if self.__selection == target_selection:
            text = self.__selected_font.render(text, False, (0, 0, 0))
        else:
            text = self.__normal_font.render(text, False, (0, 0, 0))
        return text
