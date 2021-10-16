from os import path
import pygame as pg

player_img = pg.image.load("main_hero1.png")
player_img = pg.transform.scale(player_img, (128, 128))
class Player(object):
    def __init__(self, name, screen):
        self.name = name
        self.screen = screen
        self.x, self.y = 300, 300

    def draw(self):
        self.update()
        self.screen.blit(player_img, (self.x, self.y))

    def update(self):
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT]:
            self.x += -8
        if keystate[pg.K_RIGHT]:
            self.x += 8










