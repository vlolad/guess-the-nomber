import time
import random

# Простейшая игра, в которой программа загадывает число, а игрок отгадывает
# Некоторые куски кода закомментированы со времён отладки приложения

# (c) vlolad (2022)
# Простите, что вы это видите

print('Игра: Угадай загаданное число!')
time.sleep(1)

# Две функции для дебага
# debugs - убирает перерывы в отображении команд (для юзер френдли экспириенса)
# debugv - чит, чтобы игра сразу говорила, какое число загадала

def debugs(i):
    sus = False
    if not sus:
        time.sleep(i)

def debugv(num):
    sus = False
    if sus:
        print(num)

while True:
    print("Я загадываю числа от 1 до бесконечности.")

    # Юзверь задает верхнюю планку генерации числа
    def check_int():
        while True:
            print('Выбери, до какого числа (включительно) я могу загадывать:')
            max_num = input()
            try:
                int(max_num)
                return max_num
            except ValueError:
                print('Это не число!')

    max_num = check_int()

    # Генерация числа
    print('Понял!')
    debugs(1)
    print('Загадываю число...')
    secret = random.randint(1, int(max_num))
    debugs(1)
    print('Загадал число от 1 до ' + str(max_num) + '!')
    # Чит
    debugv(secret)
    # Переменные, сохраняющие угадывание и количество попыток
    guess = 0
    guess_count = 1
    # Метод для считывания предположения пользователя
    def guessing(guess):
        while True:
            print('Введи число:')
            guess = input()
        # guess = int(guess)
            try:
                int(guess)
                if guess == 1488:
                    print("Фашист! Выключаюсь")
                    time.sleep(1)
                    quit()
                return int(guess)
            except ValueError:
                print('Это не число!')
    
    # База игры, игрок гадает пока не отгадает
    while guess != secret:
        # print('random:', secret)
        guess = guessing(guess)
        # print('user input:', guess, type(guess))
        
        if guess != secret:
            print('Неа, не угадал')
            guess_count += 1
            print ("Попытка №", guess_count)
            
            if guess > secret:
                print('Я загадал число меньше')
                
            if guess < secret:
                print('Я загадал число больше')

    # Метод, который задает правильное отображение количества попыток по итогам игры
    def count_right(guess_count):
        tgc = ''
        a = 0
        b = 0
        res_new = 0
        i = guess_count
        # Если кол-во попыток больше 20, то нужно считать сложнее
        if i > 20:
            res = []
            while i > 0:
                res.append(i % 10)
                i //= 10
            #print(res)
            a = res[0]
            b = res[1]
            res_new = str(b) + str(a) 
            i = int(res_new)
            #print (i)
        # print(f"i: {i} || a:{a} || b:{b} || res_new:{res_new}")
        if (i == 1) or (a == 1):
            tgc = 'попытку!'
        elif (i <= 4) or ((a <= 4) and (a != 0)):
            tgc = 'попытки!'
        elif (i > 4) or (a > 4):
            tgc = 'попыток!'
        
        return tgc

    # Вывод результатов игры
    print('Ты угадал! Я загадал число', secret)
    debugs(1)
    print('Ты угадал всего за', guess_count, count_right(guess_count))
    debugs(2)
    def endgame():
        choice = input()
        try:
            int(choice)
            return int(choice)
        except ValueError:
            print('Это не число!')

    # Итоговое меню на выходе, можно перезапустить игру
    while True:
        print ('Сыграем ещё? (1 - Да, 0 - Нет, выйти)')
        choice = endgame()
        # print(f'choice: {choice}')
        if choice == 0:
            print('Завершаю...')
            debugs(5)
            break
        elif choice == 1:
            print('Ну че, народ...')
            debugs(2)
            break
        else:
            print('Не понял')
    if choice == 0:
        break

# ⠄⠄⠄⢰⣧⣼⣯⠄⣸⣠⣶⣶⣦⣾⠄⠄⠄⠄⡀⠄⢀⣿⣿⠄⠄⠄⢸⡇⠄⠄
#  ⠄⠄⠄⣾⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄⠸⢀⣿⠄
# ⠄⠄⢀⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿⣿⠄
# ⠄⠄⢸⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⠄
# ⠄⢀⢸⣿⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠉⠋⣰
# ⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠃⠄⠄
# ⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁⠄⠄⠄
# ⠄⠄⠄⠄⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁⠄⠄⠄⠄⠄
# ⠄⠄⠄⠄⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁⠄⠄⠄⠄⠄⢀⣠⣴
# ⣿⣿⣿⣶⣶⣮⣥⣒⠲⢮⣝⡿⣿⣿⡆⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⣠⣴⣿⣿⣿