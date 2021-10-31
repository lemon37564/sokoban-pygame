#!/bin/env python3
import pygame
import pygame.time
import time
import enum
import logging

# 設定視窗大小
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


import record
import frame
import maps
import element
import sounds
import parameter
import GameTimer.GameTimer
from pygame import freetype as ft

ft.init()
info_font = ft.Font(parameter.INFO_FONT , 20)

WIN_WIDTH, WIN_HEIGHT = parameter.WIN_WIDTH, parameter.WIN_HEIGHT


class GameState(enum.Enum):
    """
    用來表示當前遊戲的狀況
    畫面依據目前狀況進行不同的更新
    """
    PLAYING = 0
    PAUSE = 1
    VICTORY = 2
    LOSING = 3
    LOSS = 4


class Game():
    """
    level 表示第幾關
    mask 是用來增加遊戲難度的物件
    debug時不啟用mask
    """

    def __init__(self, level, debug=False):
        self.ticker = pygame.time.Clock()  # 控制fps的物件
        self.background = (230, 230, 200)  # 背景顏色
        self.level = level
        self.build_world()
        self.key_cooldown = time.time()
        self.state = GameState.PLAYING # 初始狀態為playing
        self.Timer = GameTimer.GameTimer.Timer()
        self.score = 0 #分數

        # 各種frames的初始化
        self.game_pause = frame.Pause()  # pause frame
        self.game_victory = frame.Victory()
        self.game_loss = frame.Loss()  # 死亡後的選單

        self.display_font = pygame.font.Font(parameter.FONT, 24)

        self.debug = debug
        if self.debug:
            logging.info("starting game with debug mode")
        else:
            player_x, player_y = self.player.pos()
            self.mask = element.Mask(player_x, player_y)

    def run_game(self):
        sounds.bgm.play(sounds.LOOP_FOREVER)
        self.Timer.start()
        self.in_game = True
        while self.in_game:
            # 基礎事件
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.in_game = False

            # 依據目前遊戲的狀態選擇更新模式
            if self.state == GameState.PLAYING:
                self.Timer.start()
                self.update_world()
                self.key_handle()
                self.draw_world()
            elif self.state == GameState.PAUSE:
                self.Timer.pause()
                self.pause()
            elif self.state == GameState.VICTORY:
                self.Timer.pause()
                self.victory()
            elif self.state == GameState.LOSING:
                self.Timer.pause()
                self.gameOver()
                self.update_world()
                self.draw_world()
            elif self.state == GameState.LOSS:
                self.Timer.pause()
                self.loss()

            self.info_show() # 印出畫面資訊
            pygame.display.update()
            self.ticker.tick(60)  # 60 fps

        pygame.quit()

    def pause(self):
        # 背景色
        screen.fill(self.background)
        selection = self.game_pause.update(screen)

        # 根據不同選項，對遊戲狀態進行更新
        if selection == frame.Option.RESUME:
            self.state = GameState.PLAYING
        elif selection == frame.Option.RESTART:
            self.restart()
            self.state = GameState.PLAYING
        elif selection == frame.Option.EXIT:
            self.in_game = False

    def victory(self):
        # 背景色
        screen.fill(self.background)
        selection = self.game_victory.update(screen)

        # 根據不同選項，對遊戲狀態進行更新
        if selection == frame.Option.NEXTLEVEL:
            self.level += 1
            self.build_world()
            self.state = GameState.PLAYING
        elif selection == frame.Option.RESTART:
            self.restart()
            self.state = GameState.PLAYING
        elif selection == frame.Option.EXIT:
            self.in_game = False

        record.save(level=self.level + 1)

    def loss(self):
        # 背景色
        screen.fill(self.background)
        selection = self.game_loss.update(screen)

        # 根據不同選項，對遊戲狀態進行更新
        if selection == frame.Option.RESTART:
            self.restart()
            sounds.dead.stop()
            sounds.bgm.play(sounds.LOOP_FOREVER)
            self.state = GameState.PLAYING
        elif selection == frame.Option.EXIT:
            self.in_game = False

    def gameOver(self):
        sounds.bgm.stop()
        if self.player.DeadAnime():
            self.state = GameState.LOSS

    # 按鍵輸入處理
    def key_handle(self):
        if self.player.isdead():
            return

        keys = pygame.key.get_pressed()

        # game pause，設定遊戲狀態為pause
        if keys[pygame.K_ESCAPE]:
            self.state = GameState.PAUSE

    # 建構地圖
    def CountInitialPoint(self):
        x , y = 0 , 0
        for char in self.map_:
            if char == "\n":  # 換行
                y += parameter.IMG_SIZE
                Map_halfwidth = x / 2
                x = 0
            elif char == "H" or "#" or "." or "$" or "%" or "!" or "P" or "@":
                x += parameter.IMG_SIZE
            elif char == " ":
                pass
            else:
                logging.warning(f"unknow idetifier {char} in map {self.level}, ignored.")
        Map_halfheight = y / 2
        initial_height = parameter.WIN_HEIGHT / 2 - Map_halfheight
        initial_width = parameter.WIN_WIDTH / 2 - Map_halfwidth
        return [initial_width , initial_height]

    def build_world(self):
        self.borders = pygame.sprite.Group()
        self.boxes = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.goals = pygame.sprite.Group()
        self.guards = pygame.sprite.Group()
        self.portals = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.portals = pygame.sprite.Group()
        self.map_ = maps.get_map(self.level)

        initialList =  self.CountInitialPoint()
        x , y = initialList[0] , initialList[1]

        for char in self.map_:
            if char == "\n":  # 換行
                y += parameter.IMG_SIZE
                x = initialList[0]
            elif char == "H":  # 邊界
                self.borders.add(element.Border(x, y))
            elif char == "#":  # 牆
                self.walls.add(element.Wall(x, y))
            elif char == ".":  # 終點
                self.goals.add(element.Goal(x, y))
            elif char == "$":  # 箱子
                self.boxes.add(element.Box(x, y))
            elif char == "%":  # 終點上有箱子
                self.goals.add(element.Goal(x, y))
                self.boxes.add(element.Box(x, y))
            elif char == "!":  # 警衛
                self.guards.add(element.Guard(x, y))
            elif char == "P":
                self.portals.add(element.Portal(x, y))
            elif char == "@":  # 玩家（初始）位置
                self.player = element.Player(x, y)
            elif char == " ":
                pass
            else:
                logging.warning(f"unknow idetifier {char} in map {self.level}, ignored.")
            x += parameter.IMG_SIZE

        # dict
        self.all_objects = {
            element.ObjectID.BORDER: self.borders,
            element.ObjectID.BOX: self.boxes,
            element.ObjectID.BULLET: self.bullets,
            element.ObjectID.GOAL: self.goals,
            element.ObjectID.GUARD: self.guards,
            element.ObjectID.PORTAL: self.portals,
            element.ObjectID.WALL: self.walls,
            element.ObjectID.PLAYER: self.player,
            element.ObjectID.PORTAL: self.portals,
        }

    # 遊戲邏輯處理，更新遊戲狀態
    def update_world(self):
        self.bullets.update(self.all_objects)
        self.portals.update()
        

        if self.state != GameState.LOSING:
            self.guards.update(self.all_objects)

        if not self.debug:
            self.mask.update(self.player)

        # 根據玩家狀態決定遊戲狀態
        state = self.player.update(self.all_objects)
        if state == element.PlayerState.LOSING:
            self.state = GameState.LOSING
        elif state == element.PlayerState.OVER:
            self.state = GameState.LOSS
        elif state == element.PlayerState.WON:
            self.score = self.score + 100 + (100 - int((self.Timer.get_elapsed() / 20)) * 10)
            self.state = GameState.VICTORY

    # 畫在螢幕上
    def draw_world(self):
        # 背景色
        screen.fill(self.background)

        self.borders.draw(screen)
        self.walls.draw(screen)
        self.goals.draw(screen)
        self.guards.draw(screen)
        self.portals.draw(screen)
        self.boxes.draw(screen)
        self.bullets.draw(screen)
        self.player.draw(screen)

        # 如果mask啟用(非debug模式)，畫在player身邊
        if not self.debug:
            self.mask.draw(screen)       

    # 在螢幕畫出需要顯示的資訊
    def info_show(self):
        text = f"Ammos: {self.player.ammos()}"
        info_font.render_to(screen, (4,4) , text , (255,255,255), None , size = 30)
        

        text = "Time: " + time.strftime("%H:%M:%S", time.gmtime(self.Timer.get_elapsed()))
        info_font.render_to(screen,(200 , 4) , text , (255,255,255) , None, size= 30)

        text = f"Score: {self.score}" 
        info_font.render_to(screen,(600 , 4) , text , (255,255,255) , None, size= 30)

        text = f"Box_In_Goal: {self.player.Numberofbox_in_goal(self.all_objects)}" 
        info_font.render_to(screen,(900 , 4) , text , (255,255,255) , None, size= 30)

        

        # debug用資訊
        if self.debug:
            text = "<debug>fps: {:.1f}".format(self.ticker.get_fps())
            text = self.display_font.render(text, True, (0, 0, 0))
            screen.blit(text, (WIN_WIDTH - 250, WIN_HEIGHT - 100))

            objects = 0
            for _, v in self.all_objects.items():
                try:
                    objects += len(v)
                except Exception:
                    pass
            text = "<debug>objects: {}".format(objects)
            text = self.display_font.render(text, True, (0, 0, 0))
            screen.blit(text, (WIN_WIDTH - 250, WIN_HEIGHT - 50))

        # tutorial SS
        if self.level == maps.TUTORIAL:
            tutorial_text_0 = "<遊戲教學>"
            tutorial_text_1 = "這是一個密室逃脫"
            tutorial_text_2 = "要逃離這個房間必須把箱子推進格子"
            tutorial_text_4 = "這個藍藍的裝置是傳送器"
            tutorial_text_5 =" 踏進去能跳躍到別的房間"
            tutorial_text_6 = "要小心警衛！被摸到就完了!"
            tutorial_text_7 = "但別擔心，你並非手無寸鐵"
            tutorial_text_8 = "按下空白鍵能開槍"
            tutorial_text_9 = "只要推進一個箱子就能補充彈藥"
            tutorial_text_10 = "遇上警衛就請他吃子彈吧!"
            tutorial_text_11 = "牆的隔壁就是警衛"
            tutorial_text_12="準備好就傳送吧"
            tutorial_text_13 = "一共有9道謎題"
            tutorial_text_14 ="全部解完就能逃離這裡"
            tutorial_text_15 = "祝你好運:D"

            tutorial_text_0 = self.display_font.render(tutorial_text_0, True, (0, 0, 0))
            screen.blit(tutorial_text_0, (WIN_WIDTH/2 - 700, WIN_HEIGHT/3 -220))
            tutorial_text_1 = self.display_font.render(tutorial_text_1, True, (0, 0, 0))
            screen.blit(tutorial_text_1, (WIN_WIDTH/2 - 500, WIN_HEIGHT/3 -195))
            tutorial_text_2 = self.display_font.render(tutorial_text_2, True, (0, 0, 0))
            screen.blit(tutorial_text_2, (WIN_WIDTH/2 - 200, WIN_HEIGHT/3 -220))
            tutorial_text_4 = self.display_font.render(tutorial_text_4, True, (0, 0, 0))
            screen.blit(tutorial_text_4, (WIN_WIDTH/2 - 120, WIN_HEIGHT/3  -100))
            tutorial_text_5 = self.display_font.render(tutorial_text_5, True, (0, 0, 0))
            screen.blit(tutorial_text_5, (WIN_WIDTH/2 - 550, WIN_HEIGHT/3  -70))

            tutorial_text_6 = self.display_font.render(tutorial_text_6, True, (0, 0, 0))
            screen.blit(tutorial_text_6, (WIN_WIDTH/2 - 650, WIN_HEIGHT/3 +10 ))
            tutorial_text_7 = self.display_font.render(tutorial_text_7, True, (0, 0, 0))
            screen.blit(tutorial_text_7, (WIN_WIDTH/2 - 650, WIN_HEIGHT/3 +50 ))
            tutorial_text_8 = self.display_font.render(tutorial_text_8, True, (0, 0, 0))
            screen.blit(tutorial_text_8, (WIN_WIDTH/2 - 650, WIN_HEIGHT/3 +75 ))
            tutorial_text_9 = self.display_font.render(tutorial_text_9, True, (0, 0, 0))
            screen.blit(tutorial_text_9, (WIN_WIDTH/2 - 650, WIN_HEIGHT/3 +100 ))

            tutorial_text_10 = self.display_font.render(tutorial_text_10, True, (0, 0, 0))
            screen.blit(tutorial_text_10, (WIN_WIDTH/2 - 50, WIN_HEIGHT/3 +10 ))
            tutorial_text_11 = self.display_font.render(tutorial_text_11, True, (0, 0, 0))
            screen.blit(tutorial_text_11, (WIN_WIDTH/2 - 50, WIN_HEIGHT/3 +50 ))
            tutorial_text_12 = self.display_font.render(tutorial_text_12, True, (0, 0, 0))
            screen.blit(tutorial_text_12, (WIN_WIDTH/2 -50, WIN_HEIGHT/3 +100 ))

            tutorial_text_13 = self.display_font.render(tutorial_text_13, True, (0, 0, 0))
            screen.blit(tutorial_text_13, (WIN_WIDTH/2 -450, WIN_HEIGHT/3 +350 ))
            tutorial_text_14 = self.display_font.render(tutorial_text_14, True, (0, 0, 0))
            screen.blit(tutorial_text_14, (WIN_WIDTH/2 -350, WIN_HEIGHT/3 +410 ))
            tutorial_text_15 = self.display_font.render(tutorial_text_15, True, (0, 0, 0))
            screen.blit(tutorial_text_15, (WIN_WIDTH/2 -50, WIN_HEIGHT/3 +340 ))

    def restart(self):
        self.Timer.__init__()
        self.build_world()


if __name__ == "__main__":
    game = Game(level=0, debug=True)
    game.run_game()
