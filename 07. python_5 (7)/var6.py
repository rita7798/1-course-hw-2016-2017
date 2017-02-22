with open ("file.txt", "r", encoding = "utf-8") as f:
    s = f.read()
    s = s.replace("\n"," ")
    words = s.split()

words_count = 0
words_total = len (words)

for word in words:
  C = word[0]
  if C.isupper():
        words_count+= 1 

print ("процент", words_count  / words_total * 100)

