import os
import shutil

# Define the source directory and file type-based target directories
SOURCE_DIR = r'C:\Users\user\Desktop\pythonproject1'
TARGET_DIRS = {
    'Images': ['jpg', 'jpeg', 'png', 'gif'],
    'Documents': ['pdf', 'docx', 'txt'],
    'Music': ['mp3', 'wav'],
    'Videos': ['mp4', 'mov', 'avi'],
    'Archives': ['zip', 'rar', 'tar']
}

# Function to create target directories if they don't exist
def create_directories():
    for folder in TARGET_DIRS:
        folder_path = os.path.join(SOURCE_DIR, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

# Function to organize files by type
def organize_files():
    for filename in os.listdir(SOURCE_DIR):
        file_path = os.path.join(SOURCE_DIR, filename)
        if os.path.isfile(file_path):
            file_extension = filename.split('.')[-1].lower()
            moved = False

            # Check the file type and move it to the appropriate folder
            for folder, extensions in TARGET_DIRS.items():
                if file_extension in extensions:
                    target_folder = os.path.join(SOURCE_DIR, folder)
                    shutil.move(file_path, target_folder)
                    print(f"Moved: {filename} -> {folder}")
                    moved = True
                    break

            # Optionally, move unknown types to an "Others" folder
            if not moved:
                other_folder = os.path.join(SOURCE_DIR, 'Others')
                if not os.path.exists(other_folder):
                    os.makedirs(other_folder)
                shutil.move(file_path, other_folder)
                print(f"Moved: {filename} -> Others")

if __name__ == "__main__":
    create_directories()
    organize_files()
