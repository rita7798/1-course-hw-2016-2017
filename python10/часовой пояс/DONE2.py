#coding = 'utf-8'

import re


def searching(fname):
    with open (fname, 'r', encoding = 'utf-8') as f:
        text = f.read()
    name = fname[:-5]
    name = name.capitalize()
    reg = '>Часовой пояс(.*\n?).*(\n)?.*">(.+?)</a></div>'
    if re.search(reg, text):
        res = re.search(reg, text).group(3)
        print("Часовой пояс для города", name, "успешно записан в файл!")
        with open ('results.txt', 'w', encoding = 'utf-8') as f:
                f.write(res)
    else:
        print("Нет нужной информации.")
        with open ('results.txt', 'w', encoding = 'utf-8') as f:
            f.write("Нет нужной информации.")
    
def main():
    iname = str(input("Введите название города: ")) #Москва, Калининград, Пермь, Новосибирск - 4 различных города на выбор
    fname = iname.lower()+".html"
    searching(fname)

main()
