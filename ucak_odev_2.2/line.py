import pygame
from color import *
from element import *
import math
class line:
    def __init__(self):
        self.noktalar=[]
        self.editing="Now"
    def draw(self,pencere):
        if len(self.noktalar)==2:
            boyut=7
            pygame.draw.line(pencere,color.beyaz,(self.noktalar[0][0],self.noktalar[0][1]),(self.noktalar[1][0],self.noktalar[1][1]),2)
            pygame.draw.circle(pencere, color.kırmızı, self.noktalar[0], boyut)
            pygame.draw.circle(pencere, color.kırmızı, self.noktalar[1], boyut)
            orta=((self.noktalar[0][0]+self.noktalar[1][0])//2,(self.noktalar[0][1]+self.noktalar[1][1])//2)
            pygame.draw.circle(pencere, color.kırmızı, orta, boyut)
        if pygame.mouse.get_pressed()[2]:
            x,y=pygame.mouse.get_pos()
            if x<self.noktalar[0][0]+boyut and x>self.noktalar[0][0]-boyut and y<self.noktalar[0][1]+boyut and y>self.noktalar[0][1]-boyut:
                return "sil"
            if x<self.noktalar[1][0]+boyut and x>self.noktalar[1][0]-boyut and y<self.noktalar[1][1]+boyut and y>self.noktalar[1][1]-boyut:
                return "sil"
            if x<orta[0]+boyut and x>orta[0]-boyut and y<orta[1]+boyut and y>orta[1]-boyut:
                return "sil"
    @staticmethod
    def save_lines(llist):
        dosya = open("lines.data", "w")
        for i in llist:
            dosya.write(str(i.noktalar[0][0]) + " ")
            dosya.write(str(i.noktalar[0][1]) + " ")
            dosya.write(str(i.noktalar[1][0]) + " ")
            dosya.write(str(i.noktalar[1][1]) + " ")
            dosya.write("\n")
        dosya.close()



