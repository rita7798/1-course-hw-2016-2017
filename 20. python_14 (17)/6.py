#coding = utf-8

import os
import re


files = []
t = (os.getcwd())+"{}"
roots = [root[1:] for root, dirs, files in os.walk('.')]
for root in roots:
    if root != "":
        files.append(os.listdir(path = t.format(root)))
    elif root == "":
        files.append(os.listdir(path = "."))   
list_of_folders = {}
for i in range(len(files)):
    list_of_ext = {}
    for j in range(len(files[i])):
        if re.search('[.]', files[i][j]) != None: #рассматриваем только файлы с расширениями
            name = files[i][j].rsplit('.', maxsplit=1)[0]
            ext = files[i][j].rsplit('.', maxsplit=1)[1]
            if len(name) >= 1: # избавляюсь от файла .DS_Store
                if ext not in list_of_ext:
                    list_of_ext[ext] = 1
                else:
                    list_of_ext[ext] += 1
    for key in list_of_ext:
        if list_of_ext[key] >= 1:
            extension = key
            if extension not in list_of_folders:
                list_of_folders[extension] = 1
            else:
                list_of_folders[extension] += 1  
t1 = "Расширение \".{}\" встретилось в {} папках(е)"
for key, value in list_of_folders.items():
    print(t1.format(key, value))


