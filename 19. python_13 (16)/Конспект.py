#КОНСПЕКТОС



import os
path = os.getcwd()
path1 = "/Users/margaritaberseneva/Desktop/12345/CW13_1.py"
print(os.name) # имя системы
print(os.getlogin()) #логин
print(os.getcwd()) #показывает путь к текущей папке
print(os.path.abspath('.')) #показывает абсолютный путь к текущей папке
print(os.listdir(path=".")) #показывает файлы в текущей папке | path="." -- текущая папка
print(os.path.dirname(path)) #показывает имя директории
print(os.path.exists(path)) #говорит существует ли папка с путем path
print(os.path.isfile(path1)) # говорит является ли путь файлом
print(os.path.isdir(path)) # - является ли путь директорией
print(os.path.samefile(path1, path)) # - указывают ли path и path1 на один и тот же файл или директорию
print(os.path.split(path)) # - разбивает путь на кортеж (голова, хвост), где хвост - последний компонент пути, а голова - всё остальное. Хвост никогда не начинается со слеша (если путь заканчивается слешем, то хвост пустой). Если слешей в пути нет, то пустой будет голова.
print(os.path.join('folder', 'file.txt')) # напишет путь к файлу через папку как принято в системе

# os.listdir()


##print(os.listdir(path))
##for f in os.listdir(path):
##    print('file: ', f) # -- красиво печатаем все внутренности папки


##print(os.listdir(folder))
##for f in os.listdir(folder):
##     with open(os.path.join(folder, f)) as text:
##        print('file: ', f, '   text: ', text.read())  -- что-то не работает


# os.mkdir()

#os.mkdir('new_folder')  # добавил папку new_folder (если такая есть, то ошибки не миновать)

print(os.path.exists('new_folder')) # - проверяем существует ли она 

if not os.path.exists('new_folder2'):
    os.mkdir('new_folder2') # - если папки не существует, то можно и сразу создать
    print(os.listdir(path="."))


#path = 'a/long/long/long/path'
#os.makedirs(path) # - добавляет плеяду папок в текущую


# shutil.copy(), shutil.move(), os.rename()

import shutil
if not os.path.exists('new_texts'):
    os.mkdir('new_texts')
for f in os.listdir('7'):
    shutil.copy(os.path.join('7', f), 'new_texts') # -- скопировали внутренности из папки 7 в новосозданную new_texts


for f in os.listdir('1'):
    shutil.move(os.path.join('1', f), '7') # -- переместили внутренности из папки 1 в уже имеющуюся папку 7


for f in os.listdir('6'):
    os.rename(os.path.join('6', f), os.path.join('6', 'my' + f))
os.listdir('6') # -- переименовали внутренности папке 6 по образцу my+X.txt


# os.path.isdir() и os.path.isfile()

# 5 - это папка?
print(os.path.isdir('5'))

# А 6 - то файл?
print(os.path.isfile('6'))
