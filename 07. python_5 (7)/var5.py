with open ("file.txt", "r", encoding = "utf-8") as f:
    s = f.read()
    s = s.replace("\n"," ")
    words = s.split()
    
words_more_than_10 = 0
words_total = len (words)

for word in words:
  if len(word) > 10:
        words_more_than_10 += 1

print ("процент", words_more_than_10  / words_total * 100)

