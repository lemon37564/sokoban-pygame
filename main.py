import time
import game
import logging
import pygame
import parameter
import sounds

import window
logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)


pygame.font.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

width = screen.get_width()
height = screen.get_height()

# defining fonts
smallfont = pygame.font.Font(parameter.INFO_FONT, 35)
bigfont = pygame.font.Font(parameter.INFO_FONT, 50)

text_random_level_in_progress = bigfont.render('Level generation in progress... ', True, (0, 0, 0))
text_2 = bigfont.render("for 8x8 maps this may take up to a minute", True, (0, 0, 0))


def menu():
    for btn in level_btns:
        btn.hide()
    for btn in home_page_btn:
        btn.unhide()
    window.set_background_color((210, 200, 200))

def submenu():
    for btn in level_btns:
        btn.unhide()
    for btn in home_page_btn:
        btn.hide()
    window.set_background_color((200, 200, 0))

def hide_everything():
    level_1_btn.hide()
    level_2_btn.hide()
    level_3_btn.hide()
    level_4_btn.hide()
    level_5_btn.hide()
    level_6_btn.hide()
    level_7_btn.hide()
    level_8_btn.hide()
    level_9_btn.hide()
    random_6x6_btn.hide()
    random_7x7_btn.hide()
    random_8x8_btn.hide()
    start_btn.hide()
    tutorial_btn.hide()
    exit_btn.hide()
    window.set_background_color((200, 200, 0))

def start_game(level_selected, random_level_size):
    hide_everything()
    screen.fill((210, 200, 200))
    
    if(level_selected > 999):
        screen.blit(text_random_level_in_progress, (width/2-350, height/3+20))
        screen.blit(text_2, (width/2-450, height/3+90))
        pygame.display.update()
        g = game.Game(level=level_selected, random_level_size=random_level_size, debug=False)
        g.run_game()
    else:  # normal level 1 to 9
        g = game.Game(level=level_selected, random_level_size=random_level_size, debug=False)
        g.run_game()
   
    menu()
    sounds.stop_everything()


LEVEL_BTN_SIZE = (300, 60)

V1, V2, V3 = height/3+50, height/3+150, height/3+250
H1, H2, H3 = width/2-350, width/2, width/2+350

level_1_btn = window.Button(font=smallfont, text="Level 1", position=(H1, V1), size=LEVEL_BTN_SIZE)
level_1_btn.connect(start_game, args=(1, 0))
level_1_btn.hide()

level_2_btn = window.Button(font=smallfont, text="Level 2", position=(H1, V2), size=LEVEL_BTN_SIZE)
level_2_btn.connect(start_game, args=(2, 0))
level_2_btn.hide()

level_3_btn = window.Button(font=smallfont, text="Level 3", position=(H1, V3), size=LEVEL_BTN_SIZE)
level_3_btn.connect(start_game, args=(3, 0))
level_3_btn.hide()

level_4_btn = window.Button(font=smallfont, text="Level 4", position=(H2, V1), size=LEVEL_BTN_SIZE)
level_4_btn.connect(start_game, args=(4, 0))
level_4_btn.hide()

level_5_btn = window.Button(font=smallfont, text="Level 5", position=(H2, V2), size=LEVEL_BTN_SIZE)
level_5_btn.connect(start_game, args=(5, 0))
level_5_btn.hide()

level_6_btn = window.Button(font=smallfont, text="Level 6", position=(H2, V3), size=LEVEL_BTN_SIZE)
level_6_btn.connect(start_game, args=(6, 0))
level_6_btn.hide()

level_7_btn = window.Button(font=smallfont, text="Level 7", position=(H3, V1), size=LEVEL_BTN_SIZE)
level_7_btn.connect(start_game, args=(7, 0))
level_7_btn.hide()

level_8_btn = window.Button(font=smallfont, text="Level 8", position=(H3, V2), size=LEVEL_BTN_SIZE)
level_8_btn.connect(start_game, args=(8, 0))
level_8_btn.hide()

level_9_btn = window.Button(font=smallfont, text="Level 9", position=(H3, V3), size=LEVEL_BTN_SIZE)
level_9_btn.connect(start_game, args=(9, 0))
level_9_btn.hide()

random_6x6_btn = window.Button(font=smallfont, text="6x6 random level", position=(H2, V3+100), size=(width/2, 60))
random_6x6_btn.connect(start_game, args=(1000, 6))
random_6x6_btn.hide()

random_7x7_btn = window.Button(font=smallfont, text="7x7 random level", position=(H2, V3+200), size=(width/2, 60))
random_7x7_btn.connect(start_game, args=(1000, 7))
random_7x7_btn.hide()

random_8x8_btn = window.Button(font=smallfont, text="8x8 random level", position=(H2, V3+300), size=(width/2, 60))
random_8x8_btn.connect(start_game, args=(1000, 8))
random_8x8_btn.hide()

level_btns = [level_1_btn, level_2_btn, level_3_btn, level_4_btn, level_5_btn,
    level_6_btn, level_7_btn, level_8_btn, level_9_btn, random_6x6_btn, random_7x7_btn, random_8x8_btn]

start_btn = window.Button(font=bigfont, text="start game", position=(width/2, height/3+100), size=(400, 80))
start_btn.connect(submenu)
start_btn.hide()

tutorial_btn = window.Button(font=bigfont, text="tutorial", position=(width/2, height/3+220), size=(400, 80))
tutorial_btn.connect(start_game, args=(0, 0))
tutorial_btn.hide()

exit_btn = window.Button(font=bigfont, text="quit", position=(width/2, height/3+340), size=(400, 80))
exit_btn.connect(pygame.quit)
exit_btn.hide()

home_page_btn = [start_btn, tutorial_btn, exit_btn]

img_title = pygame.image.load('data/img/menu/gameTitle2.png')
window.show_image(img_title, (width/2, height/5))

img_player = pygame.image.load('data/img/menu/PlayerThreeRight.png')
img_player = pygame.transform.scale(img_player, (140, 140))
window.show_image(img_player, (400, 500))

if __name__ == '__main__':
    menu()
