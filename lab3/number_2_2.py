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
x, y = 10, 260  # making "waves beetween sun and sea". This is start coordinations.
for i in range(8):
    circle(screen, FOR_SEA, (x, y), 40, draw_bottom_left=True, draw_bottom_right=True)  # sea half - circle
    x += 68
    y += 159 ** 0.5 + 30  # change coordintaes to draw beach half-circle
    circle(screen, YELLOW, (x, y), 40, draw_top_left=True, draw_top_right=True)
    x += 68
    y -= 159 ** 0.5 + 30  # change cords fo next sea circle


def draw_sun(x, y, radius, screen, color):  # sun
    '''Func that makes a sun. First 2 paramets - center of sun, 3 - rd radius of main part of sun'''
    circle(screen, color, (x, y), radius)  # cirlce of sun
    phi = [i for i in range(int(180 * 2 / math.pi))]  # I will make a lights as triangles
    x1 = [math.cos(angle + math.pi / 3) * radius / 3 + x for angle in
          phi]  # 2 coordinates of which will "ride" on 2 circles
    y1 = [math.sin(angle + math.pi / 3) * radius / 3 + y for angle in phi]  # different radius, with angle step = pi / 3
    x2 = [math.cos(angle) * (radius + 10) + x for angle in phi]
    y2 = [math.sin(angle) * (radius + 10) + y for angle in phi]
    for i in range(len(x1)):  # the main cicle to draw triangles
        polygon(screen, color, [[x, y], [x1[i], y1[i]], [x2[i], y2[i]]])


draw_sun(350, 50, 40, screen, YELLOW)

circle(screen, WHITE, (60, 40), 20)  # start making clouds
circle(screen, BLACK, (60, 40), 20, 1)  # 1-st cloud
circle(screen, WHITE, (75, 40), 20)  # borders of cloud and etc.
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
rect(screen, BLACK, (210, 200, 150, 30), 1)  # the main part of float
polygon(screen, BROWN, [[360, 200], [400, 200], [360, 230]])  # nose right
polygon(screen, BLACK, [[360, 200], [400, 200], [360, 230]], 1)  # borders
circle(screen, BLACK, (370, 212), 8)  # window
circle(screen, WHITE, (370, 212), 6)  # border
circle(screen, BROWN, (210, 200), 30)  # second nose(left)
circle(screen, BLACK, (210, 200), 30, 1)  # making a circle(to take left-bottom part of it):(
rect(screen, FOR_SEA, (0, 180, 400, 20))  # deleting false parts
rect(screen, FOR_SKY, (0, 170, 400, 10))
rect(screen, BROWN, (210, 200, 150, 30))
rect(screen, BLACK, (210, 200, 150, 30), 1)
line(screen, BROWN, [240, 200], [360, 200])  # end of deleting false parts
rect(screen, BLACK, (285, 125, 5, 75))  # flag. The main part
polygon(screen, BEJE, [[290, 125], [300, 162.5], [320, 162.5]])  # 1-st part of flag
polygon(screen, BLACK, [[290, 125], [300, 162.5], [320, 162.5]], 1)  # border for it
polygon(screen, BEJE, [[290, 200], [300, 162.5], [320, 162.5]])  # 2-nd part
polygon(screen, BLACK, [[290, 200], [300, 162.5], [320, 162.5]], 1)  # border.End of float.

# Start of canopy
rect(screen, BROWN, (50, 260, 5, 120))  # pillar
polygon(screen, FOR_ROOF, [[52.5, 260], [92.5, 290], [12.5, 290]])  # roof
aaline(screen, BLACK, [52.5, 260], [20, 290])  # lines on a roof
aaline(screen, BLACK, [52.5, 260], [40, 290])
aaline(screen, BLACK, [52.5, 260], [60, 290])
aaline(screen, BLACK, [52.5, 260], [80, 290])  # end of roof

# to see everything on a screen
pygame.display.update()
clock = pygame.time.Clock()

# cathing events
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
