with open ("file.txt", "r", encoding = "utf-8") as f:
    s = f.read()
    lines = s.split("\n")
    
count_of_lines = 0
for line in lines:
        words = line.split(" ")
        if len(words) > 5:
                count_of_lines += 1
           
print ("процент ", count_of_lines / len(lines) * 100)


