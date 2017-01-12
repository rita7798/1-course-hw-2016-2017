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
    count_total = 0
    count_y = 0
    for i in range(len(words)):
        if words[i].endswith("ed"):
            count_total += 1   
            if words[i].endswith("ied"):
                count_y += 1           
    print("В данном тексте", count_total, "форм на -ed.")
    if count_total != 0:
        print("Из них на -y образованы", count_y, "слов(а).")

def main():
    counting(opening(input('Введите имя файла: ')))

main()
