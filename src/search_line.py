import os
import json

print('Щоб вийти натисніть Ctrl+C\nВітаю! Введіть у поле нижче, що ви хочете зробити.')
def start():
    print('Меню\n1 - налаштувати програму; 2 - запустити програму;')
    answer = input('> ')

    if answer == '1':
        settings()
    elif answer == '2':
        search()
    else:
        print('ПОМИЛКА: Стався якийсь збій та/або ви ввели неправильне значення!\nПриймається лише цілі числа від 1 до 2.\n\n')
        start()

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def search():
    with open('config.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)
        
    if not os.path.exists(data['data_folder']):
        print('ПОМИЛКА: Такої папки не існує!\nПапки за вказеним шляхом немає. Будь ласка вкажіть дійсну папку!')
        start()
    elif not os.listdir(data['data_folder']):
        print('ПОМИЛКА: Папка порожня!\nПапка за вказаним шляхом є порожня. Будь ласка перенесіть файли гри в папку, яку ви вказали, або змініть папку.')
        start()
    else:
        print('Щоб очистити консоль напишіть: sudo cls.\nОчищення консолі працює лише тут, в меню не працює.\nЩоб повернутися в меню напишіть: sudo back')
        while True:
            text = input('Введіть текст: ')
            if text == 'sudo cls' or text == 'ігвщ сдк':
                clear_console()
            elif text == 'sudo back' or text == 'ігвщ ифсл':
                start()
            else:
                strings = []
                for root, dirs, files in os.walk(data['data_folder']):
                    for filename in files:
                        if filename.endswith('.txt'):
                            path = os.path.join(root, filename)
                            with open(path, 'r', encoding=data['encoding'], errors="ignore") as f: # cp1251 - для англійської, UTF-8 - для кирилиці
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

def settings():
    with open('config.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)
    print('Налаштування')
    print('Виберіть, що хочете зробити:\n1 - дізнатися поточні налаштування; 2 - змінити налаштування; 3 - запустити програму;')
    answer = input('> ')
    
    def get_settings():
        print('Поточні налаштування')
        path = data["data_folder"]
        for i in path:
                if i == '\\':
                    path.replace("\\\\", "\\")
        print(f'Папка із файлами гри: {path};\nЕнкодинг: {data["encoding"]};')
        settings()
        
    def set_settings():
        print('Встановлення налаштувань')
        print('Виберіть, що хочете зміниити:\n1 - змінити шлях до файлів гри; 2 - змінити енкодинг; 3 - повернутися назад;')
        
        def set_path():
            print('Змінна шляху до файлів')
            print('Шлях можна вказати абсолютний(C:\\Users\\User\\...\\data),\nабо відносний(тобто в цій саміж папці: data)')
            path = input('> ')
            for i in path:
                if i == '\\':
                    path.replace('\\', '\\\\')
            
            data['data_folder'] = path
            
            with open("config.json", "w") as file:
                json.dump(data, file, indent = 4)
            set_settings()
        
        def set_encoding():
            print('Зміна типу енкодінгу')
            print('Енкодінг потрібен для коректоного відображення тексту.\nТому, якщо ви працюєте лише із латиницею пишіть: 1, а якщо із латиницею та кирилицею то: 2')
            encoding = input('> ')
            if encoding == '1':
                data['encoding'] = 'cp1251'
                with open("config.json", "w") as file:
                    json.dump(data, file, indent = 4)
                set_settings()
            elif encoding == '2':
                data['encoding'] = 'UTF-8'
                with open("config.json", "w") as file:
                    json.dump(data, file, indent = 4)
                set_settings()
            else:
                print('ПОМИЛКА: Стався якийсь збій та/або ви ввели неправильне значення!\nПриймається лише цілі числа від 1 до 2.\n\n')
                set_settings()
        
        answer = input('> ')
        if answer == '1':
            set_path()
        elif answer == '2':
            set_encoding()
        elif answer == '3':
            settings()
        else:
            print('ПОМИЛКА: Стався якийсь збій та/або ви ввели неправильне значення!\nПриймається лише цілі числа від 1 до 3.\n\n')
            set_settings()
    
    if answer == '1':
        get_settings()
    elif answer == '2':
        set_settings()
    elif answer == '3':
        search()
    else:
        print('ПОМИЛКА: Стався якийсь збій та/або ви ввели неправильне значення!\nПриймається лише цілі числа від 1 до 3.\n\n')
        settings()
    
            
def main():
    start()

if __name__ == '__main__':
    main()
