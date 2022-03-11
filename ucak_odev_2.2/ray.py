import pygame
import math
from color import *
class dogru:
    def __init__(self,x1,y1,x2,y2):
        #Y=mX+n
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        if x1!=x2:
            self.m=(y1-y2)/(x1-x2)
            self.n=y1-self.m*x1
        else:
            self.m="tanımsız"
            self.n=0


    def kesisim_bul(self,d2):
        deger=0
        if self.m!=d2.m:
            if self.m == "tanımsız" and d2.m != "tanımsız":
                deger= (round(self.x1), round(d2.m * self.x1 + d2.n))
            if self.m != "tanımsız" and d2.m == "tanımsız":
                deger= (round(d2.x1), round(self.m * d2.x1 + self.n))
            if self.m != "tanımsız" and d2.m != "tanımsız":
                x=(d2.n-self.n)/(self.m-d2.m)
                deger= (round(x),round(self.m*x+self.n))
            if deger!=0:
                if max(d2.x1,d2.x2)+5>deger[0] and min(d2.x1,d2.x2)-5<deger[0] and max(self.x1,self.x2)+5>deger[0] and min(self.x1,self.x2)-5<deger[0]:
                    if max(d2.y1,d2.y2)+5>deger[1] and min(d2.y1,d2.y2)-5<deger[1] and max(self.y1,self.y2)+5>deger[1] and min(self.y1,self.y2)-5<deger[1]:
                        return deger



class ray:
    def __init__(self,x=0,y=0):
        self.aci=0
        self.boyut=200
        self.x=x
        self.y=y
    def draw_ray(self,pencere,x,y,line_list):
        self.aci-=1
        self.x=x
        self.y=y
        n1=(x+self.boyut*math.cos(math.radians(self.aci)),y-self.boyut*math.sin(math.radians(self.aci)))
        n2 = (x + self.boyut * math.cos(math.radians(self.aci+90)), y - self.boyut * math.sin(math.radians(self.aci+90)))
        n3 = (x + self.boyut * math.cos(math.radians(self.aci+180)), y - self.boyut * math.sin(math.radians(self.aci+180)))
        n4 = (x + self.boyut * math.cos(math.radians(self.aci+270)), y - self.boyut * math.sin(math.radians(self.aci+270)))
        d1 = dogru(n1[0], n1[1], x, y)
        d2 = dogru(n2[0], n2[1], x, y)
        d3 = dogru(n3[0], n3[1], x, y)
        d4 = dogru(n4[0], n4[1], x, y)

        n1 = self.engellenen_nokta_bul(d1, line_list)
        n2 = self.engellenen_nokta_bul(d2, line_list)
        n3 = self.engellenen_nokta_bul(d3, line_list)
        n4 = self.engellenen_nokta_bul(d4, line_list)

        pygame.draw.line(pencere, color.yeşil, n1, (x, y), 2)
        pygame.draw.line(pencere, color.yeşil, n2, (x, y), 2)
        pygame.draw.line(pencere, color.yeşil, n3, (x, y), 2)
        pygame.draw.line(pencere, color.yeşil, n4, (x, y), 2)


    def uzaklik(self,x1,y1,x2,y2):
        return ((y2-y1)**2+(x2-x1)**2)**0.5

    def engellenen_nokta_bul(self,d1,line_list):
        liste=[]
        Min=self.boyut #çok büyük bir sayı başlangıç için min değer gibi ...
        nokta=(d1.x1,d1.y1)#rastgele en yakın nokta
        for i in line_list:
            d5=dogru(i.noktalar[0][0],i.noktalar[0][1],i.noktalar[1][0],i.noktalar[1][1])
            if d5.kesisim_bul(d1)!=None:
                mesafe=self.uzaklik(d5.kesisim_bul(d1)[0],d5.kesisim_bul(d1)[1],self.x,self.y)

                if mesafe<Min:
                    Min=mesafe
                    nokta=d5.kesisim_bul(d1)
        return nokta

