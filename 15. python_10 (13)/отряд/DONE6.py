#coding = 'utf-8'

import re


def searching(fname):
    with open (fname, 'r', encoding = 'utf-8') as f:
        text = f.read()
    name = fname[:-5]
    reg = '>Отряд(.*\n?).*\n?.*"?>(.+?)(</b>|</a>)'
    if re.search(reg, text):
        res = re.search(reg, text).group(2)
        print("Отряд для животного", name, "успешно записан в файл!")
        with open ('results.txt', 'w', encoding = 'utf-8') as f:
                f.write(res)
    else:
        print("Нет нужной информации.")
        with open ('results.txt', 'w', encoding = 'utf-8') as f:
            f.write("Нет нужной информации.")
    
def main():
    iname = str(input("Введите название животного: ")) #черепаха, сурикат, бизон, утконос - 4 различных животных на выбор
    fname = iname.lower()+".html"
    searching(fname)

main()
