import pygame 
import sys

pygame.init() 
pygame.font.init()

from game import Game
import parameter
# initializing the constructor 

  
# screen resolution 
#res = (720,720) 
  
# opens up a window 
screen = pygame.display.set_mode((parameter.WIN_WIDTH, parameter.WIN_HEIGHT))
  
# white color 
color = (255,255,255) 
  
# light shade of the button 
color_light = (170,170,170) 
  
# dark shade of the button 
color_dark = (100,100,100) 
  
# stores the width of the 
# screen into a variable 
width = screen.get_width() 
  
# stores the height of the 
# screen into a variable 
height = screen.get_height() 
  
# defining a font 
smallfont = pygame.font.SysFont('Corbel',35) 
  
# rendering a text written in 
# this font 
text_quit = smallfont.render('quit' , True , color) 
text_start=smallfont.render('start game' , True , color) 
text_help=smallfont.render('tutorial' , True , color) 

#where btns at
x_start_btn=  width/2-80
x_quit_btn=  width/2-80
x_tut_btn=  width/2-80
y_start_btn=height/3
y_tut_btn=  height/3+50
y_quit_btn= height/3+100


width_start_btn=200
width_quit_btn=140
width_tut_btn=180


height_start_btn=40
height_quit_btn=40
height_tut_btn=40

#game settings
level_selected=1
start_game=False
game_mask=False

while True: 
    breakflag=False
    for ev in pygame.event.get(): 
          
        if ev.type == pygame.QUIT: 
            pygame.quit() 
              
        #checks if a mouse is clicked 
        if ev.type == pygame.MOUSEBUTTONDOWN: 
              
            #if the mouse is clicked on the 
            # button the game is terminated 
            if x_quit_btn<= mouse[0] <= x_quit_btn+ width_quit_btn and y_quit_btn <= mouse[1] <= y_quit_btn+height_quit_btn: 
                pygame.quit() 
                breakflag=True
                break
            elif x_start_btn <= mouse[0] <= x_start_btn+width_start_btn and y_start_btn <= mouse[1] <= y_start_btn+height_start_btn: 
                start_game=True
                breakflag=True
                break
            elif x_tut_btn <= mouse[0] <= x_tut_btn+width_tut_btn and y_tut_btn <= mouse[1] <= y_tut_btn+height_tut_btn: 
                
                breakflag=True
                break
    if breakflag==True:
        break
                  
    # fills the screen with a color 
    screen.fill((60,25,60)) 
      
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos() 
      
    # if mouse is hovered on a button it 
    # changes to lighter shade 
    #start btn
    if x_start_btn <= mouse[0] <= x_start_btn+width_start_btn and y_start_btn<= mouse[1] <= y_start_btn+height_start_btn: 
        pygame.draw.rect(screen,color_light,[x_start_btn,y_start_btn,width_start_btn,height_start_btn]) 
    #tut_btn
    elif x_tut_btn <= mouse[0] <= x_tut_btn+width_tut_btn and y_tut_btn<= mouse[1] <= y_tut_btn+height_tut_btn: 
        pygame.draw.rect(screen,color_light,[x_tut_btn,y_tut_btn,width_tut_btn,height_tut_btn]) 
    #quit_btn
    elif x_quit_btn <= mouse[0] <= x_quit_btn+width_quit_btn and y_quit_btn<= mouse[1] <= y_quit_btn+height_quit_btn : 
        pygame.draw.rect(screen,color_light,[x_quit_btn,y_quit_btn,width_quit_btn,height_quit_btn]) 
    #not hovered above
    else:
        pygame.draw.rect(screen,color_dark,[x_start_btn,y_start_btn,width_start_btn,height_start_btn]) 
        pygame.draw.rect(screen,color_dark,[x_tut_btn,y_tut_btn,width_tut_btn,height_tut_btn])
        pygame.draw.rect(screen,color_dark,[x_quit_btn,y_quit_btn,width_quit_btn,height_quit_btn])
      
    # superimposing the text onto our button 
    screen.blit(text_quit , (x_quit_btn+50,y_quit_btn)) 
    screen.blit(text_start , (x_start_btn+50,y_start_btn)) 
    screen.blit(text_help , (x_tut_btn+50,y_tut_btn)) 
      
    # updates the frames of the game 
    pygame.display.update() 


if(start_game):

    game = Game(level=level_selected, mask_enabled=game_mask)
    game.run_game()

pygame.quit() 