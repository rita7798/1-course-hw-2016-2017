s = input('Введите слово: ')
for i in range(len(s)//2+1):
    if i==0:
        print (s)
    else:
        print(s[i:-i])
