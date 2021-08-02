import enum
import time
import pygame

import parameter
import sounds


class Option(enum.Enum):
    RESUME = 0
    RESTART = 1
    EXIT = 2
    NEXTLEVEL = 3


button_font = pygame.font.SysFont("", 48)

color_black = (0, 0, 0)
color_gray = (50, 50, 50)
color_red = (255, 0, 0)
color_btn = (140, 255, 0) # 按鈕背景顏色

BTN_WIDTH = 250
BTN_HEIGHT = 64

MIDDLE_X = parameter.WIN_WIDTH // 2
TOP_Y = parameter.WIN_HEIGHT // 2 - 150 # 第一個選項出現的Y位置
GAP = 100 # 每個選項間的間隔


class Frame():
    def __init__(self, options: list, meaning: list):
        self.__selection = 0
        self.__options = options # 選項: string[]
        self.__meaning = meaning # 目前__selection實際代表的意義
        self.__cooldown = time.time()

    def update(self, screen):
        keys = pygame.key.get_pressed()
        now = time.time()
        if now - self.__cooldown > parameter.PAUSE_KEY_COOLDOWN:
            if keys[pygame.K_UP]:
                self.__selection -= 1
                self.__cooldown = now
                sounds.se.play(sounds.LOOP_ONCE)
            if keys[pygame.K_DOWN]:
                self.__selection += 1
                self.__cooldown = now
                sounds.se.play(sounds.LOOP_ONCE)

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
            if i == self.__selection: # 是選中的情況
                bias = 6
                clr = color_red
                shadow = pygame.Rect(0, 0, BTN_WIDTH, BTN_HEIGHT) # draw shadow 營造立體感
                shadow.center = (MIDDLE_X, TOP_Y + i*GAP)
                pygame.draw.rect(screen, color_gray, shadow, border_radius=10)
            else: # 其他未被選中的選項
                bias = 0
                clr = color_btn

            center = (MIDDLE_X - bias, TOP_Y + i*GAP - bias) # 按鈕的位置。往左上移動bias，模擬懸浮效果

            btn = pygame.Rect(0, 0, BTN_WIDTH, BTN_HEIGHT) # 按鈕的背景
            btn.center = center
            pygame.draw.rect(screen, clr, btn, border_radius=10)

            edge = pygame.Rect(0, 0, BTN_WIDTH, BTN_HEIGHT) # 按鈕的邊框
            edge.center = center
            pygame.draw.rect(screen, color_black, edge, width=2, border_radius=10)

            text = button_font.render(text, True, color_black) # 按鈕的文字
            text_rect = text.get_rect(center=center)
            screen.blit(text, text_rect)


class Loss(Frame):
    def __init__(self):
        super().__init__(
            ["Retry", "Exit"],
            [Option.RESTART, Option.EXIT],
        )


class Pause(Frame):
    def __init__(self):
        super().__init__(
            ["Resume", "Restart", "Exit"],
            [Option.RESUME, Option.RESTART, Option.EXIT],
        )


class Victory(Frame):
    def __init__(self):
        super().__init__(
            ["Next  Level", "Restart", "Exit"],
            [Option.NEXTLEVEL, Option.RESTART, Option.EXIT],
        )
