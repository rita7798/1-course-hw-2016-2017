#я быстро иду.
#я иду быстро?
#я не иду быстро.
#если бы я быстро шла...
#иди быстро!

import random

def noun():
    nouns = []
    with open('nouns.txt','r', encoding = 'utf-8') as f: 
        lines = f.readlines()
        for line in lines:
            nouns.append(line)
    n = random.choice(nouns)
    n = n[0:len(n)-1]
    return n

def verb():
    verbs = []
    with open('verbs.txt','r', encoding = 'utf-8') as f: 
        lines = f.readlines()
        for line in lines:
            verbs.append(line)
    v = random.choice(verbs)
    v = v[0:len(v)-1]
    return v

def imperative_verb():
    imp_verbs = []
    with open('imp_verbs.txt','r', encoding = 'utf-8') as f: 
        lines = f.readlines()
        for line in lines:
            imp_verbs.append(line)
    iv = random.choice(imp_verbs)
    iv = iv[0:len(iv)-1]
    return iv
        
def adverb():   
    adverbs = []
    with open('adverbs.txt','r', encoding = 'utf-8') as f: 
        lines = f.readlines()
        for line in lines:
            adverbs.append(line)
    a = random.choice(adverbs)
    a = a[0:len(a)-1]
    return a
    
def ifword():
    ifwords = []
    with open('ifwords.txt','r', encoding = 'utf-8') as f: 
        lines = f.readlines()
        for line in lines:
            ifwords.append(line)
    iw = random.choice(ifwords)
    iw = iw[0:len(iw)-1]
    return iw    
        

def declarative_sentence():
    return (noun() + ' ' + adverb() + ' ' + verb() + '.')


def interrogative_sentence():
    return (noun() + ' ' + verb() + ' ' + adverb() + '?')


def negative_sentence():
    return (noun() + ' ' + 'не' + ' ' + verb() + ' ' + adverb() + '.')


def conditional_sentence():
    return (ifword().capitalize() + ' ' + noun() + ' ' + verb() + ' ' + adverb() + '...')    


def imperative_sentences():
    return (imperative_verb() + ' ' + adverb() + '!')



elem = 0
a = []
for i in range(1,6):
    a.append(i)
random.shuffle(a)
for j in range(5):
    i = a[elem]   
    if i == 1:
        print(declarative_sentence().capitalize())
    elif i == 2:
        print(interrogative_sentence().capitalize())
    elif i == 3:
        print(negative_sentence().capitalize())
    elif i == 4:
        print(conditional_sentence())
    else:
        print(imperative_sentences().capitalize())
    a.pop(elem)
