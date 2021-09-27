import pygame

# 畫面長寬
WIN_WIDTH, WIN_HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h

# 圖片
IMG_SIZE = 40  # pixel

# 箱子
BOX_SIZE = 24  # 箱子圖片大小
BOX_GAP = 24  # 箱子碰撞偵測距離
BOX_OFFSET = (IMG_SIZE - BOX_SIZE) // 2  # 箱子顯示的偏移量

# 傳送門
PORTAL_SIZE = 35
PORTAL_DELAY = 4  # (frame)

# 玩家
INIT_BULLET_NUM = 10

# 物體移動速度
BULLET_VELOCITY = 10  # pixel
PLAYER_VELOCITY = 4  # pixel
GUARD_VELOCITY = 4
GUARD_INERITA = 45  # 警衛朝同一方向移動的時間（單位:frame）
GUARD_SLEEP = 20  # 警衛變換方向時留在原地的時間（單位:frame）

# 避免按鍵重複觸發的冷卻時間
BULLET_COOLDOWN = 0.2  # sec
KEY_COOLDOWN = 0.5
PAUSE_KEY_COOLDOWN = 0.1

# 死亡Frame
DEAD_DELAY = 2

# 字體
# open source font, see https://github.com/fontworks-fonts/Klee
FONT = "data/font/KleeOne-Regular.ttf"
# open source font, see https://github.com/justfont/open-huninn-font
BTN_FONT = "data/font/jf-openhuninn-1.0.ttf"
# open source font, see https://github.com/fontworks-fonts/Rampart
TITLE_FONT = "data/font/RampartOne-Regular.ttf"
