#coding = 'utf-8'

import re


def main():
    with open('Лингвистика.html', 'r', encoding = 'utf-8') as f:
        text = f.read()
    new_text = re.sub('язык([а-я]{,3}([\s\&,.!\?:;<"\(\)\'» —-]))','шашлык\\1', text)
    new_text2 = re.sub('Язык([а-я]{,3}([\s\&,.!\?:;<"\(\)\'» —-]))','Шашлык\\1', new_text)
    with open('Другая лингвистика.html', 'w', encoding = 'utf-8') as f:
        f.write(new_text2)   
    print("Файл \"Другая лингвистика\"был создан.")


main()
