import pygame
from text import *
from color import *

class tiklama:
    durum=[0,0,0]
    @classmethod
    def click(cls,m):
        if pygame.mouse.get_pressed()[m] and cls.durum[m]==0:
            cls.durum[m]=1
            return True
        if pygame.mouse.get_pressed()[m]==0:
            cls.durum[m]=0
            return False

class buton:
    def __init__(self,x=0,y=0,size_x=50,size_y=50):
        self.x=x
        self.y=y
        self.size_x=size_x
        self.size_y=size_y
        self.string_text="BUTON"
        self.string_rengi = color.siyah
        self.string_arkaplan_rengi = color.beyaz
        self.Tiklama=tiklama()
        self.string=text.printText(self.string_text,self.string_rengi,self.string_arkaplan_rengi)
        self.color=color.beyaz
    def draw(self,pencere):
        pygame.draw.rect(pencere,self.color,((self.x,self.y),(self.size_x,self.size_y)),int(max(self.size_x,self.size_y)/2))
        pencere.blit(self.string,(self.x+self.size_x//2-self.string.get_size()[0]//2,self.y+self.size_y//2-self.string.get_size()[1]//2))

    def setStringText(self,string):
        self.string_text=string
        self.string=text.printText(self.string_text,self.string_rengi,self.string_arkaplan_rengi)

    def setStrnigColor(self,yazi_rengi,aprengi):
        self.string_rengi=yazi_rengi
        self.string_arkaplan_rengi=aprengi
        self.string=text.printText(self.string_text,self.string_rengi,self.string_arkaplan_rengi)
    def isClick(self):
        x,y=pygame.mouse.get_pos()
        if x > self.x and x < self.x + self.size_x and y > self.y and y < self.y + self.size_y:


            if tiklama.click(0):
                return True
            return False
