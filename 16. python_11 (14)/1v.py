#coding = 'utf-8'

import re


def main():
    with open('Комары.html', 'r', encoding = 'utf-8') as f:
        text = f.read()
    new_text = re.sub('комар([а-я]{,3}([\s\&,.!\?:;<"\(\)\'» —-])|(ы́))','слон\\1', text)
    new_text2 = re.sub('Комар([а-я]{,3}([\s\&,.!\?:;<"\(\)\'» —-])|(ы́))','Слон\\1', new_text)
    with open('Слоны.html', 'w', encoding = 'utf-8') as f:
        f.write(new_text2)   
    print("Файл \"Слоны\"был создан.")


main()
