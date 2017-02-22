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
    uns = []
    count = 0
    for i in range(len(words)):
        if words[i].startswith("un"):
            uns.append(words[i])
            count += 1
    print("С приставкой -un в тексте нашлось", count, "слов(а).")
    return uns
    
def comparison(uns):
    if len(uns) != 0:
        print("----------------------------------------------------")
        n = int(input("Введите число: "))
        bigger = []
        for i in range(len(uns)):
            if len(uns[i]) > n:
                bigger.append(uns[i])
        percent = int(len(bigger) / len(uns) * 100)
        print("Длинну большую,чем", n, ", имеет", percent, "% слов.")

def main():
    comparison(counting(opening(input('Введите имя файла: '))))

main()
