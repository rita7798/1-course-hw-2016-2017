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
    prev = 1000
    a = 0
    min_word = ""
    hoods = []
    hoods_samples = set()
    for i in range(len(words)):
        if words[i].endswith("hood") or words[i].endswith("hoods"):
            count += 1
            hoods.append(words[i])
            hoods_samples.add(words[i])                
    hoods.sort()
    for word in hoods_samples:
        a = hoods.count(word)
        if a < prev:
            prev = a
            min_word = word
        else:
            a = 0
    print("В данном тексте", count, "прилагательных с суффиксом -hood.")
    print("Существительное", min_word, "имеет минимальную частотность - найдено всего", prev, "слов(а).")   
    return hoods_samples

def forming():
    forms = []
    hoods_samples = counting()
    for word in hoods_samples:
        word = word[:-4]
        forms.append(word)
    print("Вот такие получились корни:")
    for i in range(len(forms)):
        print(forms[i], sep = "\n")

forming()
