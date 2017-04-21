#КОНСПЕКТОС

import os

print(os.listdir('.')) # - выводит список файлов в данной папке
print("----------")
print(os.listdir('..')) # - выводит список файлов в папке выше
print("----------")
print(os.walk('.')) # - гуляние по папкам
print("----------")
for d in os.walk('.'): # -  каждый шаг - новая папка, новые root, dirs, files 
    print(d)
print("----------")
for root, dirs, files in os.walk('.'): # - все возможные пути к папкам в текущей директории
    print(root)
print("----------")
for root, dirs, files in os.walk('.'): # - сколько файлов (не папок!) лежит в каждой папке
    print(root, len(files), sep='  ---  ')
print("----------")
i = 0
names = []
for root, dirs, files in os.walk('.'): # -есть ли файлы с именем длиной больше 10 (не учитывая расширение)
    for f in files:
        if len(f.split('.')[0]) > 10:
            i += 1
            names.append(f.split('.')[0])
print('Найдено {} файла(ов):'.format(i))
print("----------")
for name in names:
    print(name)
print("----------")
whole_corpus = ''
for root, dirs, files in os.walk('.'): # -собрать информацию во всех файлах
    for f in files:
        if not f.endswith('.txt'):
            continue       # файлы с другими расширениями, не относящиеся к корпусу, нас не интересуют.
        with open(os.path.join(root, f), 'r', encoding='utf-8') as text:
            whole_corpus += text.read()
print(len(whole_corpus.split()))
print("----------")
for root, dirs, files in os.walk('.', topdown=False): # - идем по папкам снизу вверх
    print(root)

for root, dirs, files in os.walk('.'): # - можно не посещать скрытые папки, например, 
    for d in dirs:                      # - которые начинатюся с "." или с любой другой буквы ("В")
        if d.startswith('B'):
            dirs.remove(d)
    print(root)
