with open ("file.txt", "r", encoding = "utf-8") as f:
    s = f.read()
    lines = s.split("\n")
    
max_len = 0
min_len = len(lines[0])

for line in lines:
    str_len = len(line)
    if str_len > max_len:
        max_len = str_len
    if str_len < min_len:
        min_len = str_len

min_to_max =  min_len / max_len

print ("В", min_to_max, "раз")
