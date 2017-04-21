#coding = utf-8

import os
import re


list_of_files = {}
for root, dirs, files in os.walk('.'):
    list_of_files[root] = len(files)

max_value = max(list_of_files.values()) 
t = "В папке по адресу "+(os.getcwd())+" встретилось максимум файлов -- {} штук(и)"
t1 = "В папке по адресу "+(os.getcwd())+"{} встретилось максимум файлов -- {} штук(и)"
for key in list_of_files:
    if key == ".":
        if list_of_files[key] == max_value:
            print(t.format(list_of_files[key]))
    else:
        if list_of_files[key] == max_value:
            print(t1.format(key, list_of_files[key]))
