# count number of folders and files in given directory
import os
total_files = 0
total_dirs = 0

os.chdir('D:\\new_ex_folder_by_py')

current_folder = os.getcwd()
for root, folders, files in os.walk(current_folder):
    total_dirs += len(folders)
    total_files += len(files)

print(f"Total folders :- {total_dirs} \n Total Files :- {total_files} \n Total :- {total_dirs + total_files}")
