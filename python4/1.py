s = input('Введите слово: ')
for i in range(len(s)):
    if i==0:
        print (s)
    else:
        print(s[:-i])
