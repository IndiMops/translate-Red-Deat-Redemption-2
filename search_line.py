import os

print('Щоб вийти натисніть Ctrl++C')



while True:
    text = input('Введіть текст: ')
    strings = []
    for root, dirs, files in os.walk('en_txt'):
        for filename in files:
            if filename.endswith('.txt'):
                path = f'{root}\{filename}'
                with open(path, 'r', errors="ignore") as f:
                    for string in f:
                        str_encode = string.encode(encoding = 'UTF-8')
                            
                        str_decode = str_encode.decode()
                            
                        if text in str_decode or text in str_decode.lower():
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
