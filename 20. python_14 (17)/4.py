#coding = utf-8

import os


def finding_and_counting(list_of_fletter):
    for root, dirs, files in os.walk('.'):
        for d in dirs:
            if d[0].lower() not in list_of_fletter:
                list_of_fletter[d[0].lower()] = 1
            else:
                list_of_fletter[d[0].lower()] += 1
    return (list_of_fletter)


def printing_out(list_of_fletter):
    for key, value in list_of_fletter.items():
        if value >= 3: #встретилось более 3 раз - часто
            t = "Первая буква \"{}\" встретилась {} раз(а)"
            print(t.format(key, value))
    value = max(list_of_fletter.values())        
    for key in list_of_fletter:
        if list_of_fletter[key] == value:
            t1 = "Самое частая буква - \"{}\""
            print(t1.format(key))


def main():
    list_of_fletter = {}
    finding_and_counting(list_of_fletter)
    printing_out(list_of_fletter)


main()
