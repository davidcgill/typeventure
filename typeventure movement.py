# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 19:36:12 2018

@author: gilld

words:
    during battle show all possible actions for the weapon combo
    or
    show like 8 options at a time
        need defesive 
        passive 
        offence sections
        
        
        ..if real time shouldn't be too turn baseds
        .. just have them in different boxes if the guy is swinging look to deffensive block (starts to glow)
"""

import pygame
import typefuncs1
void =0
black=(0,0,0)#black is all colours at a min
white=(255,255,255)#white is all colours at a max
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

display_width=800
display_hieght=600

#main does setup and calls the main loop
pygame.init()


# setting up the window (surface).. pass width and height (one single argument, tuple)
gameDisplay = pygame.display.set_mode((display_width,display_hieght))  #top left is 0,0 ... soemthimes better to make these variables
gameDisplay.fill(black)
#puts a label on the window to help the user know whats going on
pygame.display.set_caption('typeventure')


clock=pygame.time.Clock()

char=pygame.image.load("noback.png")

char_spot=char.get_rect()
char_spot.center=(display_width/2,display_hieght/2)


gameDisplay.blit(char,char_spot)
pygame.display.update()
def movelogic():
    x_diviation=0
    y_diviation=0
    type_string=""
    done=0
    command=void
    while not done:
             for event in pygame.event.get():
                 if (event.type== pygame.QUIT):
                    done=1
                    
                        
                 if (event.type == pygame.KEYDOWN):
                     type_string,command,done =typefuncs1.key_checker(event.key,type_string)
                     if len(type_string)>53:
                         type_string= type_string[0:-1]  # if the string is too long trucate it.. may later consider shrinking
                     gameDisplay.fill(black)
                     
                     if command != void:
                         if command==1:
                             x_diviation+=10
                         elif command==2:
                             y_diviation+=10
                         elif command==3:
                             x_diviation-=10
                         elif command==4:
                             y_diviation-=10  # up is decreasing y to get closer to 0,0 in the top right
                     
                     char_spot.center=(display_width/2+x_diviation,display_hieght/2+y_diviation)
                     gameDisplay.blit(char,char_spot)
                     typefuncs1.text_display(type_string,(display_width/2,display_hieght-50),gameDisplay)
    
                 
    pygame.quit()
    quit()

if __name__=="__main__":
    movelogic()