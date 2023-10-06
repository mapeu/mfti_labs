import pygame
from pygame.draw import *
from random import randint

class Ball:
    def __init__(self, x: float, y:float, r:float):
        """x, y - coordinates of ball's center
        r - radius of ball
        color - colour of ball
        speed - speed of ball
        """
        self.x = x
        self.y = y
        self.r = r
        self.color = (randint(1, 255), randint(1, 255), randint(1, 255))
        self.speed = randint(1, 10) / 10
        self.vector = [randint(-1, 1), randint(-1, 1)]#В каком направлении будет двигаться шарик


    def draw_ball(self, screen: pygame.display):#Зарисовка шарика
        circle(screen, self.color, (self.x, self.y), self.r)

    def move(self):#перемещаем шарик
        self.x += self.vector[0] * self.speed
        self.y += self.vector[1] * self.speed

    def check_wall(self):#ПРоверка на столкновение, если столкнулись двигаемся в противоположном направлении
        if self.x >= 1000 or self.x <= 0:
            self.vector[0] *= -1
        if  self.y >= 1000 or self.y <= 0:
            self.vector[1] *= -1
