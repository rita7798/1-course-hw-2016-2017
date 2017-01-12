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
    print("----------------------------------------------------------")
    if count != 0:
        print("Существительное", max_word, "имеет максимальную частотность - найдено", prev, "слов(а).")   

def main():
    counting(opening(input('Введите имя файла: ')))

main()
