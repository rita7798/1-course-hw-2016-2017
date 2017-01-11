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
    prev = 0
    a = 0
    max_word = ""
    ness = []
    ness_samples = set()
    for i in range(len(words)):
        if words[i].endswith("ness"):
            ness.append(words[i])
            ness_samples.add(words[i])                
    ness.sort()
    for word in ness_samples:
        count += 1
        a = ness.count(word)
        if a >= prev:
            prev = a
            max_word = word
        
    print("В данном тексте", count, "разных существительных с суффиксом -ness.")
    if count != 0:
        print("Существительное", max_word, "имеет максимальную частотность - найдено", prev, "слов(а).")   

counting()
