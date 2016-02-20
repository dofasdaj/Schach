import pygame
import MSG
import Button1
from pygame import *
class Soldat:
    def __init__(self,feld,display):
        self.feld = feld
        self.lebenspunkte = 100
        self.xpos = feld.xpos + 5
        self.ypos = feld.ypos + 5
        self.Waffe = [""]
        self.display = display
        self.pos = False
        self.matx = feld.matx
        self.maty = feld.maty
        self.matxBew = 1
        #self.Button = Button1.to_screen("",5,self.xpos,self.ypos,(255,255,255),(0,0,200),15,15,self.display,self.matx,self.maty)
    def Bewegung(self,Feld):
        #self.Button.update()
        self.color = (0,0,0)
        self.color2 = (0,0,0)
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        Button1.to_screen("",5,self.xpos,self.ypos,(255,255,255),(0,0,200),15,15,self.display,self.matx,self.maty)
        if self.xpos+25>cur[0]>self.xpos and self.ypos+25>cur[1]>self.ypos:
            if click[0] == 1:
                pygame.draw.rect(self.display,self.color,(self.xpos-5,self.ypos-5,25,25))
                self.Button = Button1.to_screen("",5,self.xpos,self.ypos,(255,255,255),(0,0,200),15,15,self.display,self.matx,self.maty)
                #if Feld[self.matx+1][self.maty] == Feld:
                Feld[self.matx+1][self.maty].color = (255,0,0)
                #Feld[self.maty+1][self.maty].color = (255,0,0)
                #Feld[self.matx-1][self.maty].color = (255,0,0)
                #Feld[self.maty-1][self.maty].color = (255,0,0)
            #def update(self,Feld):
        #Feld[self.matx+1][self.maty].color = (255,0,0)
        
    def Grafik(self,feld):
        self.feld.ypos = self.maty*27
        self.feld.xpos = self.matx*27
        self.xpos = self.feld.xpos + 5
        self.ypos = self.feld.ypos +5
        self.Button = Button1.to_screen("",5,self.xpos,self.ypos,(255,255,255),(0,0,200),15,15,self.display,self.matx,self.maty)
        
        
