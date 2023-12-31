import pygame
from math import *
G = 1

class Bullet:
    def __init__(self, x, y, v, angle, side):
        self.x = x
        self.y = y
        self.v = v * 10
        self.angle = -angle
        self.r = 10
        self.side = side
        self.for_x = (1 if self.side == "left" else -1)#Для проверки в какую сторону будем стрелять
        self.time = 0
        self.start = [self.x, self.y]#Необходимо для хранения начальной позиции

    def move(self):
        self.time += 1
        self.x = self.v * cos(self.angle) * self.time * self.for_x + self.start[0]
        self.y = -self.v * sin(self.angle) * self.time + G * self.time ** 2 / 2 + self.start[1]

        if self.y + self.r >= 800:#отрабатываем удар об пол
            vx = self.v * cos(self.angle)
            self.v = sqrt((self.v * cos(self.angle)) ** 2 + (self.v * sin(self.angle) - G * self.time) ** 2)
            self.time = 0
            self.angle = acos(vx / self.v)
            self.v -= 2
            self.start = (self.x, 800)
        if self.x + self.r >= 800 or self.x - self.r <= 0:#Удар об боковые стены
            vx = self.v * cos(self.angle)
            self.v = sqrt((self.v * cos(self.angle)) ** 2 + (self.v * sin(self.angle) - G * self.time) ** 2)
            self.time = 0
            self.angle = acos(vx / self.v)
            self.v -= 2
            self.for_x *= -1
            self.start = (self.x, self.y)
    def draw(self, screen, color):
        pygame.draw.circle(screen, color, (self.x, self.y), self.r)

    def destroy(self):
        self.time = 100
