import pygame
import sys

import line
from color import *
from car import *
from text import *
from element import *
from appMode import *
from line import *
class app:
    def __init__(self):
        pygame.init()
        size = (pygame.display.get_desktop_sizes()[0][0]*0.9,pygame.display.get_desktop_sizes()[0][1]*0.8)

        pencere = pygame.display.set_mode(size)


        clock = pygame.time.Clock()

        btn_edit_car = buton(pygame.display.get_window_size()[0] - 100, 0, 100, 100)
        btn_edit_car.setStringText("Car editing")
        btn_edit_line = buton(pygame.display.get_window_size()[0] - 201, 0, 100, 100)
        btn_edit_line.setStringText("Line editing")

        info="Line editing mode"
        car1=car()
        line_list=[]
        dosya=open("lines.data","r")
        for i in dosya.readlines():
            line_list.append(line())
            line_list[-1].noktalar.append(tuple(map(int, i.split()[0:2])))
            line_list[-1].noktalar.append(tuple(map(int, i.split()[2:4])))
            line_list[-1].editing="End"
        dosya.close()


        while True:
            clock.tick(60)
            pencere.fill(color.siyah)

            car1.draw_car(pencere,line_list)

            ################################################
            if len(line_list):
                i=0
                while i < len(line_list):
                    if line_list[i].draw(pencere)=="sil":
                        del line_list[i]
                        line.save_lines(line_list)
                        i-=1
                    i+=1
            tuslar = pygame.key.get_pressed()

            ############################################
            if tuslar[pygame.K_ESCAPE]:
                sys.exit()
            if tuslar[pygame.K_e]:
                appMode.mode="E"
                appMode.editing = "L"
                info = "Line editing mode"
            if tuslar[pygame.K_r]:
                appMode.mode="R"
                info="Run Mode"
            ############################################################

            if appMode.mode == "E":
                btn_edit_line.draw(pencere)
                btn_edit_car.draw(pencere)
                ##########################
                if btn_edit_line.isClick():
                    appMode.editing="L"
                    info="Line editing mode"
                if btn_edit_car.isClick():
                    appMode.editing="C"
                    info="Car editing mode"
                ############################
                if appMode.editing=="C":
                    if tiklama.click(0):
                        car1.visible=True
                        car1.x,car1.y=pygame.mouse.get_pos()
                        car1.acı=0
                        car1.hız=0

                if appMode.editing=="L":
                    if tiklama.click(0):
                        line_list.append(line())
                        line_list[-1].noktalar.append(pygame.mouse.get_pos())
                    if len(line_list):
                        if pygame.mouse.get_pressed()[0] and line_list[-1].editing=="Now":
                            if len(line_list[-1].noktalar)==1:
                                line_list[-1].noktalar.append(pygame.mouse.get_pos())
                            else:
                                line_list[-1].noktalar[1]=pygame.mouse.get_pos()
                        elif pygame.mouse.get_pressed()[0]==0 and line_list[-1].editing=="Now":
                            line_list[-1].editing="End"
                            line.save_lines(line_list)

            if appMode.mode=="R":
                car1.sur()

            ###########################################
            pencere.blit(text.printText(info),(size[0]//2-text.printText(info).get_size()[0]/2,size[1]-50))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    line.save_lines(line_list)
                    sys.exit()

            pygame.display.update()


app()
