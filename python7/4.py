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
    count_total = 0
    count_y = 0
    for i in range(len(words)):
        if words[i].endswith("ed"):
            count_total += 1   
            if words[i].endswith("ied"):
                count_y += 1           
    print("В данном тексте", count_total, "форм на -ed.")
    print("Из них на -y образованы", count_y, "слов(а).")


counting()
