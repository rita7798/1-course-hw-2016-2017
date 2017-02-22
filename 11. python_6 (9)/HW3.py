import random


def noun():
    nouns = []
    with open('nouns.txt','r', encoding = 'utf-8') as f: 
        lines = f.readlines()
        for line in lines:
            nouns.append(line)
    nouns.remove(" ")
    n = random.choice(nouns)
    n = n[0:len(n)-1]
    return n

def noun2():
    nouns2 = []
    with open('nouns.txt','r', encoding = 'utf-8') as f: 
        lines = f.readlines()
        for line in lines:
            nouns2.append(line)
    nouns2.remove(" ")
    n = random.choice(nouns2)
    n = n[0:len(n)-1]
    if n[-1] == 'а':
        n = n[:-1] + 'е'
    else:
        n += 'у'
    return n
    

def adjective():
    adjectives = []
    with open('adjectives.txt','r', encoding = 'utf-8') as f: 
        lines = f.readlines()
        for line in lines:
            adjectives.append(line)
    adjectives.remove(" ")
    adj = random.choice(adjectives)
    adj = adj[0:len(adj)-1]
    n = noun()
    if n[-1] == 'а':
        adj = adj[:-2] + 'ая'
    if n == 'Василиса':
        n = n.capitalize()
    return adj.capitalize() + ' ' + n


def verb():
    verbs = []
    with open('verbs.txt','r', encoding = 'utf-8') as f: 
        lines = f.readlines()
        for line in lines:
            verbs.append(line)
    verbs.remove(" ")
    v = random.choice(verbs)
    v = v[0:len(v)-1]
    return v


def imperative_verb():
    imp_verbs = []
    with open('imp_verbs.txt','r', encoding = 'utf-8') as f: 
        lines = f.readlines()
        for line in lines:
            imp_verbs.append(line)
    imp_verbs.remove(" ")
    iv = random.choice(imp_verbs)
    iv = iv[0:len(iv)-1]
    return iv


def infinitive():
    infinitives = []
    with open('infinitives.txt','r', encoding = 'utf-8') as f: 
        lines = f.readlines()
        for line in lines:
            infinitives.append(line)
    infinitives.remove(" ")
    inf = random.choice(infinitives)
    inf = inf[0:len(inf)-1]
    return inf
    
      
def adverb():   
    adverbs = []
    with open('adverbs.txt','r', encoding = 'utf-8') as f: 
        lines = f.readlines()
        for line in lines:
            adverbs.append(line)
    adverbs.remove(" ")
    a = random.choice(adverbs)
    a = a[0:len(a)-1]
    return a
    
    
def ifword():
    ifwords = []
    with open('ifwords.txt','r', encoding = 'utf-8') as f: 
        lines = f.readlines()
        for line in lines:
            ifwords.append(line)
    ifwords.remove(" ")
    iw = random.choice(ifwords)
    iw = iw[0:len(iw)-1]
    return iw    
        

def declarative_sentence():
    return (adjective() + ' ' + adverb() + ' ' + verb() + '.')


def interrogative_sentence():
    return (adverb().capitalize() + ' ' + 'ли ' + noun() + ' ' + verb() + '?')


def negative_sentence():
    
    return (adjective() + ' ' + adverb() + ' не '+ verb() + '.')


def conditional_sentence():
    return (ifword().capitalize() + ' ' + noun() + ' будет ' + adverb() + ' ' + infinitive() + ' ' + ', то ' + noun2() + ' будет ' + adverb() +  '.')    


def imperative_sentences():
    return (adjective() + ', ' + imperative_verb() + ' ' + adverb() + '!')



elem = 0
a = []
for i in range(1,6):
    a.append(i)
random.shuffle(a)
for j in range(5):
    i = a[elem]   
    if i == 1:
        print(declarative_sentence())
    elif i == 2:
        print(interrogative_sentence())
    elif i == 3:
        print(negative_sentence())
    elif i == 4:
        print(conditional_sentence())
    else:
        print(imperative_sentences())
    a.pop(elem)
