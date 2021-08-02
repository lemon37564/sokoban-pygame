import enum
import time
import pygame

import parameter


class Option(enum.Enum):
    RESUME = 0
    RESTART = 1
    EXIT = 2
    NEXTLEVEL = 4


normal_font = pygame.font.SysFont("", 32)
selected_font = pygame.font.SysFont("", 60)

color_black = (0, 0, 0)
color_red = (255, 0, 0)
color_btn_bg = (30, 30, 30)

MIDDLE_X = parameter.WIN_WIDTH // 2 - 150
TOP_Y = parameter.WIN_HEIGHT // 2 - 250
GAP = 150


class Frame():
    def __init__(self, options, meaning):
        self.__selection = 0
        self.__options = options
        self.__meaning = meaning
        self.__cooldown = time.time()

    def update(self, screen):
        keys = pygame.key.get_pressed()
        now = time.time()
        if now - self.__cooldown > parameter.PAUSE_KEY_COOLDOWN:
            if keys[pygame.K_UP]:
                self.__selection -= 1
                self.__cooldown = now
            if keys[pygame.K_DOWN]:
                self.__selection += 1
                self.__cooldown = now

        if self.__selection < 0:
            self.__selection = 0
        elif self.__selection >= len(self.__options):
            self.__selection = len(self.__options) - 1

        self.__draw(screen)

        # press enter
        if keys[pygame.K_RETURN]:
            act = self.__meaning[self.__selection]
            self.__selection = 0
            return act

    def __draw(self, screen):
        for i, text in enumerate(self.__options):
            text = self.__render_button(self.__selection, i, text)
            screen.blit(text, (MIDDLE_X, TOP_Y + i * GAP))

    def __render_button(self, selection, target_selection, text):
        if selection == target_selection:
            text = selected_font.render(text, True, color_red)
        else:
            text = normal_font.render(text, True, color_black)
        return text


class Loss(Frame):
    def __init__(self):
        super().__init__(
            ["RETRY", "EXIT"],
            [Option.RESTART, Option.EXIT],
        )


class Pause(Frame):
    def __init__(self):
        super().__init__(
            ["RESUME", "RESTART", "EXIT"],
            [Option.RESUME, Option.RESTART, Option.EXIT],
        )


class Victory(Frame):
    def __init__(self):
        super().__init__(
            ["NEXT LEVEL", "RESTART", "EXIT"],
            [Option.NEXTLEVEL, Option.RESTART, Option.EXIT],
        )
