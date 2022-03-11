import pygame
from color import *
class text:
    size=20
    yazi_tipi="Veranda"
    @classmethod
    def printText(cls,string, yaziRengi =color.beyaz, arkaPlanRengi=color.siyah):
        yazi = pygame.font.SysFont(cls.yazi_tipi, cls.size)
        surface = yazi.render(string, True, yaziRengi, arkaPlanRengi)
        return surface