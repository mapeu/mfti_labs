import pygame
from pygame.draw import *
from random import randint

class Rect:
    def __init__(self, x: float, y: float, width: float):
        """x, y - coordinates of rectangles top left
        width - width of rectangle
        color - colour of rect
        speed - speed of rect
        """
        self.x = x
        self.y = y
        self.width = width
        self.color = (randint(1, 255), randint(1, 255), randint(1, 255))
        self.speed = randint(1, 10) / 10
        self.vector = [randint(-1, 1), randint(-1, 1)]# куда двигается


    def draw_rect(self, screen: pygame.display):#Рисуем квадратик
        rect(screen, self.color, (self.x, self.y, self.width, self.width))

    def move(self):#Двигаем квадратик
        self.x += self.vector[0] * self.speed
        self.y += self.vector[1] * self.speed

    def check_wall(self):#Проверяем столкнулись ли со стеной, если да, то двигаемся в другую сторону
        if self.x >= 1000 - self.width or self.x <= 0:
            self.vector[0] *= -1
        if  self.y >= 1000 - self.width or self.y <= 0:
            self.vector[1] *= -1
