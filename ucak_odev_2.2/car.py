import pygame
import sys
import math
from color import *
from line import *
from ray import *
class car():
    ivme = 0.2
    surtunme=0.05
    def __init__(self):
        self.x = 0
        self.y = 0
        self.acı = 0
        self.hız = 0
        self.max_hız = 10
        self.visible=False
        self.ray=ray()
    def draw_car(self, pencere ,line_list, renk=color.kırmızı,):
        if self.visible:
            boyut=20
            nokta1 = (self.x + boyut * math.cos(math.radians(self.acı + 30)), self.y - boyut * math.sin(math.radians(self.acı + 30)))
            nokta2 = (self.x + boyut * math.cos(math.radians(self.acı + 150)), self.y - boyut * math.sin(math.radians(self.acı + 150)))
            nokta3 = (self.x + boyut * math.cos(math.radians(self.acı + 210)), self.y - boyut * math.sin(math.radians(self.acı + 210)))
            nokta4 = (self.x + boyut * math.cos(math.radians(self.acı + 330)), self.y - boyut * math.sin(math.radians(self.acı + 330)))


            pygame.draw.line(pencere, color.yeşil, nokta2, nokta1, 2)
            pygame.draw.line(pencere, color.yeşil, nokta2, nokta3, 2)
            pygame.draw.line(pencere, color.yeşil, nokta3, nokta4, 2)
            pygame.draw.line(pencere, renk, nokta4, nokta1, 2)

            self.ray.draw_ray(pencere,self.x,self.y,line_list)

            self.x += self.hız * math.cos(math.radians(self.acı))
            self.y -= self.hız * math.sin(math.radians(self.acı))


            if self.hız >= 0:
                self.hız -= self.surtunme
                if self.hız < 0:
                    self.hız = 0
            if self.hız <= 0:
                self.hız += self.surtunme
                if self.hız > 0:
                    self.hız = 0
            ###########################################
            if self.x > pygame.display.get_window_size()[0]:
                self.x = 0
            if self.x < 0:
                self.x = pygame.display.get_window_size()[0]
            if self.y > pygame.display.get_window_size()[1]:
                self.y = 0
            if self.y < 0:
                self.y = pygame.display.get_window_size()[1]
            ##################################################
            if self.hız > 0 and self.hız > self.max_hız:
                self.hız = self.max_hız
            elif self.hız < 0 and abs(self.hız) > self.max_hız:
                self.hız = -self.max_hız
            ###################################################
    def sur(self):
        if self.visible:
            tuslar = pygame.key.get_pressed()
            if tuslar[pygame.K_RIGHT] or tuslar[pygame.K_d] and self.hız:
                self.acı -= 0.8*self.hız

            elif tuslar[pygame.K_LEFT] or tuslar[pygame.K_a] and self.hız:
                self.acı += 0.8 * self.hız

            if tuslar[pygame.K_UP] or tuslar[pygame.K_w]:
                if self.hız >= 0:
                    self.hız += self.ivme
                else:
                    self.hız += 2 * self.ivme

            if tuslar[pygame.K_DOWN] or tuslar[pygame.K_s]:
                if self.hız <= 0:
                    self.hız -= self.ivme
                else:
                    self.hız -= 2 * self.ivme

