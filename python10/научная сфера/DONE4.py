#coding = 'utf-8'

import re


def searching(fname):
    with open (fname, 'r', encoding = 'utf-8') as f:
        text = f.read()
    name = fname[:-5]
    name = name.capitalize()
    reg = '>Научная сфера(.*\n?).*\n?.*">(.+?)</a>(</span>)?'
    if re.search(reg, text):
        res = re.search(reg, text).group(2)
        print("Научная сфера для ученого", name, "успешно записана в файл!")
        with open ('results.txt', 'w', encoding = 'utf-8') as f:
                f.write(res)
    else:
        print("Нет нужной информации.")
        with open ('results.txt', 'w', encoding = 'utf-8') as f:
            f.write("Нет нужной информации.")
    
def main():
    iname = str(input("Введите фамилию ученого: ")) #Павлов, Королев, Сахаров, Эйнштейн - 4 различных ученых на выбор
    fname = iname.lower()+".html"
    searching(fname)

main()
