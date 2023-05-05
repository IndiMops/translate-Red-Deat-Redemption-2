import os
import shutil

work_dir = "work"
original_dir = "../en_yldb"
game_dir = "done"

for file_name in os.listdir(work_dir):
    file_path = os.path.join(work_dir, file_name)
    original_file_path = os.path.join(original_dir, os.path.splitext(file_name)[0])
    if os.path.isfile(file_path) and os.path.exists(original_file_path):
        with open(os.path.join(game_dir, file_name), 'wb') as dst:
            with open(os.path.join(original_dir, os.path.splitext(file_name)[0]), 'rb') as src:
                shutil.copyfileobj(src, dst)
        os.replace(os.path.join(game_dir, file_name), os.path.join(work_dir, file_name))
        print(f"{file_name} was successfully moved to {game_dir}")
