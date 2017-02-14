#coding = utf-8

import re
import csv

def opening_words(text):
    words = []
    text = text.lower()
    words = text.split("\n")
    return words


#5
def counting_headers(words):
    headers = []
    for i in range (len(words)):
        if words[i] != "  <text>":
            headers.append(words[i])
        else:
            break
    count = str(len(headers))
    with open('counting.txt', 'w', encoding='utf-8') as f:
        f.write(count)

        
#8
def counting_words(words):
    forms = {}
    for i in range (len(words)):
        reg = "<w lemma=\"(.*)\" type=\"(.*)\""
        if re.search(reg, words[i]):
            res = re.search(reg, words[i]).group(2)
            if res not in forms:
                forms[res] = 1
            else:
                forms[res] += 1
        else:
            continue
    return forms


def making_list(forms):
    with open('answwers.csv', 'a', encoding='utf-8') as f:
        output = csv.writer(f, delimiter=',')
        header = ['слово', 'частота']
        output.writerow(header)
        for key in sorted(forms.keys()):
            output.writerow([key, forms[key]])

#10

        
def main():
    with open("F1.xml", 'r', encoding='utf-8') as f:
        text = f.read()
    words = opening_words(text)
    counting_headers(words)
    forms = counting_words(words)
    making_list(forms)

   
main()
