def opening():
    words = []
    with open (input('Введите имя файла: '), 'r', encoding='utf-8') as f:
        for line in f.read().split():
            words.append(line.lower())
    for i in range(len(words)):
        words[i] = words[i].strip('.,!?*()«»\'";:-')
    return words

def counting():
    words = opening()
    count = 0
    count_samples = 0
    ings = []
    ings_samples = set()
    for i in range(len(words)):
        if words[i].endswith("ing"):
            count += 1
            ings.append(words[i])
            ings_samples.add(words[i])
    print("С окончанием -ing встретилось", count, "слов(а).")
    for word in ings_samples:
        a = ings.count(word)
        print("Для слова", word, "встретилось", a, "примера(ов).")
        count_samples += 1
    print("Всего разных словоформ встретилось", count_samples, "штук(и).")
        
counting()
