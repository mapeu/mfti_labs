import pygame
import math
from pygame.draw import *

# инициализации библиотеки
pygame.init()

# define screen
FPS = 30
screen = pygame.display.set_mode((400, 400))

# define colors
BLACK = (0, 0, 0)
YELLOW = (225, 225, 0)
WHITE = (255, 255, 255)
BEJE = (245, 245, 220)
BROWN = (128, 64, 48)
FOR_ROOF = (170, 64, 48)
FOR_SEA = (0, 77, 255)
FOR_SKY = (48, 213, 200)

rect(screen, FOR_SKY, (0, 0, 400, 180))  # skies
rect(screen, FOR_SEA, (0, 180, 400, 100))  # sea
rect(screen, YELLOW, (0, 280, 400, 120))  # beach
x, y = 10, 280
for i in range(8):
    circle(screen, YELLOW, (x, y), 52)
    x += 52
    y += 5
    circle(screen, FOR_SEA, (x, y), 52)
    x += 52
    y -= 5


def draw_sun(x, y, radius, screen, color):  # sun
    circle(screen, color, (x, y), radius)
    phi = [i / 2 for i in range(int(180 * 2 / math.pi))]
    x1 = [math.cos(angle) * radius / 2 + x for angle in phi]
    y1 = [math.sin(angle) * radius / 2 + y for angle in phi]
    x2 = [math.cos(angle) * (radius + 10) + x for angle in phi]
    y2 = [math.sin(angle) * (radius + 10) + y for angle in phi]
    for i in range(len(x1)):
        polygon(screen, color, [[x, y], [x1[i], y1[i]], [x2[i], y2[i]]])


draw_sun(350, 50, 40, screen, YELLOW)
circle(screen, WHITE, (60, 40), 20)  # start making clouds
circle(screen, BLACK, (60, 40), 20, 1)
circle(screen, WHITE, (75, 40), 20)
circle(screen, BLACK, (75, 40), 20, 1)
circle(screen, WHITE, (90, 40), 20)
circle(screen, BLACK, (90, 40), 20, 1)
circle(screen, WHITE, (50, 50), 20)
circle(screen, BLACK, (50, 50), 20, 1)
circle(screen, WHITE, (65, 55), 20)
circle(screen, BLACK, (65, 55), 20, 1)
circle(screen, WHITE, (83, 55), 20)
circle(screen, BLACK, (83, 55), 20, 1)
circle(screen, WHITE, (98, 50), 20)
circle(screen, BLACK, (98, 50), 20, 1)  # finished to make clouds
rect(screen, BROWN, (210, 200, 150, 30))  # start making float
rect(screen, BLACK, (210, 200, 150, 30), 1)
polygon(screen, BROWN, [[360, 200], [400, 200], [360, 230]])  # nose
polygon(screen, BLACK, [[360, 200], [400, 200], [360, 230]], 1)
circle(screen, BLACK, (370, 212), 8)  # window
circle(screen, WHITE, (370, 212), 6)
circle(screen, BROWN, (210, 200), 30)  # second nose
circle(screen, BLACK, (210, 200), 30, 1)
rect(screen, FOR_SEA, (0, 180, 400, 20))
rect(screen, FOR_SKY, (0, 170, 400, 10))
rect(screen, BROWN, (210, 200, 150, 30))
rect(screen, BLACK, (210, 200, 150, 30), 1)
line(screen, BROWN, [240, 200], [360, 200])
rect(screen, BLACK, (285, 125, 5, 75))  # flag
polygon(screen, BEJE, [[290, 125], [300, 162.5], [320, 162.5]])
polygon(screen, BLACK, [[290, 125], [300, 162.5], [320, 162.5]], 1)
polygon(screen, BEJE, [[290, 200], [300, 162.5], [320, 162.5]])
polygon(screen, BLACK, [[290, 200], [300, 162.5], [320, 162.5]], 1)
rect(screen, BROWN, (50, 260, 5, 120))  # roof
polygon(screen, FOR_ROOF, [[52.5, 260], [92.5, 290], [12.5, 290]])
aaline(screen, BLACK, [52.5, 260], [20, 290])
aaline(screen, BLACK, [52.5, 260], [40, 290])
aaline(screen, BLACK, [52.5, 260], [60, 290])
aaline(screen, BLACK, [52.5, 260], [80, 290])

# to see everything on a screen
pygame.display.update()
clock = pygame.time.Clock()

# cathing events
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
