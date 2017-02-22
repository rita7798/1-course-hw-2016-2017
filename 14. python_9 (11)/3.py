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
        prog = re.match('программир(ова(ть.*|л[аои]?|в|нн.*|)|у(й(.*)?|я(сь)?|е.*|ю.*))', texte[i])
        if prog != None:
            words.add(texte[i])
        prog2 = re.match('буд(у(.*)?|е.*)', texte[i])
        prog = re.match('программир(ова(ть.*|л[аои]?|в|нн.*|)|у(й(.*)?|я(сь)?|е.*|ю.*))', texte[i+1])
        if prog2 != None and prog != None:
            texte[i+1] = texte[i+1].strip('”“".,«»\\/*!:;—()\'-?')
            word = texte[i] +" "+ texte[i+1]
            word = str(word)
            words.add(word)
    if len(words) != 0:
        print("Формы глагола 'программировать' в файле: ")
        for word in words:
            print (word)
        print("Всего разных форм найдено", len(words), "штук(и)." )
    else:
        print("Ни одной формы глагола 'программировать' в файле не найдено." )


def main():
    fname = input("Введите имя файла: ") 
    searching(fname)

main()
