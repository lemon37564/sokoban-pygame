import enum
import time
import pygame, pygame.font

import parameter
import sounds


class Option(enum.Enum):
    RESUME = 0
    RESTART = 1
    EXIT = 2
    NEXTLEVEL = 3
    TOMENU = 4


pygame.font.init()
title_font = pygame.font.Font(parameter.TITLE_FONT, 200)
button_font = pygame.font.Font(parameter.INFO_FONT, 48)

color_black = (0, 0, 0)
color_gray = (50, 50, 50)

color_btn = (167, 147, 0) # 按鈕背景顏色
color_btn_selected = (255, 255, 20) # 選中的按鈕的顏色

BTN_WIDTH = 280
BTN_HEIGHT = 64

MIDDLE_X = parameter.WIN_WIDTH // 2
TOP_Y = parameter.WIN_HEIGHT // 2 - 100 # 第一個選項出現的Y位置
TITLE_Y = parameter.WIN_HEIGHT // 2 - 300
BTN_GAP = 100 # 每個選項間的間隔


class Frame():
    def __init__(self, title: str, options: list, meaning: list):
        self.__selection = 0
        self.__title = title
        self.__options = options # 選項: string[]
        self.__meaning = meaning # 目前__selection實際代表的意義
        self.__cooldown = time.time()

    def update(self, screen):
        keys = pygame.key.get_pressed()
        now = time.time()
        if now - self.__cooldown > parameter.PAUSE_KEY_COOLDOWN:
            # 往上一個選項
            if keys[pygame.K_UP] and self.__selection-1 >= 0:
                self.__selection -= 1
                self.__cooldown = now
                sounds.se.play(sounds.LOOP_ONCE)
            # 往下一個選項
            if keys[pygame.K_DOWN] and self.__selection+1 < len(self.__options):
                self.__selection += 1
                self.__cooldown = now
                sounds.se.play(sounds.LOOP_ONCE)

        self.__draw_title(screen)
        self.__draw_btn(screen)

        # press enter, return class "Option"
        if keys[pygame.K_RETURN]:
            act = self.__meaning[self.__selection]
            self.__selection = 0
            return act

    def __draw_title(self, screen):
        text = title_font.render(self.__title, True, color_black) # 本體
        text_rect = text.get_rect(center=(MIDDLE_X, TITLE_Y))
        screen.blit(text, text_rect)

    def __draw_btn(self, screen):
        for i, text in enumerate(self.__options):
            if i == self.__selection: # 是選中的情況
                bias = 6
                clr = color_btn_selected
                shadow = pygame.Rect(0, 0, BTN_WIDTH, BTN_HEIGHT) # draw shadow 營造立體感
                shadow.center = (MIDDLE_X, TOP_Y + i * BTN_GAP)
                pygame.draw.rect(screen, color_gray, shadow, border_radius=10)
            else: # 其他未被選中的選項
                bias = 0
                clr = color_btn

            center = (MIDDLE_X - bias, TOP_Y + i*BTN_GAP - bias) # 按鈕的位置。往左上移動bias，模擬懸浮效果

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
    """失敗(死亡)的選單"""
    def __init__(self):
        super().__init__(
            "Failed",
            ["Retry", "Exit"],
            [Option.RESTART, Option.EXIT],
        )


class Pause(Frame):
    """暫停的選單"""
    def __init__(self):
        super().__init__(
            "Pause",
            ["Resume", "Restart", "Exit","Main Menu"],
            [Option.RESUME, Option.RESTART, Option.EXIT,Option.TOMENU],
        )


class Victory(Frame):
    """獲勝的選單"""
    def __init__(self):
        super().__init__(
            "Victory",
            ["Next  Level", "Restart", "Exit"],
            [Option.NEXTLEVEL, Option.RESTART, Option.EXIT],
        )
