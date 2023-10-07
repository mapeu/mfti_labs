from fucntions import *
import csv

username = input("Please say your nickname > ")#Иницилизируем пользователя

users = {}#Все игроки


with open("leaderboard.txt", "r") as file:#Выгужаем игроков
    # Создаем объект reader, указываем символ-разделитель ":"
    file_reader = csv.reader(file, delimiter = ":")
    # Считывание данных из CSV файла
    for row in file_reader:
        users[row[0]] = row[1]

pygame.init()# Запустили pygame

FPS = 60#Задали частоту кадров
screen = pygame.display.set_mode((1000, 1000))#Создали экран

pygame.display.update()
clock = pygame.time.Clock()#Считаем время
finished = False
list_balls = create_balls(10)#Создаём шарики, которые будут летать
list_rectangles = create_rects(10)#Создаём квадратики, которые будут летать


while not finished:#Основной цикл, чтобы можно было играть
    clock.tick(FPS)#Задаём частоту кадров в игре
    for event in pygame.event.get():#Ловим события
        if event.type == pygame.QUIT:#Выход из игры
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:#Ловим нажатие на клавишу и обрабатываем событие
            hit_obj(event, list_balls, list_rectangles)
    for ball in list_balls:#Рисуем шарики, их движение и отталкивание от стен
        ball.draw_ball(screen)
        ball.check_wall()
        ball.move()

    for rect in list_rectangles:#То же самое с квадратиками
        rect.draw_rect(screen)
        rect.check_wall()
        rect.move()

    draw_text(500, 10, screen, 18)#Рисуем таблицу счёта
    draw_leaderboard(800, 10, screen, 18, users)#Рисуем leaderboard
    pygame.display.update()
    screen.fill((0, 0, 0))#Обрисовавыем всё и при каждой итерации заливаем всё черным.

pygame.quit()#Завершаю всё

users[username] = get_score()#Добавляем нового юзера
users = dict(sorted(users.items(), key = lambda item: int(item[1]), reverse = True))#Сортирум юзеров
save_users(users, username)#Сохраняем их






