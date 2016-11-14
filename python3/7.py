#7. Программа должна получить от пользователя подряд 8 слов,
# а после этого вывести на экран 4 строчки с попарными склейками этих слов
arr1 = []
arr2 = []
for i in range (4):
    arr1.append(input('Введите слово: '))
    arr2.append(input('Введите слово: '))
for word in range(len(arr1)):
    print (arr1[word], arr2[word], sep='')

