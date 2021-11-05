import logging
import pygame
from pygame import image
logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)

pygame.init()
pygame.font.init()

from game import Game
from pygame import mouse
from time import sleep
from sokoban_solver import generate

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
text_random_level=smallfont.render('Generate a random level and Play!', True, color)
#text_title = bigfont.render('Sokoban Stealer', True, color)

#menu images 
img_title=pygame.image.load('data/img/menu/gameTitle2.png')
img_player=pygame.image.load('data/img/menu/PlayerThreeRight.png')
img_player = pygame.transform.scale(img_player, (140, 140))
img_explosion=pygame.image.load('data/img/menu/Explosion2.png')
img_explosion = pygame.transform.scale(img_explosion, (320, 320))
img_treasure=pygame.image.load('data/img/menu/Treasure2.png')
img_treasure = pygame.transform.scale(img_treasure, (160, 160))
# where BTNs and texts at
x_title = width/2-200
x_start_btn = width/2-150
x_quit_btn = width/2-150
x_quit_btn_2 = width/2-150
x_tut_btn = width/2-150

x_random_level=width/2-350
#level select
x_level_1_btn=width/2-350
x_level_2_btn=width/2-350
x_level_3_btn=width/2-350
x_level_4_btn=width/2-150
x_level_5_btn=width/2-150
x_level_6_btn=width/2-150
x_level_7_btn=width/2+50
x_level_8_btn=width/2+50
x_level_9_btn=width/2+50


y_title = height/3-70
y_start_btn = height/3+20
y_tut_btn = height/3+70
y_quit_btn = height/3+120
y_quit_btn_2 = height/3+220

y_random_level=height/3+170
#level select
y_level_1_btn=height/3+20
y_level_2_btn=height/3+70
y_level_3_btn=height/3+120
y_level_4_btn=height/3+20
y_level_5_btn=height/3+70
y_level_6_btn=height/3+120
y_level_7_btn=height/3+20
y_level_8_btn=height/3+70
y_level_9_btn=height/3+120

width_start_btn = 200
width_quit_btn = 140
width_quit_btn_2 = 140
width_tut_btn = 180
width_title = 400
width_random_level=600

#level select
width_level_1_btn=200
width_level_2_btn=200
width_level_3_btn=200
width_level_4_btn=200
width_level_5_btn=200
width_level_6_btn=200
width_level_7_btn=200
width_level_8_btn=200
width_level_9_btn=200

height_start_btn = 40
height_quit_btn = 40
height_quit_btn_2 = 40
height_tut_btn = 40
height_title = 40

height_random_level = 40
#level-select
height_level_1_btn=40
height_level_2_btn=40
height_level_3_btn=40
height_level_4_btn=40
height_level_5_btn=40
height_level_6_btn=40
height_level_7_btn=40
height_level_8_btn=40
height_level_9_btn=40

# game settings
level_selected = 3

game_mask = False

#flags for menu
tutorial_level=1
first_quit_pressed=False
second_quit_pressed=False
start_tutorial_pressed=False
first_start_game_pressed = False
start_game=False
while True:
    breakflag = False
    #sleep(0.032)
    sleep(0.1)
    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()
            first_quit_pressed=True
        # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:

            # if the mouse is clicked on the
            # button the game is terminated
            if x_quit_btn <= mouse[0] <= x_quit_btn + width_quit_btn and y_quit_btn <= mouse[1] <= y_quit_btn+height_quit_btn:
                pygame.quit()
                first_quit_pressed=True
                breakflag = True
                break
            elif x_start_btn <= mouse[0] <= x_start_btn+width_start_btn and y_start_btn <= mouse[1] <= y_start_btn+height_start_btn:
                first_start_game_pressed=True
                breakflag = True
                break
            elif x_tut_btn <= mouse[0] <= x_tut_btn+width_tut_btn and y_tut_btn <= mouse[1] <= y_tut_btn+height_tut_btn:
                start_tutorial_pressed=True
                
                breakflag = True
                break
            
    if breakflag == True:
        break

    # fills the screen with a color
    screen.fill((210, 200,    200))

    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()

    # if mouse is hovered on a button it
    # changes to lighter shade
    # start btn
    if x_start_btn <= mouse[0] <= x_start_btn+width_start_btn and y_start_btn <= mouse[1] <= y_start_btn+height_start_btn:
        pygame.draw.rect(screen, color_light, [
                         x_start_btn, y_start_btn, width_start_btn, height_start_btn])
    # tut_btn
    elif x_tut_btn <= mouse[0] <= x_tut_btn+width_tut_btn and y_tut_btn <= mouse[1] <= y_tut_btn+height_tut_btn:
        pygame.draw.rect(screen, color_light, [
                         x_tut_btn, y_tut_btn, width_tut_btn, height_tut_btn])
    # quit_btn
    elif x_quit_btn <= mouse[0] <= x_quit_btn+width_quit_btn and y_quit_btn <= mouse[1] <= y_quit_btn+height_quit_btn:
        pygame.draw.rect(screen, color_light, [
                         x_quit_btn, y_quit_btn, width_quit_btn, height_quit_btn])
   
    # not hovered above
    else:
        pygame.draw.rect(screen, color_dark, [
                         x_start_btn, y_start_btn, width_start_btn, height_start_btn])
        pygame.draw.rect(screen, color_dark, [
                         x_tut_btn, y_tut_btn, width_tut_btn, height_tut_btn])
        pygame.draw.rect(screen, color_dark, [
                         x_quit_btn, y_quit_btn, width_quit_btn, height_quit_btn])
                      
        # draw title
        #pygame.draw.rect(screen, color_dark, [
                   #      x_title, y_title, width_title, height_title])
    # superimposing the text onto our button
 
    screen.blit(text_quit, (x_quit_btn+50, y_quit_btn))
    screen.blit(text_start, (x_start_btn+50, y_start_btn))
    screen.blit(text_help, (x_tut_btn+50, y_tut_btn))
    #draw images on screen
    screen.blit(img_title, (x_title-450, y_title-80))
    screen.blit(img_player, (x_title+260, y_title+300))
    screen.blit(img_explosion, (x_title-200, y_title+300))
    screen.blit(img_treasure, (x_title+400, y_title+300))

    # updates the frames of the game
    pygame.display.update()



#level select menu
if(first_quit_pressed):
    pygame.quit()
elif start_tutorial_pressed:
    game = Game(level=tutorial_level, debug=False)
    game.run_game()
    pygame.quit()
#else continue towards level select
    

while True:
    #sleep(0.016)
    sleep(0.1)
    if(first_quit_pressed or start_tutorial_pressed):
        break
    breakflag = False
    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

        # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:

            # if the mouse is clicked on the
            # button the game is terminated
            if x_quit_btn_2 <= mouse[0] <= x_quit_btn_2 + width_quit_btn_2 and y_quit_btn_2 <= mouse[1] <= y_quit_btn_2+height_quit_btn_2:
                pygame.quit()
                second_quit_pressed=True
                breakflag = True
                break
            elif x_level_1_btn <= mouse[0] <= x_level_1_btn+ width_level_1_btn and y_level_1_btn <= mouse[1] <= y_level_1_btn+height_level_1_btn:
                start_game=True
                level_selected=1
                breakflag = True
                break
            elif x_level_2_btn <= mouse[0] <= x_level_2_btn+ width_level_2_btn and y_level_2_btn <= mouse[1] <= y_level_2_btn+height_level_2_btn:
                start_game=True
                level_selected=2
                breakflag = True
                break
            elif x_level_3_btn <= mouse[0] <= x_level_3_btn+ width_level_3_btn and y_level_3_btn <= mouse[1] <= y_level_3_btn+height_level_3_btn:
                start_game=True
                level_selected=3
                breakflag = True
                break
            elif x_level_4_btn <= mouse[0] <= x_level_4_btn+ width_level_4_btn and y_level_4_btn <= mouse[1] <= y_level_4_btn+height_level_4_btn:
                start_game=True
                level_selected=4
                breakflag = True
                break
            elif x_level_5_btn <= mouse[0] <= x_level_5_btn+ width_level_5_btn and y_level_5_btn <= mouse[1] <= y_level_5_btn+height_level_5_btn:
                start_game=True
                level_selected=5
                breakflag = True
                break
            elif x_level_6_btn <= mouse[0] <= x_level_6_btn+ width_level_6_btn and y_level_6_btn <= mouse[1] <= y_level_6_btn+height_level_6_btn:
                start_game=True
                level_selected=6
                breakflag = True
                break
            elif x_level_7_btn <= mouse[0] <= x_level_7_btn+ width_level_7_btn and y_level_7_btn <= mouse[1] <= y_level_7_btn+height_level_7_btn:
                start_game=True
                level_selected=7
                breakflag = True
                break
            elif x_level_8_btn <= mouse[0] <= x_level_8_btn+ width_level_8_btn and y_level_8_btn <= mouse[1] <= y_level_8_btn+height_level_8_btn:
                start_game=True
                level_selected=8
                breakflag = True
                break
            elif x_level_9_btn <= mouse[0] <= x_level_9_btn+ width_level_9_btn and y_level_9_btn <= mouse[1] <= y_level_9_btn+height_level_9_btn:
                start_game=True
                level_selected=9
                breakflag = True
                break
            elif x_random_level <= mouse[0] <= x_random_level+width_random_level and y_random_level <= mouse[1] <= y_random_level+height_random_level:
                start_game=True
                level_selected=8
                breakflag = True
                break
           
    if breakflag == True:
        break

    # fills the screen with a color
    screen.fill((200, 200,    0))

    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()

    # if mouse is hovered on a button it
    # changes to lighter shade
    # levels
    if x_level_1_btn <= mouse[0] <= x_level_1_btn+width_level_1_btn and y_level_1_btn <= mouse[1] <= y_level_1_btn+height_level_1_btn:
        pygame.draw.rect(screen, color_light, [
                         x_level_1_btn, y_level_1_btn, width_level_1_btn, height_level_1_btn])
    elif x_level_2_btn <= mouse[0] <= x_level_2_btn+width_level_2_btn and y_level_2_btn <= mouse[1] <= y_level_2_btn+height_level_2_btn:
        pygame.draw.rect(screen, color_light, [
                         x_level_2_btn, y_level_2_btn, width_level_2_btn, height_level_2_btn])
    
    elif x_level_3_btn <= mouse[0] <= x_level_3_btn+width_level_3_btn and y_level_3_btn <= mouse[1] <= y_level_3_btn+height_level_3_btn:
        pygame.draw.rect(screen, color_light, [
                         x_level_3_btn, y_level_3_btn, width_level_3_btn, height_level_3_btn])
    elif x_level_4_btn <= mouse[0] <= x_level_4_btn+width_level_4_btn and y_level_4_btn <= mouse[1] <= y_level_4_btn+height_level_4_btn:
        pygame.draw.rect(screen, color_light, [
                         x_level_4_btn, y_level_4_btn, width_level_4_btn, height_level_4_btn])
    elif x_level_5_btn <= mouse[0] <= x_level_5_btn+width_level_5_btn and y_level_5_btn <= mouse[1] <= y_level_5_btn+height_level_5_btn:
        pygame.draw.rect(screen, color_light, [
                         x_level_5_btn, y_level_5_btn, width_level_5_btn, height_level_5_btn])
    elif x_level_6_btn <= mouse[0] <= x_level_6_btn+width_level_6_btn and y_level_6_btn <= mouse[1] <= y_level_6_btn+height_level_6_btn:
        pygame.draw.rect(screen, color_light, [
                         x_level_6_btn, y_level_6_btn, width_level_6_btn, height_level_6_btn])
    elif x_level_7_btn <= mouse[0] <= x_level_7_btn+width_level_7_btn and y_level_7_btn <= mouse[1] <= y_level_7_btn+height_level_7_btn:
        pygame.draw.rect(screen, color_light, [
                         x_level_7_btn, y_level_7_btn, width_level_7_btn, height_level_7_btn])
    elif x_level_8_btn <= mouse[0] <= x_level_8_btn+width_level_8_btn and y_level_8_btn <= mouse[1] <= y_level_8_btn+height_level_8_btn:
        pygame.draw.rect(screen, color_light, [
                         x_level_8_btn, y_level_8_btn, width_level_8_btn, height_level_8_btn])
    elif x_level_9_btn <= mouse[0] <= x_level_9_btn+width_level_9_btn and y_level_9_btn <= mouse[1] <= y_level_9_btn+height_level_9_btn:
        pygame.draw.rect(screen, color_light, [
                         x_level_9_btn, y_level_9_btn, width_level_9_btn, height_level_9_btn])   
     #random level
    elif x_random_level <= mouse[0] <= x_random_level+width_random_level and y_random_level <= mouse[1] <= y_random_level+height_random_level:
        pygame.draw.rect(screen, color_light, [
                         x_random_level, y_random_level, width_random_level, height_random_level])                  
    # quit_btn
    elif x_quit_btn_2 <= mouse[0] <= x_quit_btn_2+width_quit_btn_2 and y_quit_btn_2 <= mouse[1] <= y_quit_btn_2+height_quit_btn_2:
        pygame.draw.rect(screen, color_light, [
                         x_quit_btn_2, y_quit_btn_2, width_quit_btn_2, height_quit_btn_2])
    # not hovered above
    else:
        pygame.draw.rect(screen, color_dark, [
                         x_level_1_btn, y_level_1_btn, width_level_1_btn, height_level_1_btn])
        pygame.draw.rect(screen, color_dark, [
                         x_level_2_btn, y_level_2_btn, width_level_2_btn, height_level_2_btn])
        pygame.draw.rect(screen, color_dark, [
                         x_level_3_btn, y_level_3_btn, width_level_3_btn, height_level_3_btn])
        pygame.draw.rect(screen, color_dark, [
                         x_level_4_btn, y_level_4_btn, width_level_4_btn, height_level_4_btn])
        pygame.draw.rect(screen, color_dark, [
                         x_level_5_btn, y_level_5_btn, width_level_5_btn, height_level_5_btn])
        pygame.draw.rect(screen, color_dark, [
                         x_level_6_btn, y_level_6_btn, width_level_6_btn, height_level_6_btn])
        pygame.draw.rect(screen, color_dark, [
                         x_level_7_btn, y_level_7_btn, width_level_7_btn, height_level_7_btn])
        pygame.draw.rect(screen, color_dark, [
                         x_level_8_btn, y_level_8_btn, width_level_8_btn, height_level_8_btn])
        pygame.draw.rect(screen, color_dark, [
                         x_level_9_btn, y_level_9_btn, width_level_9_btn, height_level_9_btn])                 
        pygame.draw.rect(screen, color_dark, [
                         x_quit_btn_2, y_quit_btn_2, width_quit_btn_2, height_quit_btn_2])
        pygame.draw.rect(screen, color_dark, [
                         x_random_level, y_random_level, width_random_level, height_random_level])   
        # draw title
        #pygame.draw.rect(screen, color_dark, [
                   #      x_title, y_title, width_title, height_title])
    # superimposing the text onto our button
    screen.blit(text_quit, (x_quit_btn_2+50, y_quit_btn_2))
    
    #levels
    screen.blit(text_level_1, (x_level_1_btn+50, y_level_1_btn))
    screen.blit(text_level_2, (x_level_2_btn+50, y_level_2_btn))
    screen.blit(text_level_3, (x_level_3_btn+50, y_level_3_btn))
    screen.blit(text_level_4, (x_level_4_btn+50, y_level_4_btn))
    screen.blit(text_level_5, (x_level_5_btn+50, y_level_5_btn))
    screen.blit(text_level_6, (x_level_6_btn+50, y_level_6_btn))
    screen.blit(text_level_7, (x_level_7_btn+50, y_level_7_btn))
    screen.blit(text_level_8, (x_level_8_btn+50, y_level_8_btn))
    screen.blit(text_level_9, (x_level_9_btn+50, y_level_9_btn))
    
    screen.blit(text_random_level, (x_random_level+50, y_random_level))
    #draw images on screen
    screen.blit(img_title, (x_title-450, y_title-80))
    screen.blit(img_player, (x_title+260, y_title+300))
    screen.blit(img_explosion, (x_title-200, y_title+300))
    screen.blit(img_treasure, (x_title+400, y_title+300))

    # updates the frames of the game
    pygame.display.update()

if(second_quit_pressed):
    pygame.quit()
elif(start_game):

    game = Game(level=level_selected, debug=False)
    game.run_game()
    pygame.quit()
pygame.quit()
