import glob
import os
import shutil
import time
import random

from PIL import Image

# Recursively read in all folders in current directory and return list of file locations
def get_filelist(DEBUG = False):
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

# Copy all files in list to destination
def cp_files(cp_list,file_list, dest):
    ofname = dest + "/original_file_loc_"+ str(time.time()) + ".txt"
    file = open(ofname,"w") 
    for index in cp_list:
        filename = "RImage" + str(index) + ".jpg"
        path = os.path.join(dest, filename)
        file.write("R" + str(index) + ": original source file: " + file_list[index] + "\n") 
        shutil.copy(file_list[index], path)
    file.close()

# Return true or false on width greater than height
def horizontal_pixels(filepath):
    try:
        width, height = Image.open(filepath).size
        return width>height
    except IOError:
        pass