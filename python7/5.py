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
    lenght = 0
    avr_len = 0
    ous = []
    for i in range(len(words)):
        if words[i].endswith("ous"):
            count += 1   
            len_word = len(words[i])
            lenght += len_word
    avr_len = int(lenght / count)
    print("В данном тексте", count, "прилагательных с суффиксом -ous.")
    print("Средняя длина такого прилагательного равна", avr_len, "слов(а).")

counting()
