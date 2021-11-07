import logging
import pygame
from pygame import image

import window
logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)


pygame.font.init()

from game import Game
from pygame import mouse
from time import sleep


# initializing the constructor

# screen resolution
#res = (720,720)

# opens up a window
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# white color
color = (255, 255, 255)

# light shade of the button
color_light = (170, 170, 170)

# dark shade of the button
color_dark = (100, 100, 100)

# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
height = screen.get_height()

# defining fonts
smallfont = pygame.font.SysFont('Corbel', 35)
bigfont = pygame.font.SysFont('Corbel', 50)

# rendering a text written in
# this font
text_quit = smallfont.render('quit', True, color)
text_back_2_menu = smallfont.render('back to menu', True, color)
text_start = smallfont.render('start game', True, color)
text_help = smallfont.render('tutorial', True, color)
text_level_1 = smallfont.render('Level 1', True, color)
text_level_2 = smallfont.render('Level 2', True, color)
text_level_3 = smallfont.render('Level 3', True, color)
text_level_4 = smallfont.render('Level 4', True, color)
text_level_5 = smallfont.render('Level 5', True, color)
text_level_6 = smallfont.render('Level 6', True, color)
text_level_7 = smallfont.render('Level 7', True, color)
text_level_8 = smallfont.render('Level 8', True, color)
text_level_9 = smallfont.render('Level 9', True, color)
text_random_level_6x6=smallfont.render('Generate a random 6x6 level and Play!', True, color)
text_random_level_7x7=smallfont.render('Generate a random 7x7 level and Play!', True, color)
text_random_level_8x8=smallfont.render('Generate a random 8x8 level and Play!', True, color)
text_random_level_in_progress=smallfont.render('Level generation in progress, for 8x8 maps this may take up to a minute...', True, color)
#text_title = bigfont.render('Sokoban Stealer', True, color)

def start_game(level_selected, random_level_size):
    if(level_selected>999):
        screen.fill((200, 200,    0))
        screen.blit(text_random_level_in_progress, (width/2-500, height/3+20))
        pygame.display.update()
        game = Game(level=level_selected, random_level_size=random_level_size,debug=False)
        return game.run_game()
    else:#normal level 1 to 9
        game = Game(level=level_selected, random_level_size=random_level_size,debug=False)
        result=game.run_game()
        
        return result

level_1_btn = window.Button(font=smallfont, text="Level 1", position=(width/2-350, height/3+20), size=(200, 40))
level_1_btn.connect(start_game, args=(1, 0))
level_1_btn.hide()

level_2_btn = window.Button(font=smallfont, text="Level 2", position=(width/2-350, height/3+70), size=(200, 40))
level_2_btn.connect(start_game, args=(2, 0))
level_2_btn.hide()

level_3_btn = window.Button(font=smallfont, text="Level 3", position=(width/2-350, height/3+120), size=(200, 40))
level_3_btn.connect(start_game, args=(3, 0))
level_3_btn.hide()

level_4_btn = window.Button(font=smallfont, text="Level 4", position=(width/2-150, height/3+20), size=(200, 40))
level_4_btn.connect(start_game, args=(4, 0))
level_4_btn.hide()

level_5_btn = window.Button(font=smallfont, text="Level 5", position=(width/2-150, height/3+70), size=(200, 40))
level_5_btn.connect(start_game, args=(5, 0))
level_5_btn.hide()

level_6_btn = window.Button(font=smallfont, text="Level 6", position=(width/2-150, height/3+120), size=(200, 40))
level_6_btn.connect(start_game, args=(6, 0))
level_6_btn.hide()

level_7_btn = window.Button(font=smallfont, text="Level 7", position=(width/2+50, height/3+20), size=(200, 40))
level_7_btn.connect(start_game, args=(7, 0))
level_7_btn.hide()

level_8_btn = window.Button(font=smallfont, text="Level 8", position=(width/2+50, height/3+70), size=(200, 40))
level_8_btn.connect(start_game, args=(8, 0))
level_8_btn.hide()

level_9_btn = window.Button(font=smallfont, text="Level 9", position=(width/2+50, height/3+120), size=(200, 40))
level_9_btn.connect(start_game, args=(9, 0))
level_9_btn.hide()

random_6x6_btn = window.Button(font=smallfont, text="6x6 random level", position=(width/2-350, height/3+170), size=(200, 40))
random_6x6_btn.connect(start_game, args=(1000, 6))
random_6x6_btn.hide()

random_7x7_btn = window.Button(font=smallfont, text="7x7 random level", position=(width/2-350, height/3+220), size=(200, 40))
random_7x7_btn.connect(start_game, args=(1000, 7))
random_7x7_btn.hide()

random_8x8_btn = window.Button(font=smallfont, text="8x8 random level", position=(width/2-350, height/3+270), size=(200, 40))
random_8x8_btn.connect(start_game, args=(1000, 8))
random_8x8_btn.hide()

def page_2():
    level_1_btn.unhide()
    level_2_btn.unhide()
    level_3_btn.unhide()
    level_4_btn.unhide()
    level_5_btn.unhide()
    level_6_btn.unhide()
    level_7_btn.unhide()
    level_8_btn.unhide()
    level_9_btn.unhide()
    random_6x6_btn.unhide()
    random_7x7_btn.unhide()
    random_8x8_btn.unhide()
    start_btn.hide()
    tutorial_btn.hide()
    exit_btn.hide()
    window.set_background_color((200, 200, 0))

start_btn = window.Button(font=smallfont, text="start game", position=(width/2-150, height/3+20), size=(200, 40))
start_btn.connect(page_2)

tutorial_btn = window.Button(font=smallfont, text="tutorial", position=(width/2-150, height/3+70), size=(200, 40))
tutorial_btn.connect(start_game, args=(0, 0))

exit_btn = window.Button(font=smallfont, text="quit", position=(width/2-150, height/3+120), size=(200, 40))
exit_btn.connect(pygame.quit)

window.set_background_color((210, 200, 200))

img_title = pygame.image.load('data/img/menu/gameTitle2.png')
window.show_image(img_title, (width/2-200, height/3-70))

img_player = pygame.image.load('data/img/menu/PlayerThreeRight.png')
img_player = pygame.transform.scale(img_player, (140, 140))
window.show_image(img_player, (400, 500))

# #menu images 
# img_title=pygame.image.load('data/img/menu/gameTitle2.png')
# img_player=pygame.image.load('data/img/menu/PlayerThreeRight.png')
# img_player = pygame.transform.scale(img_player, (140, 140))
# img_explosion=pygame.image.load('data/img/menu/Explosion2.png')
# img_explosion = pygame.transform.scale(img_explosion, (320, 320))
# img_treasure=pygame.image.load('data/img/menu/Treasure2.png')
# img_treasure = pygame.transform.scale(img_treasure, (160, 160))
# img_spike=pygame.image.load('data/img/spike/spike_2.png')
# img_spike = pygame.transform.scale(img_spike, (100, 100))
# # where BTNs and texts at
# x_title = width/2-200
# x_start_btn = width/2-150
# x_quit_btn = width/2-150
# x_back_2_menu = width/2-150
# x_tut_btn = width/2-150

# x_random_level_6x6=width/2-350
# x_random_level_7x7=width/2-350
# x_random_level_8x8=width/2-350
# #level select
# x_level_1_btn=width/2-350
# x_level_2_btn=width/2-350
# x_level_3_btn=width/2-350
# x_level_4_btn=width/2-150
# x_level_5_btn=width/2-150
# x_level_6_btn=width/2-150
# x_level_7_btn=width/2+50
# x_level_8_btn=width/2+50
# x_level_9_btn=width/2+50


# y_title = height/3-70
# y_start_btn = height/3+20
# y_tut_btn = height/3+70
# y_quit_btn = height/3+120
# y_back_2_menu = height/3+320

# y_random_level_6x6=height/3+170
# y_random_level_7x7=height/3+220
# y_random_level_8x8=height/3+270
# #level select
# y_level_1_btn=height/3+20
# y_level_2_btn=height/3+70
# y_level_3_btn=height/3+120
# y_level_4_btn=height/3+20
# y_level_5_btn=height/3+70
# y_level_6_btn=height/3+120
# y_level_7_btn=height/3+20
# y_level_8_btn=height/3+70
# y_level_9_btn=height/3+120

# width_start_btn = 200
# width_quit_btn = 140
# width_back_2_menu = 250
# width_tut_btn = 180
# width_title = 400
# width_random_level_6x6=600
# width_random_level_7x7=600
# width_random_level_8x8=600

# #level select
# width_level_1_btn=200
# width_level_2_btn=200
# width_level_3_btn=200
# width_level_4_btn=200
# width_level_5_btn=200
# width_level_6_btn=200
# width_level_7_btn=200
# width_level_8_btn=200
# width_level_9_btn=200

# height_start_btn = 40
# height_quit_btn = 40
# height_back_2_menu = 40
# height_tut_btn = 40
# height_title = 40

# height_random_level_6x6 = 40
# height_random_level_7x7 = 40
# height_random_level_8x8 = 40
# #level-select
# height_level_1_btn=40
# height_level_2_btn=40
# height_level_3_btn=40
# height_level_4_btn=40
# height_level_5_btn=40
# height_level_6_btn=40
# height_level_7_btn=40
# height_level_8_btn=40
# height_level_9_btn=40

# # game settings
# level_selected = 3

# game_mask = False



# def mainLoop(clear_event:bool):
#     #flags for menu
    
#     tutorial_level=0
#     first_quit_pressed=False
#     back_2_menu=False
#     start_tutorial_pressed=False
#     first_start_game_pressed = False
#     start_game=False
#     random_level_size=5
#     if clear_event:pygame.event.clear() 
#     #page 1
#     while True:
#         breakflag = False
#         #sleep(0.032)
#         sleep(0.1)
#         for ev in pygame.event.get():

#             if ev.type == pygame.QUIT:
#                 return "game_quit"
#                 first_quit_pressed=True
#             # checks if a mouse is clicked
#             if ev.type == pygame.MOUSEBUTTONDOWN:

#                 # if the mouse is clicked on the
#                 # button the game is terminated
#                 if x_quit_btn <= mouse[0] <= x_quit_btn + width_quit_btn and y_quit_btn <= mouse[1] <= y_quit_btn+height_quit_btn:
#                     pygame.quit()
#                     first_quit_pressed=True
#                     breakflag = True
#                     return "first_quit"
#                     break
#                 elif x_start_btn <= mouse[0] <= x_start_btn+width_start_btn and y_start_btn <= mouse[1] <= y_start_btn+height_start_btn:
#                     first_start_game_pressed=True
#                     breakflag = True
#                     break
#                 elif x_tut_btn <= mouse[0] <= x_tut_btn+width_tut_btn and y_tut_btn <= mouse[1] <= y_tut_btn+height_tut_btn:
#                     start_tutorial_pressed=True
                    
#                     breakflag = True
#                     break
                
#         if breakflag == True:
#             break

#         # fills the screen with a color
#         screen.fill((210, 200,    200))

#         # stores the (x,y) coordinates into
#         # the variable as a tuple
#         mouse = pygame.mouse.get_pos()

#         # if mouse is hovered on a button it
#         # changes to lighter shade
#         # otherwise its a dark color
#         pygame.draw.rect(screen, color_dark, [
#                             x_start_btn, y_start_btn, width_start_btn, height_start_btn])
#         pygame.draw.rect(screen, color_dark, [
#                             x_tut_btn, y_tut_btn, width_tut_btn, height_tut_btn])
#         pygame.draw.rect(screen, color_dark, [
#                             x_quit_btn, y_quit_btn, width_quit_btn, height_quit_btn])
#         # start btn
#         if x_start_btn <= mouse[0] <= x_start_btn+width_start_btn and y_start_btn <= mouse[1] <= y_start_btn+height_start_btn:
#             pygame.draw.rect(screen, color_light, [
#                             x_start_btn, y_start_btn, width_start_btn, height_start_btn])
#         # tut_btn
#         elif x_tut_btn <= mouse[0] <= x_tut_btn+width_tut_btn and y_tut_btn <= mouse[1] <= y_tut_btn+height_tut_btn:
#             pygame.draw.rect(screen, color_light, [
#                             x_tut_btn, y_tut_btn, width_tut_btn, height_tut_btn])
#         # quit_btn
#         elif x_quit_btn <= mouse[0] <= x_quit_btn+width_quit_btn and y_quit_btn <= mouse[1] <= y_quit_btn+height_quit_btn:
#             pygame.draw.rect(screen, color_light, [
#                             x_quit_btn, y_quit_btn, width_quit_btn, height_quit_btn])
    
        
        
            
                        
#             # draw title
#             #pygame.draw.rect(screen, color_dark, [
#                     #      x_title, y_title, width_title, height_title])
#         # superimposing the text onto our button
    
#         screen.blit(text_quit, (x_quit_btn+50, y_quit_btn))
#         screen.blit(text_start, (x_start_btn+50, y_start_btn))
#         screen.blit(text_help, (x_tut_btn+50, y_tut_btn))
#         #draw images on screen
#         screen.blit(img_title, (x_title-450, y_title-80))
#         screen.blit(img_player, (x_title+260, y_title+300))
#         screen.blit(img_explosion, (x_title-200, y_title+300))
#         screen.blit(img_treasure, (x_title+400, y_title+300))
#         #screen.blit(img_spike, (x_title+100, y_title+250))
#         # updates the frames of the game
#         pygame.display.update()



#     #level select menu
#         #pygame.quit()
#     if start_tutorial_pressed:
#         game = Game(level=tutorial_level, random_level_size=random_level_size,debug=False)
#         return game.run_game()
#         game=null
#         return "tutorial"
#         #pygame.quit()
#     #else continue towards level select
        

#     ###############################################################################################
#     #page 2
#     while True:
#         #sleep(0.016)
#         sleep(0.1)
#         if(first_quit_pressed or start_tutorial_pressed):
#             break
#         breakflag = False
#         for ev in pygame.event.get():

#             if ev.type == pygame.QUIT:
#                 pygame.quit()

#             # checks if a mouse is clicked
#             if ev.type == pygame.MOUSEBUTTONDOWN:

#                 # if the mouse is clicked on the
#                 # button the game is terminated
#                 if x_back_2_menu <= mouse[0] <= x_back_2_menu + width_back_2_menu and y_back_2_menu <= mouse[1] <= y_back_2_menu+height_back_2_menu:
#                     #pygame.quit()
#                     back_2_menu=True
#                     breakflag = True
#                     break
#                 elif x_level_1_btn <= mouse[0] <= x_level_1_btn+ width_level_1_btn and y_level_1_btn <= mouse[1] <= y_level_1_btn+height_level_1_btn:
#                     start_game=True
#                     level_selected=1
#                     breakflag = True
#                     break
#                 elif x_level_2_btn <= mouse[0] <= x_level_2_btn+ width_level_2_btn and y_level_2_btn <= mouse[1] <= y_level_2_btn+height_level_2_btn:
#                     start_game=True
#                     level_selected=2
#                     breakflag = True
#                     break
#                 elif x_level_3_btn <= mouse[0] <= x_level_3_btn+ width_level_3_btn and y_level_3_btn <= mouse[1] <= y_level_3_btn+height_level_3_btn:
#                     start_game=True
#                     level_selected=3
#                     breakflag = True
#                     break
#                 elif x_level_4_btn <= mouse[0] <= x_level_4_btn+ width_level_4_btn and y_level_4_btn <= mouse[1] <= y_level_4_btn+height_level_4_btn:
#                     start_game=True
#                     level_selected=4
#                     breakflag = True
#                     break
#                 elif x_level_5_btn <= mouse[0] <= x_level_5_btn+ width_level_5_btn and y_level_5_btn <= mouse[1] <= y_level_5_btn+height_level_5_btn:
#                     start_game=True
#                     level_selected=5
#                     breakflag = True
#                     break
#                 elif x_level_6_btn <= mouse[0] <= x_level_6_btn+ width_level_6_btn and y_level_6_btn <= mouse[1] <= y_level_6_btn+height_level_6_btn:
#                     start_game=True
#                     level_selected=6
#                     breakflag = True
#                     break
#                 elif x_level_7_btn <= mouse[0] <= x_level_7_btn+ width_level_7_btn and y_level_7_btn <= mouse[1] <= y_level_7_btn+height_level_7_btn:
#                     start_game=True
#                     level_selected=7
#                     breakflag = True
#                     break
#                 elif x_level_8_btn <= mouse[0] <= x_level_8_btn+ width_level_8_btn and y_level_8_btn <= mouse[1] <= y_level_8_btn+height_level_8_btn:
#                     start_game=True
#                     level_selected=8
#                     breakflag = True
#                     break
#                 elif x_level_9_btn <= mouse[0] <= x_level_9_btn+ width_level_9_btn and y_level_9_btn <= mouse[1] <= y_level_9_btn+height_level_9_btn:
#                     start_game=True
#                     level_selected=9
#                     breakflag = True
#                     break
#                 elif x_random_level_6x6 <= mouse[0] <= x_random_level_6x6+width_random_level_6x6 and y_random_level_6x6 <= mouse[1] <= y_random_level_6x6+height_random_level_6x6:
#                     start_game=True
#                     level_selected=1000
#                     random_level_size=6
#                     breakflag = True
#                     break
#                 elif x_random_level_7x7 <= mouse[0] <= x_random_level_7x7+width_random_level_7x7 and y_random_level_7x7 <= mouse[1] <= y_random_level_7x7+height_random_level_7x7:
#                     start_game=True
#                     level_selected=1000
#                     random_level_size=7
#                     breakflag = True
#                     break
#                 elif x_random_level_8x8 <= mouse[0] <= x_random_level_8x8+width_random_level_8x8 and y_random_level_8x8 <= mouse[1] <= y_random_level_8x8+height_random_level_8x8:
#                     start_game=True
#                     level_selected=1000
#                     random_level_size=8
#                     breakflag = True
#                     break
            
#         if breakflag == True:
#             break

#         # fills the screen with a color
#         screen.fill((200, 200,    0))

#         # stores the (x,y) coordinates into
#         # the variable as a tuple
#         mouse = pygame.mouse.get_pos()

#         # if mouse is hovered on a button it
#         # changes to lighter shade
#         #otherwise the color is dark
#         pygame.draw.rect(screen, color_dark, [
#                             x_level_1_btn, y_level_1_btn, width_level_1_btn, height_level_1_btn])
#         pygame.draw.rect(screen, color_dark, [
#                             x_level_2_btn, y_level_2_btn, width_level_2_btn, height_level_2_btn])
#         pygame.draw.rect(screen, color_dark, [
#                             x_level_3_btn, y_level_3_btn, width_level_3_btn, height_level_3_btn])
#         pygame.draw.rect(screen, color_dark, [
#                             x_level_4_btn, y_level_4_btn, width_level_4_btn, height_level_4_btn])
#         pygame.draw.rect(screen, color_dark, [
#                             x_level_5_btn, y_level_5_btn, width_level_5_btn, height_level_5_btn])
#         pygame.draw.rect(screen, color_dark, [
#                             x_level_6_btn, y_level_6_btn, width_level_6_btn, height_level_6_btn])
#         pygame.draw.rect(screen, color_dark, [
#                             x_level_7_btn, y_level_7_btn, width_level_7_btn, height_level_7_btn])
#         pygame.draw.rect(screen, color_dark, [
#                             x_level_8_btn, y_level_8_btn, width_level_8_btn, height_level_8_btn])
#         pygame.draw.rect(screen, color_dark, [
#                             x_level_9_btn, y_level_9_btn, width_level_9_btn, height_level_9_btn])                 
#         pygame.draw.rect(screen, color_dark, [
#                             x_back_2_menu, y_back_2_menu, width_back_2_menu, height_back_2_menu])
#         pygame.draw.rect(screen, color_dark, [
#                             x_random_level_6x6, y_random_level_6x6, width_random_level_6x6, height_random_level_6x6])
#         pygame.draw.rect(screen, color_dark, [
#                         x_random_level_7x7, y_random_level_7x7, width_random_level_7x7, height_random_level_7x7])
#         pygame.draw.rect(screen, color_dark, [
#                             x_random_level_8x8, y_random_level_8x8, width_random_level_8x8, height_random_level_8x8])
#         # levels
#         if x_level_1_btn <= mouse[0] <= x_level_1_btn+width_level_1_btn and y_level_1_btn <= mouse[1] <= y_level_1_btn+height_level_1_btn:
#             pygame.draw.rect(screen, color_light, [
#                             x_level_1_btn, y_level_1_btn, width_level_1_btn, height_level_1_btn])
#         elif x_level_2_btn <= mouse[0] <= x_level_2_btn+width_level_2_btn and y_level_2_btn <= mouse[1] <= y_level_2_btn+height_level_2_btn:
#             pygame.draw.rect(screen, color_light, [
#                             x_level_2_btn, y_level_2_btn, width_level_2_btn, height_level_2_btn])
        
#         elif x_level_3_btn <= mouse[0] <= x_level_3_btn+width_level_3_btn and y_level_3_btn <= mouse[1] <= y_level_3_btn+height_level_3_btn:
#             pygame.draw.rect(screen, color_light, [
#                             x_level_3_btn, y_level_3_btn, width_level_3_btn, height_level_3_btn])
#         elif x_level_4_btn <= mouse[0] <= x_level_4_btn+width_level_4_btn and y_level_4_btn <= mouse[1] <= y_level_4_btn+height_level_4_btn:
#             pygame.draw.rect(screen, color_light, [
#                             x_level_4_btn, y_level_4_btn, width_level_4_btn, height_level_4_btn])
#         elif x_level_5_btn <= mouse[0] <= x_level_5_btn+width_level_5_btn and y_level_5_btn <= mouse[1] <= y_level_5_btn+height_level_5_btn:
#             pygame.draw.rect(screen, color_light, [
#                             x_level_5_btn, y_level_5_btn, width_level_5_btn, height_level_5_btn])
#         elif x_level_6_btn <= mouse[0] <= x_level_6_btn+width_level_6_btn and y_level_6_btn <= mouse[1] <= y_level_6_btn+height_level_6_btn:
#             pygame.draw.rect(screen, color_light, [
#                             x_level_6_btn, y_level_6_btn, width_level_6_btn, height_level_6_btn])
#         elif x_level_7_btn <= mouse[0] <= x_level_7_btn+width_level_7_btn and y_level_7_btn <= mouse[1] <= y_level_7_btn+height_level_7_btn:
#             pygame.draw.rect(screen, color_light, [
#                             x_level_7_btn, y_level_7_btn, width_level_7_btn, height_level_7_btn])
#         elif x_level_8_btn <= mouse[0] <= x_level_8_btn+width_level_8_btn and y_level_8_btn <= mouse[1] <= y_level_8_btn+height_level_8_btn:
#             pygame.draw.rect(screen, color_light, [
#                             x_level_8_btn, y_level_8_btn, width_level_8_btn, height_level_8_btn])
#         elif x_level_9_btn <= mouse[0] <= x_level_9_btn+width_level_9_btn and y_level_9_btn <= mouse[1] <= y_level_9_btn+height_level_9_btn:
#             pygame.draw.rect(screen, color_light, [
#                             x_level_9_btn, y_level_9_btn, width_level_9_btn, height_level_9_btn])   
        
#         #random level
#         elif x_random_level_6x6 <= mouse[0] <= x_random_level_6x6+width_random_level_6x6 and y_random_level_6x6 <= mouse[1] <= y_random_level_6x6+height_random_level_6x6:
#             pygame.draw.rect(screen, color_light, [
#                             x_random_level_6x6, y_random_level_6x6, width_random_level_6x6, height_random_level_6x6])    
#         elif x_random_level_7x7 <= mouse[0] <= x_random_level_7x7+width_random_level_7x7 and y_random_level_7x7 <= mouse[1] <= y_random_level_7x7+height_random_level_7x7:
#             pygame.draw.rect(screen, color_light, [
#                             x_random_level_7x7, y_random_level_7x7, width_random_level_7x7, height_random_level_7x7])    
#         elif x_random_level_8x8 <= mouse[0] <= x_random_level_8x8+width_random_level_8x8 and y_random_level_8x8 <= mouse[1] <= y_random_level_8x8+height_random_level_8x8:
#             pygame.draw.rect(screen, color_light, [
#                             x_random_level_8x8, y_random_level_8x8, width_random_level_8x8, height_random_level_8x8])                  
#         # back 2 menu
#         elif x_back_2_menu <= mouse[0] <= x_back_2_menu+width_back_2_menu and y_back_2_menu <= mouse[1] <= y_back_2_menu+height_back_2_menu:
#             pygame.draw.rect(screen, color_light, [
#                             x_back_2_menu, y_back_2_menu, width_back_2_menu, height_back_2_menu])
       
       
               
           
#         # superimposing the text onto our button
#         screen.blit(text_back_2_menu, (x_back_2_menu+50, y_back_2_menu))
        
#         #levels
#         screen.blit(text_level_1, (x_level_1_btn+50, y_level_1_btn))
#         screen.blit(text_level_2, (x_level_2_btn+50, y_level_2_btn))
#         screen.blit(text_level_3, (x_level_3_btn+50, y_level_3_btn))
#         screen.blit(text_level_4, (x_level_4_btn+50, y_level_4_btn))
#         screen.blit(text_level_5, (x_level_5_btn+50, y_level_5_btn))
#         screen.blit(text_level_6, (x_level_6_btn+50, y_level_6_btn))
#         screen.blit(text_level_7, (x_level_7_btn+50, y_level_7_btn))
#         screen.blit(text_level_8, (x_level_8_btn+50, y_level_8_btn))
#         screen.blit(text_level_9, (x_level_9_btn+50, y_level_9_btn))
        
#         screen.blit(text_random_level_6x6, (x_random_level_6x6+50, y_random_level_6x6))
#         screen.blit(text_random_level_7x7, (x_random_level_7x7+50, y_random_level_7x7))
#         screen.blit(text_random_level_8x8, (x_random_level_8x8+50, y_random_level_8x8))
#         #draw images on screen
#         screen.blit(img_title, (x_title-450, y_title-80))
#         screen.blit(img_spike, (x_title-300, y_title+300))
#         #screen.blit(img_explosion, (x_title-200, y_title+300))
#         #screen.blit(img_treasure, (x_title+400, y_title+300))

#         # updates the frames of the game
#         pygame.display.update()

#     if(back_2_menu):
#         #pygame.quit()
#         return 'back'
#     elif(start_game):
#         if(level_selected>999):
#             screen.fill((200, 200,    0))
#             screen.blit(text_random_level_in_progress, (x_level_1_btn-150, y_level_1_btn))
#             pygame.display.update()
#             game = Game(level=level_selected, random_level_size=random_level_size,debug=False)
#             return game.run_game()
#         else:#normal level 1 to 9
#             game = Game(level=level_selected, random_level_size=random_level_size,debug=False)
#             result=game.run_game()
           
#             return result
            
        
# # mainLoop
# if __name__ == '__main__':
#     pygame.init()
#     clear_event=False
#     while True:
#         exit_code=mainLoop(clear_event)
#         if exit_code=='first_quit':break
#         elif exit_code=='second_quit':break
#         elif exit_code=='game_quit':break
#         elif exit_code=='game_to_menu':
#             pygame.init()
#             clear_event=True
#     pygame.quit()