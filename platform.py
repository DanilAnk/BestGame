import pygame as pg


class Form(object):
    def __init__(self, height, wight, pos, color, screen):
        self.height = height
        self.wight = wight
        self.x, self.y = pos
        self.color = color
        self.screen = screen

    def draw(self):
        pg.draw.rect(self.screen, self.color, (self.x, self.y, self.wight, self.height))

    def show_text(self, txt, color, size):
        f1 = pg.font.Font(None, size)
        text1 = f1.render(txt, True, color)
        self.screen.blit(text1, (self.x, self.y))






