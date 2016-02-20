import pygame
import sys
import random
import Button
import Button1
import MSG
import time
import array
import Soldat
from pygame import *
from array import *
from Soldat import *

white = (255,255,255)
black = (0,0,0)
blue = (0,0,200)
green = (0,200,0)
matx = 0
color = 0
color2 = 0
pygame.init()
display = display.set_mode((1000,700))
xFelder = 37
yFelder = 20

xObjektfelderFelder = 5
yObjektFelder = 2
class game(display):
    xFelder = 37
    yFelder = 20

    xObjektFelder = 5
    yObjektFelder = 2

    xposObj = 400
    xposAN = xposObj 
    yposObj = 600
    
    pygame.init()
    display.fill(white)
    running = True
    xpos = 0
    ypos = 0
    ObjektFelder = [[0 for x in range(25)]for x in range(37)]
    for i in range(yObjektFelder):
        for x in range(xObjektFelder):
            ObjektFelder[x][i] = Button1.to_screen("2",25,xposObj,yposObj,(255,255,255),(0,0,200),25,25,display,x,i,True)
            xposObj+= 27
        xposObj = xposAN
        yposObj+= 27
    ###################
    xpos = 0
    ypos = 0
    Feld = [[0 for x in range(25)]for x in range(37)]
    for i in range(yFelder):
        #to_screen1 = Button1.to_screen("",25,25,25,(0,0,200),(0,0,0),25,25,display)
        for x in range(xFelder):
            y = random.randrange(2)
            #l.append(Button1.to_screen("",25,xpos,ypos,(255,255,255),(0,0,200),25,25,display))
            if y == 0:
                Feld[x][i] = Button1.to_screen("2",25,xpos,ypos,(255,255,0),(0,0,200),25,25,display,x,i,True)
            else:
                Feld[x][i] = Button1.to_screen("2",25,xpos,ypos,(255,255,255),(0,0,200),25,25,display,x,i,True)
            xpos+= 27
        xpos = 0
        #l.append(Button1.to_screen("",25,xpos,ypos,(255,255,255),(0,0,200),25,25,display))
        #Feld[i,x] = Button1.to_screen("",25,xpos,ypos,(255,255,255),(0,0,200),25,25,display)
        ypos+= 27
    ##################
    Soldat1 = Soldat(Feld[2][3],display)
    #Soldat1.update(Feld)
    xpos = 0
    ypos = 0
    click = pygame.mouse.get_pressed()
    #Feld[0][0].color = (255,0,0)
    while running:
        for i in range(yFelder):
            for x in range(xFelder):
                Feld [x][i].update()
        for i in range(yObjektFelder):
            for x in range(xObjektFelder):
                ObjektFelder[x][i].update()
        Soldat1.Bewegung(Feld)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
                sys.exit()
                pygame.quit()
            if event.type == KEYDOWN: 
                if event.key == K_w:
                    Feld[Soldat1.matx][Soldat1.maty] = Button1.to_screen("2",25,Soldat1.xpos-5,Soldat1.ypos-5,Feld[Soldat1.matx][Soldat1.maty].color,(0,0,200),25,25,display,Soldat1.matx,Soldat1.maty)
                    #Feld[Soldat1.matx][Soldat1.maty] = Button1.to_screen("2",25,xpos,ypos,(255,255,255),(0,0,200),25,25,display,Soldat1.matx,Soldat1.maty)
                    Soldat1.maty -= 1
                    Feld[Soldat1.matx][Soldat1.maty].maty -= 1
                    Soldat1.Grafik(Feld[2][3])
                    #Soldat1.Button = None
                    #print(Soldat1.maty)
                if event.key == K_s:
                    Feld[Soldat1.matx][Soldat1.maty] = Button1.to_screen("2",25,Soldat1.xpos-5,Soldat1.ypos-5,Feld[Soldat1.matx][Soldat1.maty].color,(0,0,200),25,25,display,Soldat1.matx,Soldat1.maty)
                    #Feld[Soldat1.matx][Soldat1.maty] = Button1.to_screen("2",25,xpos,ypos,(255,255,255),(0,0,200),25,25,display,Soldat1.matx,Soldat1.maty)
                    Soldat1.maty += 1
                    Feld[Soldat1.matx][Soldat1.maty].maty += 1
                    Soldat1.Grafik(Feld[2][3])
                    #Soldat1.Button = None
                    #print(Soldat1.maty)
                if event.key == K_d:
                    Feld[Soldat1.matx][Soldat1.maty] = Button1.to_screen("2",25,Soldat1.xpos-5,Soldat1.ypos-5,Feld[Soldat1.matx][Soldat1.maty].color,(0,0,200),25,25,display,Soldat1.matx,Soldat1.maty)
                    #Feld[Soldat1.matx][Soldat1.maty] = Button1.to_screen("2",25,xpos,ypos,(255,255,255),(0,0,200),25,25,display,Soldat1.matx,Soldat1.maty)
                    Soldat1.matx += 1
                    Feld[Soldat1.matx][Soldat1.maty].matx += 1
                    Soldat1.Grafik(Feld[2][3])
                    #Soldat1.Button = None
                    #print(Soldat1.maty)
                if event.key == K_a:
                    Feld[Soldat1.matx][Soldat1.maty] = Button1.to_screen("2",25,Soldat1.xpos-5,Soldat1.ypos-5,Feld[Soldat1.matx][Soldat1.maty].color,(0,0,200),25,25,display,Soldat1.matx,Soldat1.maty)
                    #Feld[Soldat1.matx][Soldat1.maty] = Button1.to_screen("2",25,xpos,ypos,(255,255,255),(0,0,200),25,25,display,Soldat1.matx,Soldat1.maty)
                    Soldat1.matx -= 1
                    Feld[Soldat1.matx][Soldat1.maty].matx -= 1
                    Soldat1.Grafik(Feld[Soldat1.matx][Soldat1.maty])
                    #Soldat1.Button = None
                    #print(Soldat1.maty)
                    

game(display)
