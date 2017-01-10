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
    count_with = 0
    count_without = 0
    omnis = []
    non_omnis = []
    omnis_samples = set()
    non_omni_samples = set()
    non_omnis_samples = set()
    for i in range(len(words)):
        if words[i].startswith("omni"):
            count_with += 1
            omnis.append(words[i])
            omnis_samples.add(words[i])
    non_omni_samples = omnis_samples.copy()
    for word in non_omni_samples:
        word_new = word[4:]
        non_omnis_samples.add(word_new)
        for i in range(len(words)):
            if word_new == words[i]:
                count_without += 1
                non_omnis.append(words[i])
    print("С приставкой -omni встретилось", count_with, "слов(а)")
    for word in omnis_samples:
        a = omnis.count(word)
        print("Для слова", word, "встретилось", a, "примера(ов)")
    print("Тех же слов, но без приставки -omni встретилось", count_without)
    for word in non_omnis_samples:
        a = non_omnis.count(word)
        print("Для слова", word, "встретилось", a, "примера(ов)")

counting()
