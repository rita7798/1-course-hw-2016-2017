#coding = utf-8


import os
import re

def choosing():
    fileslist = [file for file in os.listdir() if os.path.isfile(file)]
    names = []
    for file in fileslist:
        name = file.rsplit('.', maxsplit=1)[0]
        names.append(name)
    return names


def printing_out(names):
    files = 0
    printing_names = []
    true_names = [name for name in names if re.search('[.,!?:;)(-]', name) != None]
    for i in range(len(true_names)):
        files += 1
        if true_names[i] not in printing_names:
            printing_names.append(true_names[i])
    print("Найдено ", files, " файлов(ла): ")
    for i in range(len(printing_names)):
        print(printing_names[i])

def main():
    names = choosing()
    printing_out(names)


main()

