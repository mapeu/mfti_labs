from ball import *
from rect import *
from random import randint

score = 0 #Тут ведём счет игрока

def get_score():#Необходима для получения счёта игрока в другом модуле
    return score

def create_balls(n:int):#Создаёт шары
    """n - size of list, returns list of balls"""
    list_balls = [Ball(randint(1, 1000), randint(1, 1000), randint(1, 100)) for i in range(n)]
    return list_balls

def create_rects(n:int):# Создаёт квадраты
    ''''n - size of list, returns list of rectangles'''
    list_rects = [Rect(randint(1, 1000), randint(1, 1000), randint(1, 100)) for i in range(n)]
    return list_rects

def hit_obj(event: pygame.MOUSEBUTTONDOWN, list_balls, list_rects): #Обработчик события
    (x, y) = event.pos#Куда тыкнули
    balls_hitted = []#Лист, чтобы хварнить все шары на котоыре кликнули за раз
    rects_hitted = []#Лист, чтобы хранить все квадратики на которые кликнули за раз
    global score # Необходимо, чтобы изменять счёт

    for ball in list_balls:#Проверяем попал ли клик на шарик
        distance = ((x - ball.x) ** 2 + (y - ball.y) ** 2) ** 0.5
        if distance <= ball.r:#Если попал - добавляем в лист
            balls_hitted.append(ball)

    for rect in list_rects:#Проверяем попал ли клик на квадрат
         if ( x >= rect.x  and x <= rect.x + rect.width and y >= rect.y and y <= rect.y + rect.width):
             rects_hitted.append(rect)

    for ball in balls_hitted:#Если попали на шар, то его удаляем с рисунки и рисуем нвоый
        list_balls.remove(ball)
        list_balls.append(Ball(randint(1, 1000), randint(1, 1000), randint(1, 100)))

    for rect in rects_hitted:#Если попали на квадрат, то удаляем его и рисуем новый
        list_rects.remove(rect)
        list_rects.append(Rect(randint(1, 1000), randint(1, 1000), randint(1, 100)))

    #Меняем очки игрока

    if balls_hitted:
        score += len(balls_hitted)

    if rects_hitted:
        score += len(rects_hitted) * 2


font_name = pygame.font.match_font('arial')#Задаём шрифт текста для вывода очков игрока


def draw_text(x, y, screen, size):#функция зарсиовки очков игрока
    """"
    :param x: x координата очков
    :param y: y координата очков
    :param screen: где рисуем
    :param size: размер теста
    """
    font = pygame.font.Font(font_name, size) # Сам текст
    text_surface = font.render(str(score), True, (255, 255, 255))#Что пишем и каким цветом(Белый)
    text_rect = text_surface.get_rect()#прямоугольник для текста
    text_rect.midtop = (x, y)#Располагаем его
    screen.blit(text_surface, text_rect)#Рисуем его

def draw_leaderboard(x, y, screen, size, users):
    """
    :param x: x координата очков
    :param y: y координата очков
    :param screen: где рисуем
    :param size: размер теста
    :param users: Список пользователей
    """
    cur_y = y#Чтобы рисовать их в столбец

    for user, scor in users.items():#каждого юзера по одному добавляем
        u = user + ": " + scor
        font = pygame.font.Font(font_name, size) # Сам текст
        text_surface = font.render(u, True, (255, 255, 255))#Что пишем и каким цветом(Белый)
        text_rect = text_surface.get_rect()#прямоугольник для текста
        text_rect.midtop = (x, cur_y)#Располагаем его
        screen.blit(text_surface, text_rect)#Рисуем его
        cur_y += 20#Для следующего юзера

def save_users(users, username):
    text = ''

    for user, scor in users.items():
        text += str(user) + ":" + str(scor) + "\n"

    file = open("leaderboard.txt", "w")
    file.write(text)
    file.close()

