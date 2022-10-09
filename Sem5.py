from itertools import count
from math import factorial
from functools import reduce
import os
from random import randint
# lst = [3, 7, 0]
# print(lst[3]) # обращение к несуществующему элементу

# numb = 54/0 # деление на 0!

# try:
#     numb = 54/0
# except ZeroDivisionError: # либо except:, либо except Exception
#     print('На 0 делить нельзя!')
# else: 
#     print(f'Все хорошо, результат {numb}')
# finally:
#     print('Программа завершена')
    
# 1. Создать класс исключения
# 2. Сгенерировать исключение в нужной точке программы
# 3. Отловить и обработать

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt
# inp_data = input('Введите положительное число: ')

# try:
#     inp_data = int(inp_data)
#     if inp_data < 0:
#         raise OwnError('Вы ввели отрецательное число!')
# except OwnError as err:
#     print(err)
# else:
#     print(f'Все хорошо, ваше число {inp_data}.')
    
    
lst = [322, 1, 65, 981, 0, 23, 123, 7, 1, 78, 104]
lst = [lst[i] for i in range(1, len(lst)) if lst[i] > lst[i - 1]]

# print(lst)   

lst = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]

# print(lst)

lst = [322, 1, 65, 981, 0, 23, 123, 7, 1, 65, 78, 104]
lst = [el for el in lst if lst.count(el) == 1]
# print(lst)

# def fact(n):
#     factorial = 1
#     for x in count(1):
#         if x > n: 
#             break
#         factorial = factorial * x
#         yield factorial

# n = int(input('Введите число: '))
# i = 0
# for el in fact(n):
#     i += 1
    # print(f'!{i} = {el}')



# lst = [x for x in range(100, 1001, 2)]
# res = reduce(lambda el1, el2: el1 * el2, lst)
# print(res)

# def out_of_txt(tex_incl, txt):
def clr_scrn():
    os.system('cls' if os == 'nt' else 'clear')    

def zadacha_1(): # Напишите программу, удаляющую из текста все слова, содержащие вводимые пользователем символы.
    clr_scrn()
    txt = 'Изучение полиномиальных уравнений и их решений долгое время составляло едва ли не главный объект «классической алгебры». С изучением многочленов связан целый ряд преобразований в математике: введение в рассмотрение нуля, отрицательных, а затем и комплексных чисел, а также появление теории групп как раздела математики и выделение классов специальных функций в математическом анализе.'
    print(f'Имеем исходный текст:\n"{txt}"\n')
    txt_excl = input('Введите сочетание букв, слова, содержащие которое хотите удалить из текста:\n')
    print()
    txt = txt.split()
    txt1 = [el for el in txt if txt_excl not in el]
    txt1 = ' '.join(txt1)
    print(f'Измененный текст:\n"{txt1}"')
    
def zadacha_2(): # Создайте программу для игры с конфетами человек против человека. Условие задачи: 
    # На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется 
    # жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются 
    # сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у 
    # своего конкурента?
    clr_scrn()
    left = 2021
    user_1_num = 0
    user_2_num = 0
    last_left = 28
    print('ИГРА\nИграют два игрока делая ход друг после друга. Первый ход определяется\nжеребьёвкой. За один ход можно забрать не более чем 28 конфет.\nВсе конфеты оппонента достаются сделавшему последний ход.\n')
    user = randint(1, 3)
    while True:
        try:
            robo = int(input('Хотите сыграть с бездушным Роботом - введите "1", с живым человеком - "0"!\n:'))
        except Exception:
            clr_scrn()
            print('Вы ошиблись с вводом! Попробуйте снова!')
        else:
            if robo < 0 or robo > 1: 
                clr_scrn()
                print('Повторите ввод!')
            else: break
    print(f'\nВ банке конфет: {left} шт!\n')
    input('Нажмите ENTER, чтобы начать игру!')
    while left > 0:
        if user == 1: 
            while True:
                if robo == 0: clr_scrn()
                print(f'Осталось конфет: {left}шт.')
                try:
                    user_1_turn = int(input(f'Игрок 1, возьмите от 1 до {last_left} конфет!\n:'))
                except Exception:
                    clr_scrn()
                    print('Повторите ввод!')
                else:
                    if user_1_turn < 1 or user_1_turn > last_left:
                        clr_scrn()
                        print('Вы ввели неверное число конфет!')
                    else: 
                        left -= user_1_turn
                        user = 2
                        user_1_num += user_1_turn
                        if left < last_left: last_left = left
                        break     
        else:
            if robo == 0:
                while True:
                    clr_scrn()
                    print(f'Осталось конфет: {left}шт.')
                    try:
                        user_2_turn = int(input(f'Игрок 2, возьмите от 1 до {last_left} конфет!\n:'))
                    except Exception:
                        print('Повторите ввод!')
                    else:
                        if user_2_turn < 1 or user_2_turn > last_left:
                            print('Вы ввели неверное число конфет!')
                        else: 
                            left -= user_2_turn
                            user = 1
                            user_2_num += user_2_turn
                            if left < last_left: last_left = left
                            break  
            else:
                clr_scrn()
                print(f'Осталось конфет: {left}шт.')
                user_2_turn = randint(1, last_left + 1)
                print(f'Робот ввел число {user_2_turn}\n')
                left -= user_2_turn
                user = 1
                user_2_num += user_2_turn
                if left < last_left: last_left = left
    if user == 1:
        if robo == 1: winner = 'Робот'
        else: winner = 'Игрок 2'
        win_numb = user_2_num
    else: 
        winner = 'Игрок 1'
        win_numb = user_1_num
    print(f'Победил {winner}, забрав {win_numb} конфет!')
    
# zadacha_1()
zadacha_2()

