import time

import pygame
import pygame.event, pygame.mouse, pygame.display


BTN_COLOR = (167, 147, 0) # 按鈕背景顏色
BTN_SELECTED_COLOR = (255, 255, 20) # 選中的按鈕的顏色
BTN_DISABLED_COLOR = (80, 80, 80)

COLOR_BLACK = (0, 0, 0)
COLOR_GRAY = (50, 50, 50)

MAX_BIAS = 6
BIAS_MOVE = 2

BUTTON_COOL_DOWN_SEC = 0.5

screen = pygame.display.set_mode((800, 600))

global __widgets
__widgets = list()
global __bg_color
__bg_color = (0, 0, 0)
global __show_imgs
__show_imgs = dict()

def add(widget):
    __widgets.append(widget)

def remove(widget):
    __widgets.remove(widget)

def run():
    while True:
        screen.fill(__bg_color)

        for img, pos in __show_imgs.items():
            screen.blit(img, pos)

        mouse_clicked = False
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            mouse_clicked = mouse_clicked or (event.type == pygame.MOUSEBUTTONDOWN)

        for widget in __widgets:
            cursor_pos = pygame.mouse.get_pos()
            widget.event_handle(cursor_pos, mouse_clicked)

        pygame.display.update()
        time.sleep(0.025)

def set_background_color(color):
    global __bg_color
    __bg_color = color

def show_image(img: pygame.Surface, position: tuple):
    width, height = img.get_size()
    pos_x, pos_y = position
    __show_imgs[img] = (pos_x - width/2, pos_y - height/2)


class Button():
    '''
    type of font = pygame.font.Font  \n
    text is the message of the button \n
    position indicates where the button should be, type is (int, int) \n
    size indicates the width and height of the button, type is (int, int)
    '''
    def __init__(self, font: pygame.font.Font, text: str, position: tuple, size: tuple):
        self.set_size(size)
        self.set_position(position)
        self.__center = position
        self.__text = text
        self.__font = font

        self.__bind_func = None
        self.__args = None
        self.__enabled = True
        self.__hide = False
        self.__last_click = time.time()
        self.__bias = 0

        add(self)

    def connect(self, func, args=()):
        '''
        connect to a function which will be execute after button is clicked \n
        you can pass argument into that function \n
        noticed that if the length of arguments v.s. the function needed are different, it rasies an error
        '''
        self.__bind_func = func
        self.__args = args

    def enable(self):
        '''make the button sensitive'''
        self.__enabled = True
    
    def disable(self):
        '''make the button not sensitive'''
        self.__enabled = False

    def hide(self):
        self.__hide = True

    def unhide(self):
        self.__hide = False

    def set_position(self, position: tuple):
        '''set the center position of the button'''
        center_x, center_y = position
        self.__pos_x, self.__pos_y = center_x - self.__width//2, center_y - self.__height//2

    def set_size(self, size: tuple):
        self.__width, self.__height = size

    def set_text(self, text):
        self.__text = text

    def get_text(self):
        return self.__text

    def delete(self):
        remove(self)
        del self

    def event_handle(self, cursor_pos: list, mouse_clicked: bool):
        if self.__hide:
            return
        if self.__is_hover(cursor_pos):
            self.__render(selected=True)
            self.__bias += BIAS_MOVE # 模擬動畫效果，以逐漸的方式移動
            if self.__bias > MAX_BIAS:
                self.__bias = MAX_BIAS
            if mouse_clicked and self.__enabled and (time.time() - self.__last_click > BUTTON_COOL_DOWN_SEC):
                self.__last_click = time.time()
                if len(self.__args) == 0:
                    self.__bind_func()
                else:
                    self.__bind_func(*self.__args)
        else:
            self.__render(selected=False)
            self.__bias -= BIAS_MOVE # 模擬動畫效果，以逐漸的方式移動
            if self.__bias < 0:
                self.__bias = 0
        
    def __render(self, selected: bool):
        if not self.__enabled:
            self.__draw(BTN_DISABLED_COLOR, float_=False)
        elif selected:
            self.__draw_shadow()
            self.__draw(BTN_SELECTED_COLOR, float_=True)
        else:
            self.__draw(BTN_COLOR, float_=False)

    def __is_hover(self, cursor_pos: list) -> bool:
        if not self.__enabled:
            return False 
        cursor_x, cursor_y = cursor_pos[0], cursor_pos[1]
        return self.__pos_x <= cursor_x and cursor_x <= self.__pos_x + self.__width and \
            self.__pos_y <= cursor_y and cursor_y <= self.__pos_y + self.__height

    def __draw(self, button_color, float_: bool):
        if float_:
            center_x, center_y = self.__center
            center = (center_x - self.__bias, center_y - self.__bias)
        else:
            center = self.__center

        btn = pygame.Rect(0, 0, self.__width, self.__height) # 按鈕的背景
        btn.center = center
        pygame.draw.rect(screen, button_color, btn, border_radius=10)

        edge = pygame.Rect(0, 0, self.__width, self.__height) # 按鈕的邊框
        edge.center = center
        pygame.draw.rect(screen, COLOR_BLACK, edge, width=2, border_radius=10)

        text = self.__font.render(self.__text, True, COLOR_BLACK) # 按鈕的文字
        text_rect = text.get_rect(center=center)
        screen.blit(text, text_rect)

    def __draw_shadow(self):
        shadow = pygame.Rect(0, 0, self.__width, self.__height) # draw shadow 營造立體感
        shadow.center = self.__center
        pygame.draw.rect(screen, COLOR_GRAY, shadow, border_radius=10)


if __name__ == "__main__":
    # 初始化
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont('Corbel', 35)

    # 以下為範例
    def pressed(level):
        print(f"you choosed: {level}")

    test = Button(font, "level 1", (200, 100), (120, 60))
    test.connect(pressed, args=(1,))

    test2 = Button(font, "level 2", (400, 100), (120, 60))
    test2.connect(pressed, args=(2,))

    test3 = Button(font, "level 3", (600, 100), (120, 60))
    test3.connect(pressed, args=(3,))

    def pressed_disable(btn, msg):
        btn.disable()
        print("button disabled, message:", msg)

    if_pressed_disable = Button(font, "one time button", (200, 250), (240, 60))
    if_pressed_disable.connect(pressed_disable, args=(if_pressed_disable, "this is the second argument"))

    re_enable_btn = Button(font, "enable button", (600, 250), (240, 60))
    re_enable_btn.connect(if_pressed_disable.enable)

    remove_self = Button(font, "remove myself", (400, 350), (240, 60))
    remove_self.connect(remove_self.delete)

    quit = Button(font, "quit", position=(400, 500), size=(200, 80))
    quit.connect(exit)
    run()
