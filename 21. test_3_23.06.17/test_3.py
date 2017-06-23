import os
import csv
import re

#1
def opening():
    path = os.getcwd() + "/news"
    for root, dirs, files in os.walk(path): # -собрать информацию во всех файлах
        for f in files:
            if f == ".DS_Store":
                continue
            else:
                path1 = os.path.join(root, f)
                with open(path1, 'r', encoding='cp1251') as j:
                    text = j.read()
                    lines = []
                    lines = text.split("\n")    
                    words = 0
                    reg = '</ana>(.*)</w>'
                    for line in lines:
                        if re.search(reg, line):
                            words += 1
                    #print(words)
                    template = "{}\t{}\n"
                    with open('list.txt', 'a', encoding='utf-8') as t:
                        t.write(template.format(f, words))
                                    

#2
def making_csv():
    with open('table.csv', 'w', encoding='utf-8') as f:
        output = csv.writer(f, delimiter='|')
        header = ['Название файла', 'Автор', 'Дата создания текста' ]
        output.writerow(header)
    path = os.getcwd() + "/news"
    for root, dirs, files in os.walk(path): # -собрать информацию во всех файлах
        for f in files:
            if f == ".DS_Store":
                continue
            else:
                path1 = os.path.join(root, f)
                with open(path1, 'r', encoding='cp1251') as j:
                    text = j.read()
##                    lines = []
##                    lines = text.split("\n")    
                    reg = '<meta content=\"(.*)\" name=\"author\"'
                    reg1 = '<meta content=\"(.*)\" name=\"created\"'
##                    for line in lines:
                    if re.search(reg, text) and re.search(reg1, text):
                           author = re.search(reg, text).group(1)
                           date = re.search(reg1, text).group(1)                          
                           with open('table.csv', 'a', encoding='utf-8') as o:
                                output = csv.writer(o, delimiter='|')
                                output.writerow([f, author, date])


#3 (недоделала с предложениями....)
def making_bigramms():
  path = os.getcwd() + "/news"
  for root, dirs, files in os.walk(path): # -собрать информацию во всех файлах
        for f in files:
            if f == ".DS_Store":
                continue
            else:
                path1 = os.path.join(root, f)
                with open(path1, 'r', encoding='cp1251') as j:
                    text = j.read()
                    lines = []
                    lines = text.split("\n")    
                    reg = 'gr=\".*,gen.*</ana>(.*)</w>'
                    for i in range(len(lines)):
                        #print(lines[i])
                        if re.search(reg, lines[i]) and re.search(reg, lines[i+1]):
                           a = re.search(reg, lines[i]).group(1)
                           b = re.search(reg, lines[i+1]).group(1)
                           #print(a, b)
                           template = "{}\t{}\n"
                           with open('bi.txt', 'a', encoding='utf-8') as t:
                                t.write(template.format(a, b))
                    sents = []
                    for line in lines:
                        reg = "\n.*</ana>(.*)</w>"
                        if re.search(reg, line):
                           word = re.search(reg, line).group(1)
                           sents.append(word)
                           with open('bi.txt', 'a', encoding='utf-8') as t:
                               for sent in range(len(sents)):
                                   t.write(template.format(a, b, sent))






def main():
    lines = opening()
    making_csv()
    making_bigramms()


main()
