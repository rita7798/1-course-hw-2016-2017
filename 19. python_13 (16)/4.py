#coding = utf-8


import os
import re

files = 0
files_names = []
path = os.getcwd()
fileslist = [file for file in os.listdir() if os.path.isfile(file)]

names = []
for file in fileslist:
    name = file.rsplit('.', maxsplit=1)[0]
    names.append(name)

printing_names = []
true_names = [name for name in names if re.search('[a-zA-Z]', name) != None]
for i in range(len(true_names)):
    files += 1
    if true_names[i] not in printing_names:
        printing_names.append(true_names[i])

print("Найдено ", files, " файлов(ла): ")
for i in range(len(printing_names)):
    print(printing_names[i])
    

        
    



