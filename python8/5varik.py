#coding = utf-8
#ДОПОЛНИТЕЛЬНО, кроме основного задания
#3 уровня сложности
#пользователь сам задает количество попыток 

def easy():
    d = {}
    with open ("words1.csv", 'r', encoding='utf-8') as f:
        for word in f.readlines():
            word = word.replace('\n', '').split(",")
            d[word[0]] = word[1]
    return d

def advanced():
    d = {}
    with open ("words2.csv", 'r', encoding='utf-8') as f:
        for word in f.readlines():
            word = word.replace('\n', '').split(",")
            d[word[0]] = word[1]
    return d

def hard():
    d = {}
    with open ("words3.csv", 'r', encoding='utf-8') as f:
        for word in f.readlines():
            word = word.replace('\n', '').split(",")
            d[word[0]] = word[1]
    return d

def playing(d):
    q = len(d)
    for key, val in d.items():
        print("Введите число от 1 до 10")
        l = int(input())
        print("Итак, у Вас", l, "попыток(и)")
        print("Подсказка: ", key, "...")
        print("Можете начинать отгадывать!")
        s = str(input())
        i = 1
        while s != val:
            print("Ответ неверный!")
            if l == i:
                print("Вы не отгадали!")
                print("Загаданное слово:", val)
                print("Словосочетание полностью:", key, val)
                print("----------------------------")
                print("Хотите еще?")
                a = str(input())
                if a == "нет" or a == "Нет":
                    print("Спасибо за игру!")
                    return a
            if s != val:
                print("Подсказка: ", key, "...")
                print("Вы сделали", i, "попыток(и)")
                s = str(input())
                i += 1
        if s == val:
            print("Ответ правильный!Вы молодец!")
            q -= 1
            print("В этом разделе осталось еще ", q, "загадок(и)")
            if q == 0:
                print("Загадки закончились! Спасибо за такую увлеченность!")
                print("Хотите поменять уровень и начать еще раз?")
                a = str(input())
                if a == "нет" or a == "Нет":
                    print("Пока!")
                    break
                elif a == "да" or a == "Да":
                    choosing(a)
            else:
                print("Хотите еще?")
                d = str(input())
                if d == "нет" or d == "Нет":
                    print("Спасибо за игру!")
                    break

def welcoming():
    print("Здравствуйте! Вас приветствует игра \"Отгадай слово по подсказке\"!")
    print("Хотите поиграть?")
    a = str(input())
    if a == "":
        print("Введите ваш ответ еще раз")
        a = str(input())
        if a == "":
            print("Пока!")
        elif a == "да" or a == "Да":
            print("Подумайте над уровнем сложности")
        elif a == "нет" or a == "Нет":
            print("До свидания!")
    elif a == "нет" or a == "Нет":
        print("До свиданья!")
    elif a == "да" or a == "Да":
            print("Подумайте над уровнем сложности")
    else:
        print("Я не понимаю Вас...")
        print("Попробуйте еще раз ответить на этот вопрос да или нет")
        print("Перезагружаюсь...")
        print("__________________________")
        welcoming()
    return a

def choosing(a):
    if a == "да" or a == "Да" or a == "lf":
        print("Выберете уровень сложности: (легкий/средний/тяжелый)")
        b = str(input())
        if b == "":
            print("Советую начать  с легкого")
            print("Согласны?")
            c = str(input())
            if c == "да" or c == "Да":
                print("Загружаю...")
                print("Приятной игры!")
                print("__________________________")
                playing(easy())
            elif c == "нет" or c == "Нет":
                print("До свидания!")
        elif b == "легкий":
            print("Загружаю...")
            print("Приятной игры!")
            print("__________________________")
            playing(easy())
        elif b == "средний":
            print("Загружаю...")
            print("Приятной игры!")
            print("__________________________")
            playing(advanced())
        elif b == "тяжелый":
            print("Загружаю...")
            print("Приятной игры!")
            print("__________________________")
            playing(hard())

(choosing(welcoming()))
