#coding = utf-8

import re

def opening_text(fname):
    sentences = []
    words = []
    with open (fname, 'r', encoding = 'utf-8') as f:
        text = f.read()
    new_text = re.sub('[\.\?\!…]', 'q', text)
    sentences = new_text.split('q')
    for i in range(len(sentences)):
        sentences[i] = re.sub('[\.,*<>«»:;\'\"\n–-]','', sentences[i])
        sentences[i] = re.sub('[\xa0]',' ', sentences[i]) #особенность моего текста
        sentences[i] = sentences[i].strip() 
    return (sentences)


def making_list(sentences):
    list_of_words = [[word, len(word)] for sentence in sentences for word in sentence.split(' ') if len(word) > 0]
    template = "{}_{}"
    for i in list_of_words:
        print(template.format(i[0], i[1]))    

        
def main():
    sentences = opening_text(input("Введите название файла: "))
    making_list(sentences)


main()
