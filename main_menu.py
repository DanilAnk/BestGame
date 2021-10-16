import pygame as pg
from platform import Form


class Main_menu(object):
    def __init__(self, screen):
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (180, 0, 0)
        self.F1 = Form(70, 300, (250, 50), self.RED, screen)
        self.F2 = Form(70, 300, (250, 250), self.RED, screen)
        self.F3 = Form(70, 300, (250, 450), self.RED, screen)

    def draw(self):
        self.F1.draw()
        self.F1.show_text("Start", self.BLACK, 80)
        self.F2.draw()
        self.F2.show_text("Settings", self.BLACK, 72)
        self.F3.draw()
        self.F3.show_text("Exit", self.BLACK, 80)