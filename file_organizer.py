# file_organizer.py
# Automatically organizes files into folders based on their extensions.

import os
import shutil

def organize_directory(target_dir):
    if not os.path.exists(target_dir):
        print("Directory does not exist.")
        return

    for filename in os.listdir(target_dir):
        filepath = os.path.join(target_dir, filename)
        
        if os.path.isfile(filepath):
            ext = filename.split('.')[-1].lower()
            folder_name = f"{ext}_files"
            folder_path = os.path.join(target_dir, folder_name)
            
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                
            shutil.move(filepath, os.path.join(folder_path, filename))
            print(f"Moved {filename} to {folder_name}/")

if __name__ == "__main__":
    organize_directory("./my_downloads")
