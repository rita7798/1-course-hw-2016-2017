def opening():
    words = []
    with open (input('Введите имя файла: '), 'r', encoding='utf-8') as f:
        for line in f.read().split():
            words.append(line.lower())
    for i in range(len(words)):
        words[i] = words[i].strip('.,!?*()«»\'";:-')
    return words

def appending_uns():
    words = opening()
    uns = []
    for i in range(len(words)):
        if words[i].startswith("un"):
            uns.append(words[i])
    return uns
    
def counting():
    count = 0
    uns = appending_uns()
    for i in range(len(uns)):
        count += 1                
    print("С приставкой -un в тексте нашлось", count, "слов(а).")
    return uns
    
def comparison():
    bigger = []
    uns = counting()
    for i in range(len(uns)):
        if len(uns[i]) > n:
            bigger.append(uns[i])
    percent = int(len(bigger) / len(uns) * 100)
    print("Длинну большую,чем", n, ", имеет", percent, "% слов.")
    
n = int(input("Введите число: "))
comparison()
