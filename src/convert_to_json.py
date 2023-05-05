import json
import os

directory_path = "text" 

def get_key_value(line: str) -> tuple:
    key, _, value = line.partition(" = ")
    return key.strip(), value.strip()

for filename in [f for f in os.listdir(directory_path) if f.endswith(".txt")]:
    file_path = os.path.join(directory_path, filename)
    filename = os.path.splitext(filename)[0]
    print(filename)
    with open(file_path, "r", encoding='utf-8') as file, \
         open(f'done/{filename}.json', 'w', encoding="utf-8") as json_file:
        data = {}
        for line in file:
            line = line.strip()
            if line:
                key, value = get_key_value(line)
                print(f'{filename} | {key} | {value}')
                data[(filename, key)] = {key: value}
        json.dump(data, json_file, indent=4, ensure_ascii=False)

print("Готово")
