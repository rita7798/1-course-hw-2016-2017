with open ("file.txt", "r", encoding = "utf-8") as f:
    s = f.read()
    s = s.replace("\n"," ")
    words = s.split()
    
len1 = 0
len3 = 0

for word in words:
    if len(word) == 1:
        len1 += 1
    elif len(word) == 3:
        len3 += 1

if len1 == 0:
    print ("слов длины 1 нет")
elif len3 == 0:
    print ("слов длины 3 нет") 

len3_to_len1 = len3/len1

print("В", len3_to_len1, "раз")
