import os
import re
import sys

try:
    command = str(sys.argv[1])
    path_to_group = command
except IndexError:
    path_to_group = os.getcwd()

file_names = []
dir_names = []
FILE_CATEGORIES = {
    'videos':('.mp4', '.avi', '.mkv'),
    'images':('.jpeg', '.jpg', '.png', '.svg', '.gif' ),
    'documents':('.pdf', '.docx', '.txt', ),
    'executables':(),
    'compressed':(),
    'audios':(),
    'others':(),
}

def get_file_category(ext):
    for category, extensions in FILE_CATEGORIES.items():
        if (ext in extensions):
            return category
    return 'others'
        
for (dirpath, dirnames, filenames) in os.walk(path_to_group):
    file_names.extend(filenames)
    dir_names.extend(dirnames)

for file in file_names:
    file_name, file_extension = os.path.splitext(file)
    category=''
    if (file_extension):
        if (file_extension == ".py"):
            continue
        category = get_file_category(file_extension)
    else:
        continue
    
    if not (category in dir_names):
        os.mkdir(category)
        dir_names.append(category) #This line prevents the code from trying to create a directory that was just created
    # Put different os into consideration when user wants to organize files of another directory
    # that isn't the cwd. NB:split into list by '/' or '\'
    old_file_path = os.path.join(path_to_group,file)
    new_file_path = os.path.join(path_to_group, category, file)
    os.replace(old_file_path, new_file_path)
    
