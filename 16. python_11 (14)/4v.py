#coding = 'utf-8'

import re


def main():
    with open('Философия.html', 'r', encoding = 'utf-8') as f:
        text = f.read()
    new_text = re.sub('филос(о|о́)ф([а-я]{,3}([\s\&,.!\?:;<"\(\)\'» —-]))','астролог\\2', text)
    new_text1 = re.sub('ФИЛОСОФ([А-Я]{,3}([\s\&,.!\?:;<"\(\)\'» —-]))','АСТРОЛОГ\\2', new_text)
    new_text2 = re.sub('Филос(о|о́)ф([а-я]{,3}([\s\&,.!\?:;<"\(\)\'» —-]))','Астролог\\2', new_text1)
    with open('Астрология.html', 'w', encoding = 'utf-8') as f:
        f.write(new_text2)   
    print("Файл \"Астрология\"был создан.")


main()
