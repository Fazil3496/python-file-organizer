import os
import shutil

folder_path = r"C:\Users\fazzi\Downloads"

file_types = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Videos": [".mp4", ".mkv"],
    "Documents": [".pdf", ".txt", ".docx"],
}

for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):
        for folder, extensions in file_types.items():
            if file.endswith(tuple(extensions)):
                new_folder = os.path.join(folder_path, folder)

                if not os.path.exists(new_folder):
                    os.makedirs(new_folder)

                shutil.move(file_path, os.path.join(new_folder, file))
                print(f"Moved {file} to {folder}")