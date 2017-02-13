#coding = 'utf-8'

import re


def main():
    with open('Динозавры.html', 'r', encoding = 'utf-8') as f:
        text = f.read()
    new_text = re.sub('диноз(а|а́)вр([а-я]{,3}([\s\&,.!\?:;<"\(\)\'» —-]))','кот\\2', text)
    new_text2 = re.sub('Диноз(а|а́)вр([а-я]{,3}([\s\&,.!\?:;<"\(\)\'» —-]))','Кот\\2', new_text)
    with open('Коты.html', 'w', encoding = 'utf-8') as f:
        f.write(new_text2)   
    print("Файл \"Коты\"был создан.")


main()
