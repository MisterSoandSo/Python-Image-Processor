import os
import glob
from PIL import Image
import shutil
import random

DEBUG = True

# Recursively read in all folders in current directory and return list of file locations
def get_filelist():
    file_list = []
    for filename in glob.iglob('**/*.jpg', recursive=True): 
        file_list.append(filename)
    if DEBUG == True: print("Number of files loaded: ",len(file_list))
    return file_list

# Create folder if it does not exist in the directory and return path
def mk_dir(parent_dir, directory):
    path = os.path.join(parent_dir, directory)
    if not os.path.exists(path):
        os.makedirs(path)
    return path

# Copy all all files in list to destination
def cp_files(cp_list,file_list, dest):
    
    for index in cp_list:
        filename = "RImage" + str(index) + ".jpg"
        path = os.path.join(dest, filename)
        shutil.copy(file_list[index], path)

if __name__ == "__main__":
    file_list = get_filelist()
    randomIndex = random.sample(range(len(file_list)), 3000)
    cp_files(randomIndex, file_list, mk_dir(os.getcwd(),"RandSelect"))
