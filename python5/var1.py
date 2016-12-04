with open ("file.txt", "r", encoding = "utf-8") as f:
    s = f.read()
    lines = s.split("\n")
    
count_of_words = 0
for line in lines:
        words = line.split()

        count_of_words += len(words)

average_words_in_line = count_of_words / len(lines)

print (average_words_in_line)
