with open('quotes.txt','r', encoding = 'utf-8') as f: 
  text = f.read() 
  lines = text.split('\n') 
for line in lines: 
  line = line.split(' — '); 
  words = line[0].split(' ') 
  if len(words) < 10: 
    print(line[0], ' — ', line[1])

    
