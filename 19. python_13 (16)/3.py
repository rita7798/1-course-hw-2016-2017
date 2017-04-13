#coding = utf-8


import os
import shutil
import re


folders = 0
folders_names = []

path = os.getcwd()
folderslist = [folder for folder in os.listdir() if os.path.isdir(folder)]

for i in range(len(folderslist)):
    folder = "([А-ЯЕа-яе]*\s*[А-ЯЕа-яе]*\s*[А-ЯЕа-яе]*)" #длина названия папки от 1 до 3 слов.
    name = re.findall(folder, folderslist[i])
    for j in range(len(folderslist)):
        for i in range(len(name)):
            if name[i] != " " and name[i] == folderslist[j]:
                folders += 1
                if name[i] not in folders_names:
                    folders_names.append(name[i])

print("Найдено ", folders, " папок(ки) с названиями только из кириллических символов в директории", path)

print("А вот сами папки: ")
for i in range(len(folders_names)):
    print(folders_names[i])

