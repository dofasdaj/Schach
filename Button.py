import pygame
import MSG
import time
black = (0,0,0)
class to_screen:
    def __init__(self,msg,size,xpos,ypos,color,color2,höhe,breite,display):
        self.msg = msg
        self.size = size
        self.xpos = xpos
        self.ypos = ypos
        self.color = color
        self.color2 = color2
        self.höhe = höhe
        self.breite = breite
        self.display = display
        font = pygame.font.SysFont(None, size)
        pygame.draw.rect(display,black,(xpos-1,ypos-1,breite+2,höhe+2))
        pygame.draw.rect(display,color,(xpos,ypos,breite,höhe))
        MSG.to_screen(msg,black,xpos+15,höhe/2+ypos-15,size,display)
    def update(self):
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.xpos+self.breite>cur[0]>self.xpos and self.ypos+self.höhe>cur[1]>self.ypos:
            pygame.draw.rect(self.display,self.color2,(self.xpos,self.ypos,self.breite,self.höhe))
            if click[0] == 1:
                pygame.draw.rect(self.display,(0,255,0),(self.xpos,self.ypos,self.breite,self.höhe))
        else:
            pygame.draw.rect(self.display,self.color,(self.xpos,self.ypos,self.breite,self.höhe))
    
