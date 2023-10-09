import math
from random import choice
from random import random
from random import randint

import pygame#Временно не работает нормально баллистика, плохая логика столкновения шарика и квадратика, нельзя стрелять
#танками друг в друга

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

class Projectile:
    def __init__(self, screen: pygame.Surface, x = 40, y = 450 ):
        """

        :param screen: где рисуем
        :param x: начальная x координата снаряда
        :param y: начальная y координата снаряда
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.live = 30
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)


class Ball(Projectile):
    def __init__(self, screen: pygame.Surface, x = 40, y = 450):
        super().__init__(screen, x, y)
        self.r = 10

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.live -= 1#Укорачиваем время жизни объекта

        self.x += self.vx
        self.y -= self.vy - 10 * (50 - self.live)

        #Отрабокта отскакивания от стен. FIX ME
        if self.x + self.r >= 800 or self.x - self.r <= 0:
            self.vx *= -1

        if self.y + self.r >= 600:
            self.vy = -self.vy + 10 * (50 - self.live)

    def draw(self):# Рисуем шарик, если он уже долго живет - удаляем
        global projectiles

        if self.live > 0:
            pygame.draw.circle(
                self.screen,
                self.color,
                (self.x, self.y),
                self.r
            )
        else:
            projectiles.remove(self)

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        check_hit = False

        distance = ((self.x - obj.x)**2 + (self.y - obj.y)**2)**0.5

        if obj.type == "Ball":
            if distance <= obj.r + self.r:
                check_hit = True
        elif obj.type == "Rectangle":#FIX ME, кривая логика
            if (self.x < obj.x and self.x + self.r >= obj.x) or (self.y < obj.y and self.y + self.r >= obj.y) or (
                    self.y > obj.y + obj.r and self.y - self.r <= obj.y + obj.r) or (
                self.x > obj.x + obj.r and self.x - self.r <= obj.x + obj.r):
                check_hit = True


        return check_hit

class Rectangle(Projectile):
    def __init__(self, screen: pygame.Surface, x = 40, y = 450):
        super().__init__(screen, x, y)
        self.width = 10

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение квадрата за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на квадрат,
        и стен по краям окна (размер окна 800х600).
        """
        self.live -= 1#Укорачиваем время жизни объекта

        self.x += self.vx
        self.y -= self.vy - 10 * (50 - self.live)

        #Отрабокта отскакивания от стен
        if self.x + self.width >= 800 or self.x <= 0:
            self.vx *= -1

        if self.y + self.width >= 600:
            self.y += self.vy - 10 * (50 - self.live) - self.live

    def draw(self):#Рисуем квадратик
        global projectiles

        if self.live > 0:
            pygame.draw.rect(
                self.screen,
                self.color,
                (self.x, self.y,
                self.width, self.width)
            )
        else:
            projectiles.remove(self)



    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        check_hit = False
        if obj.type == "Ball":#кривая логика
             if (self.x < obj.x and self.x + self.width >= obj.x - obj.r) or (
                 self.x > obj.x and self.x <= obj.x + obj.r) or (
                 self.y < obj.y and self.y + self.width >= obj.y - obj.r) or(
                 self.y > obj.y and self.y <= obj.y + obj.r):
                 check_hit = True
        elif obj.type == "Rectangle":#Кривая логика
               if (self.x < obj.x and self.x + self.width >= obj.x) or (self.y < obj.y and self.y + self.width >= obj.y) or (
                       self.x > obj.x and self.x <= obj.x + obj.r) or self.y <= obj.y + obj.r:
                   check_hit = True

        return check_hit

types = ["Ball", "Rectangle"]

class Gun:
    def __init__(self, screen, x = 20, y = 500):
        self.x = x
        self.y = y
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.mouse = None
        self.x_toreturn = x

    def fire2_start(self, event):#Начинаем выстрел
        self.f2_on = 1

    def fire2_end(self, event):#Выстреливаем чем-либо(либо квадратом, либо мячиком)
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global projectiles, bullet, types
        type = choice(types)

        if type == "Ball":
            bullet += 1
            new_ball = Ball(self.screen, self.x + 5 * self.f2_power, self.y)
            new_ball.r += 5
            self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
            new_ball.vx = self.f2_power * math.cos(self.an)
            new_ball.vy = - self.f2_power * math.sin(self.an)
            projectiles.append(new_ball)
        elif type == "Rectangle":
            bullet += 1
            new_rect = Rectangle(self.screen, self.x + 5 * self.f2_power, self.y)
            new_rect.width += 5
            self.an = math.atan2((event.pos[1]-new_rect.y), (event.pos[0]-new_rect.x))
            new_rect.vx = self.f2_power * math.cos(self.an)
            new_rect.vy = - self.f2_power * math.sin(self.an)
            projectiles.append(new_rect)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-self.x))
            self.mouse = event.pos

    def move(self, event):#Двигаем пушку по направлению мыши
        if event.pos[0] > self.x:
            self.x += 1
        elif event.pos[0] < self.x:
            self.x -= 1

    def hittest(self, obj):#Проврка на попадания на снаряд
        if self.y < obj.y + obj.r:
            self.x = self.x_toreturn


    def draw(self):#Рисуем танк
        tank = pygame.image.load('pngwing.com.bmp')
        #tank = pygame.transform.rotate(tank, self.an * 180 / math.pi + 90)
        tank = pygame.transform.scale(tank, (5 * self.f2_power, 5 * self.f2_power))
        tank = pygame.transform.rotozoom(tank, math.degrees(-self.an), 1)
        tank_rect = tank.get_rect(topright = (self.x + 150, self.y - 100))
        self.screen.blit(tank, tank_rect)


    def power_up(self):#Заряжаем пучу
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1


class Bomb(Projectile):#Сбрасываем бомбы
    def __init__(self, screen: pygame.surface, x, y):
        super().__init__(screen, x, y)
        self.y_cur = y
        self.r = 10

    def move(self):
        self.y_cur += 1

        if self.y_cur >= 600:
            self.y_cur = self.y


    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y_cur), self.r)


class Target:
    def __init__(self, screen):
        self.type = None
        self.points = 0
        self.x = 0
        self.y = 0
        self.r = 0
        self.color = None
        self.live = 0
        self.screen = screen
        self.vector = None
        self.bomb = None
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        global types
        self.type = choice(types)
        self.x = 600 + random() * 180
        self.y = 300 + random() * 250
        self.r = 2 + random() * 48
        self.color = RED
        self.live = 1
        self.vector = [randint(-1, 1), randint(-1, 1)]
        self.bomb = Bomb(self.screen, self.x, self.y)

    def move(self):#Двигаем цели в разные стороны, с помощью случайного вектора
        self.x += self.vector[0]
        self.y += self.vector[1]

        if self.x + self.r >= 800 or self.x - self.r <= 0:
            self.vector[0] *= -1
        if self.y + self.r >= 600 or self.y - self.r <= 0:
            self.vector[1] *= -1

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):#Рисуем цели
        if self.type == "Ball":
            pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)
        else:
            pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.r, self.r))




#Всё задаём
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
projectiles = []

clock = pygame.time.Clock()
gun1 = Gun(screen)
gun2 = Gun(screen, 400)
target1 = Target(screen)
target2 = Target(screen)
finished = False

while not finished:#Основной цикл
    screen.fill(WHITE)
    gun1.draw()
    gun2.draw()

    target1.draw()
    target1.bomb.move()
    target1.bomb.draw()
    gun1.hittest(target1.bomb)
    gun2.hittest(target1.bomb)

    target2.draw()
    target1.bomb.move()
    target2.bomb.draw()
    gun1.hittest(target2.bomb)
    gun2.hittest(target2.bomb)

    for b in projectiles:
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
            gun1.fire2_start(event)
            gun2.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun1.fire2_end(event)
            gun2.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun1.targetting(event)
            gun1.move(event)
            gun2.targetting(event)
            gun2.move(event)

    target1.move()
    target2.move()
    for b in projectiles:
        b.move()
        if b.hittest(target1) and target1.live:#Отрабатываем попадание в цель
            target1.live = 0
            target1.hit()
            target1.new_target()

        if b.hittest(target2) and target2.live:
            target2.live = 0
            target2.hit()
            target2.new_target()
    gun1.power_up()
    gun2.power_up()

pygame.quit()
