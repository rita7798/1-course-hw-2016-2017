import os
import re


c = 0
for root, dirs, files in os.walk('.'):
    for d in dirs:
        if re.search("[А-ЯЁа-яё]", d) != None and re.search("[\d]", d) == None and re.search("[A-Za-z]", d) == None:
            c += 1 # не учитываются названия с цифрами и латиницей

print("Папок с полностью кириллическими названиями -- ", c)
