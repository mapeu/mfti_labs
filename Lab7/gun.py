import math
from random import choice
from random import random
from random import randint

import pygame


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
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 50

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.live -= 1#Укорачиваем время жизни объекта

        self.x += self.vx
        self.y -= self.vy - 10 * (50 - self.live)

        #Отрабокта отскакивания от стен
        if self.x + self.r >= 800 or self.x - self.r <= 0:
            self.vx *= -1

        if self.y + self.r >= 600:
            self.y += self.vy - 10 * (50 - self.live) - self.live

    def draw(self):
        global balls

        if self.live > 0:
            pygame.draw.circle(
                self.screen,
                self.color,
                (self.x, self.y),
                self.r
            )
        else:
            balls.remove(self)

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        check_hit = False
        global bullet

        distance = ((self.x - obj.x)**2 + (self.y - obj.y)**2)**0.5

        if distance <= self.r + obj.r:
            check_hit = True

        return check_hit


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        x = 20
        y = 450
        a = self.f2_power
        b = 5
        #Рисую)
        pygame.draw.polygon(self.screen, self.color, [(x, y), (x + a * math.cos(self.an) - b * math.cos(self.an), y + 2*b*math.sin(self.an)) ,
           (x + a * math.cos(self.an), y + b * math.sin(self.an)),
                                                      (x - b * math.sin(self.an), y + b * math.cos(self.an))])

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self, screen):
        self.points = 0
        self.x = 0
        self.y = 0
        self.r = 0
        self.color = None
        self.live = 0
        self.screen = screen
        self.vector = None
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = 600 + random() * 180
        self.y = 300 + random() * 250
        self.r = 2 + random() * 48
        self.color = RED
        self.live = 1
        self.vector = [randint(-1, 1), randint(-1, 1)]

    def move(self):
        self.x += self.vector[0]
        self.y += self.vector[1]

        if self.x + self.r >= 800 or self.x - self.r <= 0:
            self.vector[0] *= -1
        if self.y + self.r >= 600 or self.y - self.r <= 0:
            self.vector[1] *= -1

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
target1 = Target(screen)
target2 = Target(screen)
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    target1.draw()
    target2.draw()
    for b in balls:
        b.draw()

    font_name = pygame.font.match_font('arial')#Задаём шрифт текста для вывода очков игрока
    font = pygame.font.Font(font_name, 10)
    text_surface = font.render(str(target1.points + target2.points), True, (0, 0, 0))#Что пишем и каким цветом(Белый)
    text_rect = text_surface.get_rect()#прямоугольник для текста
    text_rect.midtop = (400, 0)#Располагаем его
    screen.blit(text_surface, text_rect)#Рисуем его

    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    target1.move()
    target2.move()

    for b in balls:
        b.move()
        if b.hittest(target1) and target1.live:
            target1.live = 0
            target1.hit()
            target1.new_target()

        if b.hittest(target2) and target2.live:
            target2.live = 0
            target2.hit()
            target2.new_target()
    gun.power_up()

pygame.quit()
