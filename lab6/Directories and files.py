import os

def list_directories_and_files(path):
    directories = []
    files = []
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            directories.append(item)
        else:
            files.append(item)
    return directories, files

path = "C:\Users\ASUS\Desktop\path"
directories, files = list_directories_and_files(path)
print("Directories:", directories)
print("Files:", files)


import os

def check_access(path):
    access = {
        'exists': os.path.exists(path),
        'readable': os.access(path, os.R_OK),
        'writable': os.access(path, os.W_OK),
        'executable': os.access(path, os.X_OK)
    }
    return access

path = "C:\Users\ASUS\Desktop\path"
access = check_access(path)
print(access)



import os

def test_existence_and_get_parts(path):
    if os.path.exists(path):
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        return filename, directory
    else:
        return "Path does not exist", None

path ="C:\Users\ASUS\Desktop\path"
filename, directory = test_existence_and_get_parts(path)
print("Filename:", filename)
print("Directory:", directory)



def count_lines(file_path):
    with open(file_path, 'r') as file:
        return sum(1 for line in file)

file_path = "C:\Users\ASUS\Desktop\path"
print("Number of lines:", count_lines(file_path))


def write_list_to_file(file_path, data):
    with open(file_path, 'w') as file:
        for item in data:
            file.write(str(item) + '\n')

file_path = "C:\Users\ASUS\Desktop\path"
data = ['apple', 'banana', 'cherry', 'date']
write_list_to_file(file_path, data)


import string

def generate_text_files():
    for letter in string.ascii_uppercase:
        file_name = letter + '.txt'
        with open(file_name, 'w') as file:
            pass  

generate_text_files()



def copy_file(source_file, destination_file):
    with open(source_file, 'r') as source:
        with open(destination_file, 'w') as destination:
            for line in source:
                destination.write(line)

source_file = '"C:\Users\ASUS\Desktop\path.txt.docx"'
destination_file = "C:\Users\ASUS\Desktop\path"
copy_file(source_file, destination_file)



import os

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        return "File deleted successfully"
    else:
        return "File does not exist"

file_path = "C:\Users\ASUS\Desktop\path"
print(delete_file(file_path))






