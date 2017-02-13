#coding = 'utf-8'

import re


def main():
    with open('Птицы.html', 'r', encoding = 'utf-8') as f:
        text = f.read()
    new_text = re.sub('пт(и|и́)ц([а-я]{,3}([\s\&,.!\?:;<"\(\)\'» —-]))','рыб\\2', text)
    new_text2 = re.sub('Пт(и|и́)ц([а-я]{,3}([\s\&,.!\?:;<"\(\)\'» —-]))','Рыб\\2', new_text)
    with open('Рыбы.html', 'w', encoding = 'utf-8') as f:
        f.write(new_text2)   
    print("Файл \"Рыбы\"был создан.")


main()
