import pygame

from worm import *

FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 800

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

worm1 = Worm(100, 200, "worm.bmp", "left")
worm2 = Worm(100, 600, "worm.bmp", "left")
worm3 = Worm(700, 200, "worm.bmp", "right")
worm4 = Worm(700, 600, "worm.bmp", "right")
worms = [worm1, worm2, worm3, worm4]
current_worm = worms[0]

bullets =[]

finished = False

pygame.display.update()

clock = pygame.time.Clock()

while not finished:
    pygame.display.update()
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            current_worm.gun.ready_shoot(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            bullets.append(current_worm.gun.shoot(event))
            current_worm = (worms[worms.index(current_worm) + 1] if worms.index(current_worm) != 3 else worms[0])
        elif event.type == pygame.MOUSEMOTION:
            current_worm.gun.aim(event)
        elif event.type == pygame.KEYDOWN:
            current_worm.move(event)

    for bullet in bullets:
        if bullet.time < 100:
            bullet.move()
            bullet.draw(screen, (100, 100, 100))
        else:
            bullets.remove(bullet)

    for worm in worms:
        worm.draw(screen)
        for bullet in bullets:
            worm.hit(bullet)



pygame.quit()


