#coding = utf-8


import os
import re

folders = 0
folders_names = []
path = os.getcwd()
folderslist = [folder for folder in os.listdir() if os.path.isdir(folder)]

printing_names = []
true_names = [name for name in folderslist if re.search('[a-zA-Z]', name) != None and re.search('[а-яёА-ЯЁ]', name) != None]
for i in range(len(true_names)):
    folders += 1
    if true_names[i] not in printing_names:
        printing_names.append(true_names[i])

print("Найдено ", folders, " папок(ки): ")
for i in range(len(printing_names)):
    print(printing_names[i])
