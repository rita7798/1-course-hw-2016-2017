#coding = 'utf-8'

import re


def main():
    with open('Викинги.html', 'r', encoding = 'utf-8') as f:
        text = f.read()
    new_text = re.sub('в(и|и́)кинг([а-я]{,3}([\s\&,.!\?:;<"\(\)\'» —-]))','бурундук\\2', text)
    new_text2 = re.sub('В(и|и́)кинг([а-я]{,3}([\s\&,.!\?:;<"\(\)\'» —-])?)','Бурундук\\2', new_text)
    with open('Бурундуки.html', 'w', encoding = 'utf-8') as f:
        f.write(new_text2)   
    print("Файл \"Бурундуки\"был создан.")


main()
