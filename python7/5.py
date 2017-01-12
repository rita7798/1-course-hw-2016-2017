#coding = utf-8

def opening(name):
    words = []
    with open (name, 'r', encoding='utf-8') as f:
        for line in f.read().replace('\n', ' ').split():
            words.append(line.lower())
    for i in range(len(words)):
        words[i] = words[i].strip('.,!?*()«»\'";:-')
    return words

def counting(words):
    count = 0
    lenght = 0
    avr_len = 0
    ous = []
    for i in range(len(words)):
        if words[i].endswith("ous"):
            count += 1   
            len_word = len(words[i])
            lenght += len_word
    print("В данном тексте", count, "прилагательных с суффиксом -ous.")
    if count != 0:
        print("----------------------------------------------------")
        avr_len = int(lenght / count)
        print("Средняя длина такого прилагательного равна", avr_len, "слов(а).")

def main():
    counting(opening(input('Введите имя файла: ')))

main()
