#coding = utf-8

import re

def opening_words(text):
    words = []
    words = text.split("\n")
    return words


#5
def counting_words(words):
    with open('counting2.txt', 'w', encoding='utf-8') as f:
        f.write(str(len(words)))

        
#8
def making_forms(words):
    forms = {}
    for i in range (len(words)):
        reg = "<w lemma=\".*\" type=\"(.*)\""
        if re.search(reg, words[i]):
            result = re.search(reg, words[i]).group(1)
            if result not in forms:
                forms[result] = 1
            else:
                forms[result] += 1
        else:
            continue
    return forms

def printing_out(forms):
    with open('forms2.txt', 'w', encoding='utf-8') as f:
        for key, freq in forms.items():
            word = str(key) + "\n"
            f.write(word)

        
#10
def searching_forms(words):
    more_forms = []
    for i in range (len(words)):
        reg = "<w lemma=\".*\" type=\"(l.f.*?)\">(.*)<"
        if re.search(reg, words[i]):
            res = re.search(reg, words[i]).group(2)
            more_forms.append(res)
    return more_forms

def printing_out_more_forms(more_forms):
    with open('forms2.txt', 'a', encoding='utf-8') as f:
        for i in range (len(more_forms)):
            word = more_forms[i] + ", "
            f.write(word)

def making_corpus(words):
    results = []
    regex = "(\s.*)?(<w lemma=\"(.*)\" type=\"(.*)\">(.*)</w>)"
    for i in range (len(words)):
        if re.search(regex, words[i]):
            res = re.search(regex, words[i]).group(2)
            result = re.sub("<w lemma=\"(.*)\" type=\"(.*)\">(.*)</w>", "\\1, \\2, \\3", res)
            results.append(result)
            with open('corpus2.csv', 'w', encoding='utf-8') as f:
                for i in range (len(results)):
                    word = results[i] + "\n"
                    f.write(word)
            

        
def main():
    with open("F.xml", 'r', encoding='utf-8') as f:
        text = f.read()
    words = opening_words(text)
    counting_words(words)
    forms = making_forms(words)
    printing_out(forms)
    more_forms = searching_forms(words)
    printing_out_more_forms(more_forms)
    making_corpus(words)
    print("Все задания выполнены.")
   
main()
