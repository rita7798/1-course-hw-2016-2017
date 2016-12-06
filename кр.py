with open('quotes.txt','r', encoding = 'utf-8') as f: 
  text = f.read() 
  lines = text.split('\n') 
for line in lines: 
  line = line.split(' — '); 
  words = line[0].split(' ') 
  if len(words) < 10: 
    print(line[0], ' — ', line[1])


with open('quotes.txt','r', encoding = 'utf-8') as f: 
  text = f.read() 
  lines = text.split('\n') 
count = 0 
authors = [] 
for line in lines: 
  line = line.split(' — '); 
  if "разум" in line[0]: 
      count += 1 
      authors.append(line[1]) 
print("со словом 'разум' нашлось", count, "цитат") 
for author in authors[:-1]: 
  print(author, end=", ") 
print(authors[-1])
