import pygame
from pygame.draw import *

pygame.init()

BLACK = (0, 0, 0)
YELLOW = (225, 225, 0)
RED = (255, 0, 0)
BEJE = (245, 245, 220)

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, BEJE, (0, 0, 400, 400))
circle(screen, YELLOW, (200, 200), 150)
circle(screen, RED, (130, 150), 25)
circle(screen, RED, (270, 150), 16)
circle(screen, BLACK, (130, 150), 12.5)
circle(screen, BLACK, (270, 150), 8)
rect(screen, BLACK, (125, 250, 150, 30))
polygon(screen, BLACK, [[80, 90], [60, 100], [160, 140], [180, 130]])
polygon(screen, BLACK, [[350, 90], [330, 120], [220, 160], [240, 130]])



pygame.display.update()
clock = pygame.time.Clock()

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
