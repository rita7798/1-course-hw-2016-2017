with open ("file.txt", "r", encoding = "utf-8") as f:
    s = f.read()
    s = s.replace("\n"," ")
    words = s.split()

Commas = [",","."]
words_without = 0
words_total = len (words)

for word in words:
  if not (word[-1] in Commas) :
        words_without += 1

if words_without == words_total:
  print ("слов с препинаниями нет")
else:
  print ("процент", words_without / words_total * 100)

