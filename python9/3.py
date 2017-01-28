#coding = utf-8

import re


def searching(fname):
    texte = []
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    text = text.lower()
    texte = text.split()
    words = set()
    for i in range (len(texte)-1):
        texte[i] = texte[i].strip('”“".,«»\\/*!:;—()\'-?')
        prog = re.match('программир(у(ют?|е(шь|те?|м(ы(ми|м|й)|ой|ых|ые|ом(у)?|а(я)?|ы|ого|ый|ую|ое|))|я)|о(ва(л[аи]?|ть(ся)?|нн?[аы]?(й|ого|ому|ую|м(и)?|ом|ое|ой|я|е|х|))|))', texte[i])
        if prog != None:
            words.add(texte[i])
        prog2 = re.match('буд(у(чи|т)?|е(шь|те?|м))', texte[i])
        if prog2 != None:
            word = texte[i] +" "+ texte[i+1]
            word = str(word)
            words.add(word)
    if len(words) != 0:
        print("Формы глагола 'программировать' в файле: ")
        for word in words:
            print (word)
        print("Всего найдено", len(words), "штук(и)." )
    else:
        print("Ни одной формы глагола 'программировать' в файле не найдено." )


def main():
    fname = input("Введите имя файла: ") 
    searching(fname)

main()
