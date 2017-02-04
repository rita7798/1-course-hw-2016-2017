#coding = 'utf-8'

import re


def searching(fname):
    with open (fname, 'r', encoding = 'utf-8') as f:
        text = f.read()
    name = fname[:-5]
    name = name.capitalize()
    reg = 'Преподаватели(.*\n?)*?<p>(.+?)<'
    if re.search(reg, text):
        res = re.search(reg, text).group(2)
        print("Данные о количестве преподавателей в", name, "успешно записаны в файл!")
        with open ('results.txt', 'w', encoding = 'utf-8') as f:
                f.write(res)
    else:
        print("У", name, "нет нужной информации о количестве преподавателей в карточке на сайте Википедиа!")
        with open ('results.txt', 'w', encoding = 'utf-8') as f:
            f.write("Нет нужной информации.")
    
def main():
    iname = str(input("Введите название вуза: ")) #вшэ, мгу, маи, мифи - 4 различных вуза на выбор
    fname = iname.lower()+".html"
    searching(fname)

main()
