#!/bin/env python3
import pygame
import pygame.time
import time
import enum

# 設定視窗大小
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

import record
import frame
import maps
import element
import sounds
import parameter

WIN_WIDTH, WIN_HEIGHT = parameter.WIN_WIDTH, parameter.WIN_HEIGHT


class GameState(enum.Enum):
    PLAYING = 0
    PAUSE = 1
    VICTORY = 2
    LOSING = 3
    LOSS = 4


class Game():
    """
    level 表示第幾關
    mask 是用來增加遊戲難度的物件，mask_enabled決定mask是否啟用，
    debug時不啟用mask
    """

    def __init__(self, level, mask_enabled=True):
        self.screen = screen
        self.ticker = pygame.time.Clock()
        self.background = (230, 230, 200)  # 背景顏色
        self.level = level
        self.build_world()
        self.key_cooldown = time.time()
        self.game_pause = frame.Pause()  # pause frame
        self.game_victory = frame.Victory()
        self.game_loss = frame.Loss()  # 死亡後的選單
        self.state = GameState.PLAYING

        self.count = pygame.USEREVENT + 1  # 時間事件
        self.counts = 0  # 時間

        self.display_font = pygame.font.Font(parameter.FONT, 24)

        self.mask_enabled = mask_enabled
        if self.mask_enabled:
            player_x, player_y = self.player.pos()
            self.mask = element.Mask(player_x, player_y)

    def run_game(self):
        sounds.bgm.play(sounds.LOOP_FOREVER)
        pygame.time.set_timer(self.count, 1000)
        self.in_game = True
        while self.in_game:
            # 基礎事件
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.in_game = False
                elif event.type == self.count:
                    self.counts = self.counts + 1

            if self.state == GameState.PLAYING:
                self.update_world()
                self.key_handle()
                self.draw_world()
            elif self.state == GameState.PAUSE:
                self.pause()
            elif self.state == GameState.VICTORY:
                self.victory()
            elif self.state == GameState.LOSING:
                self.gameOver()
                self.draw_world()
            elif self.state == GameState.LOSS:
                self.loss()

            self.info_show()
            pygame.display.update()
            self.ticker.tick(60)  # 60 fps

        pygame.quit()

    def pause(self):
        # 背景色
        self.screen.fill(self.background)
        selection = self.game_pause.update(self.screen)
        if selection == frame.Option.RESUME:
            self.state = GameState.PLAYING
        elif selection == frame.Option.RESTART:
            self.restart()
            self.state = GameState.PLAYING
        elif selection == frame.Option.EXIT:
            self.in_game = False

    def victory(self):
        self.screen.fill(self.background)
        selection = self.game_victory.update(self.screen)
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

    def gameOver(self):
        '''
        gameOverFont = pygame.font.SysFont('arial.ttf',54) #遊戲結束字體和大小
        gameOverSurf = gameOverFont.render('Game Over!', True, (255, 255, 255)) #遊戲結束內容顯示
        gameOverRect = gameOverSurf.get_rect()
        gameOverRect.midtop = (300, 10) #顯示位置
        playSurface.blit(gameOverSurf, gameOverRect)
        pygame.display.flip() #刷新顯示介
        time.sleep(5) #休眠五秒鐘自動退出介面
        pygame.quit()
        '''
        sounds.bgm.stop()
        if self.player.DeadAnime():
            self.state = GameState.LOSS

    def loss(self):
        self.screen.fill(self.background)
        selection = self.game_loss.update(self.screen)
        if selection == frame.Option.RESTART:
            self.restart()
            sounds.dead.stop()
            sounds.bgm.play(sounds.LOOP_FOREVER)
            self.state = GameState.PLAYING
        elif selection == frame.Option.EXIT:
            self.in_game = False

    # 按鍵輸入處理
    def key_handle(self):
        if self.player.isdead():
            return

        keys = pygame.key.get_pressed()
        # 玩家輸入
        self.player.handle_keys(keys, self.all_objects)

        # game pause
        if keys[pygame.K_ESCAPE]:
            self.state = GameState.PAUSE

    # 建構地圖
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

        x, y = 0, 0
        for _, v in enumerate(self.map_):
            if v == "\n":  # 換行
                y += 40
                x = 0
            elif v == "H":  # 邊界
                self.borders.add(element.Border(x, y))
            elif v == "#":  # 牆
                self.walls.add(element.Wall(x, y))
            elif v == ".":  # 終點
                self.goals.add(element.Goal(x, y))
            elif v == "$":  # 箱子
                self.boxes.add(element.Box(x, y))
            elif v == "%":  # 終點上有箱子
                self.goals.add(element.Goal(x, y))
                self.boxes.add(element.Box(x, y))
            elif v == "!":  # 警衛
                self.guards.add(element.Guard(x, y))
            elif v == "P":
                self.portals.add(element.Portal(x, y))
            elif v == "@":  # 玩家（初始）位置
                self.player = element.Player(x, y, 0)
            elif v == " ":
                pass
            else:
                print(f"unknow idetifier {v} in map {self.level}, ignored.")
            x += 40

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
        self.guards.update(self.all_objects)
        self.portals.update()

        if self.mask_enabled:
            self.mask.update(self.player)

        # 玩家死亡
        if self.player.isdead():
            self.state = GameState.LOSING

        if self.player.is_won(self.all_objects):
            self.state = GameState.VICTORY

    # 畫在螢幕上

    def draw_world(self):
        # 背景色
        self.screen.fill(self.background)

        self.borders.draw(self.screen)
        self.walls.draw(self.screen)
        self.goals.draw(self.screen)
        self.guards.draw(self.screen)
        self.portals.draw(self.screen)
        self.boxes.draw(self.screen)
        self.bullets.draw(self.screen)
        self.player.draw(self.screen)

        # 如果mask啟用，畫在player身邊
        if self.mask_enabled:
            self.mask.draw(self.screen)
       


    # 在螢幕畫出需要顯示的資訊
    def info_show(self):
        text = f"ammos: {self.player.ammos()}"
        text = self.display_font.render(text, True, (0, 0, 0))
        self.screen.blit(text, (WIN_WIDTH - 180, WIN_HEIGHT - 200))

        text = "Time: " + time.strftime("%H:%M:%S", time.gmtime(self.counts))
        text = self.display_font.render(text, True, (0, 0, 0))
        self.screen.blit(text, (WIN_WIDTH - 200, WIN_HEIGHT - 150))

        # debug用資訊
        text = "<debug>fps: {:.1f}".format(self.ticker.get_fps())
        text = self.display_font.render(text, True, (0, 0, 0))
        self.screen.blit(text, (WIN_WIDTH - 250, WIN_HEIGHT - 100))
        #tutorial 
        if self.level==10:
            tutorial_text_0="                   <遊戲教學>"
            tutorial_text_1="1.方向鍵移動，按下space可以開槍射擊，若擊中警衛可將其清除。"
            tutorial_text_2="2.靠近傳送門可以使用空間跳躍。"
            tutorial_text_3="3.把箱子推到框框內就獲勝囉"
            tutorial_text_4="4.Good luck:D"
            tutorial_text_0=self.display_font.render(tutorial_text_0,True,(0,0,0))
            self.screen.blit(tutorial_text_0, (WIN_WIDTH /2-500, WIN_HEIGHT/3+360))
            tutorial_text_1=self.display_font.render(tutorial_text_1,True,(0,0,0))
            self.screen.blit(tutorial_text_1, (WIN_WIDTH /2-500, WIN_HEIGHT/3+400))
            tutorial_text_2=self.display_font.render(tutorial_text_2,True,(0,0,0))
            self.screen.blit(tutorial_text_2, (WIN_WIDTH /2-500, WIN_HEIGHT/3+430))
            tutorial_text_3=self.display_font.render(tutorial_text_3,True,(0,0,0))
            self.screen.blit(tutorial_text_3, (WIN_WIDTH /2-500, WIN_HEIGHT/3+460))
            tutorial_text_4=self.display_font.render(tutorial_text_4,True,(0,0,0))
            self.screen.blit(tutorial_text_4, (WIN_WIDTH /2-500, WIN_HEIGHT/3+490))
        # debug用資訊
        objects = 0
        for _, v in self.all_objects.items():
            try:
                objects += len(v)
            except Exception:
                pass
        text = "<debug>objects: {}".format(objects)
        text = self.display_font.render(text, True, (0, 0, 0))
        self.screen.blit(text, (WIN_WIDTH - 250, WIN_HEIGHT - 50))

    def restart(self):
        self.build_world()


if __name__ == "__main__":
    # debugging now, mask_enabled should be True
    game = Game(level=1, mask_enabled=False)
    game.run_game()
