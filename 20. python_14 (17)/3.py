#coding = utf-8

import os


def finding_and_counting(list_of_ext):
    for root, dirs, files in os.walk('.'):
        for f in files:
            name = f.rsplit('.', maxsplit=1)[0]
            ext = f.rsplit('.', maxsplit=1)[1]
            if len(name) >= 1: # избавляюсь от файла .DS_Store
                if ext not in list_of_ext:
                    list_of_ext[ext] = 1
                else:
                    list_of_ext[ext] += 1
    return (list_of_ext)


def printing_out(list_of_ext):
    for key, value in list_of_ext.items():
        if value >= 3: #встретилось более 3 раз - часто
            t = "Расширение \".{}\" встретилось {} раз(а)"
            print(t.format(key, value))
    value = max(list_of_ext.values())        
    for key in list_of_ext:
        if list_of_ext[key] == value:
            t1 = "Самое частое расширение - \".{}\""
            print(t1.format(key))


def main():
    list_of_ext = {}
    finding_and_counting(list_of_ext)
    printing_out(list_of_ext)


main()
