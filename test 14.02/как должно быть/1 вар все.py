#coding = utf-8

import re

def opening_words(text):
    words = []
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
    with open('counting.txt', 'w', encoding='utf-8') as f:
        f.write(str(len(headers)))

        
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
    with open('forms.txt', 'a', encoding='utf-8') as f:
        for key, freq in forms.items():
            word = str(key) + " : " + str(freq) + "\n"
            f.write(word)


#10
def searching_forms(words):
    more_forms = []
    for i in range (len(words)):
        reg = "<w lemma=\"(.*)\" type=\"(f.h.*?)\">(.*)<"
        if re.search(reg, words[i]):
            res = re.search(reg, words[i]).group(3)
            more_forms.append(res)
    return more_forms

def printing_out_more_forms(more_forms):
    with open('forms.txt', 'a', encoding='utf-8') as f:
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
            with open('corpus.csv', 'w', encoding='utf-8') as f:
                for i in range (len(results)):
                    word = results[i] + "\n"
                    f.write(word)
            

        
def main():
    with open("F.xml", 'r', encoding='utf-8') as f:
        text = f.read()
    words = opening_words(text)
    counting_headers(words)
    forms = counting_words(words)
    making_list(forms)
    more_forms = searching_forms(words)
    printing_out_more_forms(more_forms)
    making_corpus(words)
    print("Все задания выполнены.")

main()
