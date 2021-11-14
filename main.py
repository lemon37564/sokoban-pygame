import game
import logging
import pygame
import maps
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
bigfont = pygame.font.Font(parameter.INFO_FONT, 55)

text_random_level_in_progress = bigfont.render('Level generation in progress... ', True, (0, 0, 0))
text_2 = bigfont.render("this may take up to a minute", True, (0, 0, 0))


def menu():
    for btn in home_page_btn:
        btn.unhide()
    for btn in sub_menu_btns:
        btn.hide()
    window.set_background_color((210, 200, 200))

def submenu():
    for btn in home_page_btn:
        btn.hide()
    for btn in sub_menu_btns:
        btn.unhide()
    window.set_background_color((200, 200, 0))

def hide_everything():
    for btn in home_page_btn:
        btn.hide()
    for btn in sub_menu_btns:
        btn.hide()
    window.set_background_color((200, 200, 0))

def start_game(level_selected):
    hide_everything()
    screen.fill((210, 200, 200))
    
    if maps.level_is_random(level_selected):
        screen.blit(text_random_level_in_progress, (width/2-350, height/3+20))
        screen.blit(text_2, (width/2-350, height/3+90))
        pygame.display.update()

    g = game.Game(level=level_selected, debug=False)
    g.run_game()
   
    menu()
    sounds.stop_everything()


LEVEL_BTN_SIZE = (300, 60)

V1, V2, V3 = height/3, height/3+80, height/3+160
H1, H2, H3 = width/2-350, width/2, width/2+350

level_1_btn = window.Button(font=smallfont, text="Level 1", position=(H1, V1), size=LEVEL_BTN_SIZE)
level_1_btn.connect(start_game, args=(11,))

level_2_btn = window.Button(font=smallfont, text="Level 2", position=(H1, V2), size=LEVEL_BTN_SIZE)
level_2_btn.connect(start_game, args=(2,))

level_3_btn = window.Button(font=smallfont, text="Level 3", position=(H1, V3), size=LEVEL_BTN_SIZE)
level_3_btn.connect(start_game, args=(3,))

level_4_btn = window.Button(font=smallfont, text="Level 4", position=(H2, V1), size=LEVEL_BTN_SIZE)
level_4_btn.connect(start_game, args=(4,))

level_5_btn = window.Button(font=smallfont, text="Level 5", position=(H2, V2), size=LEVEL_BTN_SIZE)
level_5_btn.connect(start_game, args=(5,))
level_5_btn.hide()

level_6_btn = window.Button(font=smallfont, text="Level 6", position=(H2, V3), size=LEVEL_BTN_SIZE)
level_6_btn.connect(start_game, args=(6,))

level_7_btn = window.Button(font=smallfont, text="Level 7", position=(H3, V1), size=LEVEL_BTN_SIZE)
level_7_btn.connect(start_game, args=(7,))

level_8_btn = window.Button(font=smallfont, text="Level 8", position=(H3, V2), size=LEVEL_BTN_SIZE)
level_8_btn.connect(start_game, args=(8,))

level_9_btn = window.Button(font=smallfont, text="Level 9", position=(H3, V3), size=LEVEL_BTN_SIZE)
level_9_btn.connect(start_game, args=(9,))

random_6x6_btn = window.Button(font=smallfont, text="6x6 random level", position=(H2, V3+100), size=(width/2, 60))
random_6x6_btn.connect(start_game, args=(maps.RANDOM_6X6,))

random_7x7_btn = window.Button(font=smallfont, text="7x7 random level", position=(H2, V3+180), size=(width/2, 60))
random_7x7_btn.connect(start_game, args=(maps.RANDOM7X7,))

random_8x8_btn = window.Button(font=smallfont, text="8x8 random level", position=(H2, V3+260), size=(width/2, 60))
random_8x8_btn.connect(start_game, args=(maps.RANDOM8X8,))

back_menu_btn = window.Button(font=smallfont, text="back", position=(H2, V3+340), size=(width/2, 60))
back_menu_btn.connect(menu)

sub_menu_btns = [level_1_btn, level_2_btn, level_3_btn, level_4_btn, level_5_btn, level_6_btn,
    level_7_btn, level_8_btn, level_9_btn, random_6x6_btn, random_7x7_btn, random_8x8_btn, back_menu_btn]

start_btn = window.Button(font=bigfont, text="start game", position=(width/2, height/3+100), size=(400, 80))
start_btn.connect(submenu)

tutorial_btn = window.Button(font=bigfont, text="tutorial", position=(width/2, height/3+220), size=(400, 80))
tutorial_btn.connect(start_game, args=(maps.TUTORIAL,))

exit_btn = window.Button(font=bigfont, text="quit", position=(width/2, height/3+340), size=(400, 80))
exit_btn.connect(pygame.quit)

home_page_btn = [start_btn, tutorial_btn, exit_btn]

img_title = pygame.image.load('data/img/menu/gameTitle2.png')
window.show_image(img_title, (width/2, height/5))

img_player = pygame.image.load('data/img/menu/PlayerThreeRight.png')
img_player = pygame.transform.scale(img_player, (140, 140))
window.show_image(img_player, (400, 500))

if __name__ == "__main__":
    menu()
    window.run()
