import pygame
import time

pygame.init()  # 初始化pygame
pygame.font.init()

import parameter

# 設定視窗大小
screen = pygame.display.set_mode((parameter.WIN_WIDTH, parameter.WIN_HEIGHT))
import element
import maps
import frame


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
        self.map_ = maps.get_map(level)
        self.build_world()
        self.key_cooldown = time.time()
        self.game_pause = frame.pause.Pause() # pause frame
        self.STW = False # stop the world (pause)

        self.display_font = pygame.font.SysFont("default", 32)

        self.mask_enabled = mask_enabled
        if self.mask_enabled:
            player_x, player_y = self.player.pos()
            self.mask = element.Mask(player_x, player_y)

    def run_game(self):
        in_game = True
        while in_game:
            # 基礎事件
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    in_game = False

            # 背景色
            self.screen.fill(self.background)
            
            if self.STW:
                selection = self.game_pause.update(self.screen)
                if selection == frame.pause.RESUME:
                    self.STW = False
                elif selection == frame.pause.RESTART:
                    self.restart()
                    self.STW = False
                elif selection == frame.pause.EXIT:
                    in_game = False
            else:
                self.update_world()
                self.key_handle()
                self.draw_world()
                self.screen.blit(self.player.img(), self.player.pos())

            # debug用資訊
            text = " fps: {:.1f}".format(self.ticker.get_fps())
            text = self.display_font.render(text, False, (0, 0, 0))
            self.screen.blit(text, (1440, 740))

            # debug用資訊
            text = " objects: {}".format(len(self.world))
            text = self.display_font.render(text, False, (0, 0, 0))
            self.screen.blit(text, (1440, 770))

            pygame.display.update()
            self.ticker.tick(60)  # 60 fps

        pygame.quit()


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
        self.player.DeadAnime()
        
        

        
    # 按鍵輸入處理
    def key_handle(self):
        keys = pygame.key.get_pressed()

        # player movement
        if keys[pygame.K_UP]:
            self.player.move(0, -parameter.PLAYER_VELOCITY, self.world)
            self.player.set_dir(element.direction.UP)
        elif keys[pygame.K_DOWN]:
            self.player.move(0, parameter.PLAYER_VELOCITY, self.world)
            self.player.set_dir(element.direction.DOWN)
        elif keys[pygame.K_LEFT]:
            self.player.move(-parameter.PLAYER_VELOCITY, 0, self.world)
            self.player.set_dir(element.direction.LEFT)
        elif keys[pygame.K_RIGHT]:
            self.player.move(parameter.PLAYER_VELOCITY, 0, self.world)
            self.player.set_dir(element.direction.RIGHT)

        # player attack
        if keys[pygame.K_SPACE]:
            if self.player.shoot():
                player_x, player_y = self.player.pos()
                player_dir = self.player.direction()
                self.world.append(element.Bullet(player_x, player_y, player_dir))

        # game pause
        if keys[pygame.K_ESCAPE]:
            self.STW = True

    # 建構地圖
    def build_world(self):
        self.world = []

        x, y = 0, 0
        for i, v in enumerate(self.map_):
            if v == "\n": # 換行
                y += 40
                x = 0
            elif v == "H": # 邊界
                self.world.append(element.Border(x, y))
            elif v == "#": # 牆
                self.world.append(element.Wall(x, y))
            elif v == ".": # 終點
                self.world.append(element.Goal(x, y))
            elif v == "$": # 箱子
                self.world.append(element.Box(x, y))
            elif v == "%": # 終點上有箱子
                self.world.append(element.Goal(x, y))
                self.world.append(element.Box(x, y))
            elif v == "!": # 警衛
                self.world.append(element.Guard(x, y))
            elif v == "@": # 玩家（初始）位置
                self.player = element.Player(x, y, 0)
                self.world.append(self.player)
            x += 40
        
        

    # 遊戲邏輯處理，更新遊戲狀態
    def update_world(self):
        for item in self.world:
            # 子彈位置更新
            if isinstance(item, element.Bullet):
                item.update(self.world)
            # 警衛移動
            elif isinstance(item, element.Guard):
                item.update(self.world)
        #玩家死亡
        if self.player.isdead() == True:
            self.gameOver()



    # 畫在螢幕上
    def draw_world(self):
        for obj in self.world:
            self.screen.blit(obj.img(), obj.pos())
        
        # 如果mask啟用，畫在player身邊
        if self.mask_enabled:
            player_x, player_y = self.player.pos()
            self.screen.blit(self.mask.img(), (player_x-self.mask.offset_x, player_y-self.mask.offset_y))

    def restart(self):
        self.build_world()


if __name__ == "__main__":
    # debugging now, mask_enabled should be True
    game = Game(level=9, mask_enabled=1)
    game.run_game()
