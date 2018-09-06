# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 14:12:50 2018

@author: david

type tester:
    this program shows a word
    it shows what you have typed
    it has a 30 second countdown
    hit enter to move to next word  .... i could do letters per min and say average word is 4 or limit word size from 1 to 6 letters

    words typed/0.5 to get words per minute
    display score
    allow for play agian or quick

Future add ons:
    words flying at the wall
        words flying faster with time
        difficulty level changes lives and word length
        make a scoring system
        ... doesn't help me make my end goal but does help learn animation of motion
"""
#need this every time to make a something in pygame
import pygame, random
''' colours are not deffined so to decect we need to store them as rgb values
note how i put them outside all the functions therefor they are gobal and can be accessed anywhre.. also note the are tuples'''


#main does setup and calls the main loop
pygame.init()


# setting up the window (surface).. pass width and height (one single argument, tuple)

#define the games clock (sync everything with this)


#if you want to insert images
''' background=pygame.image.load("random_backdrop.jpg")  #insert with file name.. or if somewhere else on computer use full path
 gameDisplay.blit(background,(400,300)) #blit draws, order in which you draw layers it'''


black=(0,0,0)#black is all colours at a min
white=(255,255,255)#white is all colours at a max
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

#def high_score_checker(myscore):
#    infile=open("highscores.txt","r")
#    highscores=[]
#    highnames=[]
#    updated=0
#    scores=infile.readlines()
#    ypos=0
#    for words in scores:
#        words=words.split(" ")
#
#        #display the highscores
#        text_display(words[0], (display_width/4, 20+ypos))
#        text_display(words[1], (display_width/2+display_width/4, 20+ypos))
#
#        highnames.append(words[0])
#        highscores.append(words[1])
#        ypos+=30
#
#    infile.close()
#    #above this point reads the file and displays them on screen
#
#    index=0
#
#    for score in highscores:
#        #this loop checks if we beat the high score
#        if myscore>= eval(score):
#            #     once a high score is beat
#
#            text_display("please type your name to be put into the hall of records",(display_width/2, display_hieght/2+40))
#            text_display("Hit enter or space to confirm",(display_width/2, display_hieght/2+80))
#            score_string= "your score is "+str(myscore)
#            pygame.display.update()
#            done=0
#            name=""
#            while not done:
#                #let them type thier name and then wait for enter or sapce click
#                for event in pygame.event.get():
#                    if (event.type == pygame.KEYDOWN):
#                        name,done =key_checker(event.key,name)
#                        gameDisplay.fill(green)
#                        text_display("please type your name to be put into the hall of records",(display_width/2, display_hieght/2+40))
#                        text_display("Hit enter or space to confirm",(display_width/2, display_hieght/2+80))
#                        text_display(name, (display_width/2, display_hieght/2+120))
#                        score_string= "your score is "+str(myscore)
#                        text_display(score_string,(display_width/2, display_hieght/2))
#
#
#                        ypos=0
#                        prindex=0
#                        for words in highnames:
#
#                            #display the highscores
#                            text_display(words, (display_width/4, 20+ypos))
#                            text_display(highscores[prindex], (display_width/2+display_width/4, 20+ypos))
#
#                            ypos+=30
#                            prindex+=1
#
#                pygame.display.update()
#
#            highscores.insert(index,str(myscore)+"\n")
#            highnames.insert(index,name)
#            highnames.pop(-1)
#            highscores.pop(-1)
#            updated=1
#            break
#        index+=1
#    if updated:
#        index=0
#        outfile=open("highscores.txt","w")
#        for name in highnames:
#            print (f"{name} {highscores[index]}",file=outfile,end="")
#            index+=1
#        outfile.close()


#use for mining or whatever typing words gets you resources
# certain speeds to craft certain items..
def get_rand_words():
    #adding my text file
    words=[]
    chosen_ones=[]
    wordfile=open("words.txt","r")  #maybe use more topical words
    multi_words_per_line=wordfile.readlines()
    for word_string in multi_words_per_line:
        words+= word_string.split()
    length=len(words)
    #let's prelaod 100 words for each time (they can get up to 200 wpm).. this will make it run faster
    for x in range(0,100):
        index=random.randint(0,length-1)
        chosen_ones.append( words[index] )
    wordfile.close()
    return chosen_ones


def Get_battle_words(sword,ranged,shield):
    
    d_words=[]
    a_words=[]
    p_words=[]
    skip=0
    
    section_num=0  # section 1 =d 2 is ofecfe and 3 is passive
    
    wordfile= open("battlewords.txt","r")
    words=wordfile.readline()
    for word in words:
        if word=="\n":
            pass
        elif word.lfind(":"):
            section_num+=1
            skip=0
        else:
            if section_num==1:
                if word.lfind(";"):  #skip to the next section if not equiped
                    skip =0
                    if word.find("shield")not shield:
                        skip=1
                if not skip:
                    d_words.append(word)
                    
                    
            elif section_num==2:
                if word.lfind(";"):
                    skip=0
                    if word.find("ranged") and not ranged:
                        skip=1
                        
                    elif word.find("sword") and not sword:
                        skip=1
                if not skip:
                    a_words.append(word)
            elif section_num==3:
                p_words.append(word)
                
        
    
    wordfile.close()
    return d_words, a_words,p_words


def text_display(text,location,surface):
    font =pygame.font.SysFont('arial',32)# type then size
    try:
       textSurface =font.render(text, True , white )# makes a text retangle
    except TypeError:
        print("sorry we couldn't print that, make sure you are passing strings")
        return
    else:
        text_rectangle= textSurface.get_rect()
        text_rectangle.center=(location) #this centers it at location
        surface.blit(textSurface,text_rectangle)
        pygame.display.update()

def key_checker(key,type_string,spaces=1):
    void=0
    right=1
    down=2
    left=3
    up=4
    
    
    if(key == pygame.K_a):
        type_string +="a"
    elif(key == pygame.K_b):
        type_string+="b"
    elif(key == pygame.K_c):
        type_string+="c"
    elif(key == pygame.K_d):
        type_string+="d"
    elif(key == pygame.K_e):
        type_string+="e"
    elif(key == pygame.K_f):
        type_string+="f"
    elif(key == pygame.K_g):
        type_string+="g"
    elif(key == pygame.K_h):
        type_string+="h"
    elif(key == pygame.K_i):
        type_string+="i"
    elif(key == pygame.K_j):
        type_string+="j"
    elif(key == pygame.K_k):
        type_string+="k"
    elif(key == pygame.K_l):
        type_string+="l"
    elif(key == pygame.K_m):
        type_string+="m"
    elif(key == pygame.K_n):
        type_string+="n"
    elif(key == pygame.K_o):
        type_string+="o"
    elif(key == pygame.K_p):
        type_string+="p"
    elif(key == pygame.K_q):
        type_string+="q"
    elif(key == pygame.K_r):
        type_string+="r"
    elif(key == pygame.K_s):
        type_string+="s"
    elif(key == pygame.K_t):
        type_string+="t"
    elif(key == pygame.K_u):
        type_string+="u"
    elif(key == pygame.K_v):
        type_string+="v"
    elif(key == pygame.K_w):
        type_string+="w"
    elif(key == pygame.K_x):
        type_string+="x"
    elif(key == pygame.K_y):
        type_string+="y"
    elif(key == pygame.K_z):
        type_string+="z"
    elif(key == pygame.K_BACKSPACE):
        type_string= type_string[0:-1]
    elif(key == pygame.K_SPACE and spaces==0):
        return type_string,void,1
    elif(key == pygame.K_SPACE and spaces==1):
        type_string+=" "
    elif(key == pygame.K_RETURN):
        return type_string,void,1
    elif(key == pygame.K_RIGHT):
        return type_string,right,0
    elif(key == pygame.K_LEFT):
        return type_string,left,0
    elif(key == pygame.K_UP):
        return type_string,up,0
    elif(key == pygame.K_DOWN):
        return type_string,down,0
    return type_string,void,0


# return whT IS typed command string, what is done code
    #reutn code 