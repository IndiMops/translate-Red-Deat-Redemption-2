import os

print('Щоб вийти натисніть Ctrl+C')

while True:
    text = input('Введіть текст: ')
    strings = []
    for root, dirs, files in os.walk('en_txt'):
        for filename in files:
            if filename.endswith('.txt'):
                path = os.path.join(root, filename)
                with open(path, 'r', encoding='UTF-8', errors="ignore") as f: # кодинги: cp1251 - для англійської, UTF-8 - для кирилиці
                    for string in f:
                        if text in string or text in string.lower():
                            line = dict()
                            line['file'] = filename
                            line['string'] = string
                            strings.append(line)
    if strings == []:
        print('Текст не був знайдений серед усіх файлів!')
    else:
        if len(strings) == 1:
            print(f'Знайдено {len(strings)} збіг')
        else:
            print(f'Знайдено {len(strings)} збігів')
        for i in strings:
            print(f'Файл: {i["file"]}, з текстом:\n{i["string"]}')
