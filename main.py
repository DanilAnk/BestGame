import pygame as pg
from platform import Form
from main_menu import Main_menu
from player import Player

WIDTH, HEIGHT, FPS = 800, 600, 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (180, 0, 0)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)
pg.display.set_caption("My Game")
clock = pg.time.Clock()

main_menu = Main_menu(screen)
danil = Player("Danil", screen)

main_menu_bool = True
playing = False
running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                if x >= main_menu.F1.x and x <= main_menu.F1.x + main_menu.F1.wight and main_menu_bool:
                    if y >= main_menu.F1.y and y <= main_menu.F1.y + main_menu.F1.height:
                        print("Very good")
                        main_menu_bool = False
                        playing = True
    if main_menu_bool:
        main_menu.draw()

    if playing:
        danil.draw()

    pg.display.update()
    screen.fill(WHITE)
    pg.time.delay(20)

pg.quit()
