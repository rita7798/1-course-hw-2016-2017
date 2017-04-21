#coding = utf-8

import os
import re


files = []
list_of_names = []
names = 0
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
            if len(name) >= 1: # избавляюсь от файла .DS_Store
                if name not in list_of_names:
                    list_of_names.append(name)
                    names += 1

print("В ", len(roots), " папках встретилось ", names, " различных названий файлов")


