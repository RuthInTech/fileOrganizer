import os
import shutil
folder_path= input("Enter your folder path to be organized: ")
files= os.listdir(folder_path)


for f in files:
    print(f)

file_types= {
    "Images": [".jpg", ".png", ".gif" ],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
}
# loop through files
for file in files:
    file_path= os.path.join(folder_path, file)
    if os.path.isfile(file_path):
        ext= os.path.splitext(file)[1].lower()
        moved= False
        for folder, extension in file_types.items():
            if ext in extension:
                dest_folder= os.path.join(folder_path, file)
            if not os.path.exists(dest_folder):
                os.mkdir(dest_folder)
            shutil.move(file_path, dest_folder)
            print(f"Moved {file}-> {folder}")
            moved=True
            break
        if not moved:
            print(f"No folder defined for {file}, skipping.....")









