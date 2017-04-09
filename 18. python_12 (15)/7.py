#coding = utf-8

import re


def opening_text(fname):
    sentences = []
    words = []
    with open (fname, 'r', encoding = 'utf-8') as f:
        text = f.read().lower()
    new_text = re.sub('[\.\?\!…]', 'q', text)
    sentences = new_text.split('q')
    for i in range(len(sentences)):
        sentences[i] = re.sub('[\.,*<>«»:;\'\"\n–-]','', sentences[i])
        sentences[i] = re.sub('[\xa0]',' ', sentences[i]) #особенность моего текста
        sentences[i] = sentences[i].strip()
    return (sentences)


def making_list(sentences):
    count = {word : sentence.count(word) for sentence in sentences for word in sentence.split(' ')}
    repeating = {word : count[word] for word in count if count[word] > 1}
    template = "{}   {}"
    for key in repeating:
        print(template.format(key, repeating[key]))
    if repeating == {}:
        print("Повторяющихся слов не найдено.")


def main():
    sentences = opening_text(input("Введите название файла: "))
    making_list(sentences)


main()
