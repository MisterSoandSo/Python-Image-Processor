#!/usr/bin/env python

import os, sys
import glob
import shutil
from PIL import Image

DEBUG = True

# Recursively read in all folders in current directory and return list of file locations
def get_filelist():
    file_list = []
    for filename in glob.iglob('**/*.jpg', recursive=False): 
        file_list.append(filename)
    if DEBUG == True: print("Number of files loaded: ",len(file_list))
    return file_list

# Create folder if it does not exist in the directory and return path
def mk_dir(parent_dir, directory):
    path = os.path.join(parent_dir, directory)
    if not os.path.exists(path):
        os.makedirs(path)
    return path

# Return true or false on width greater than height
def horizontal_pixels(filepath):
    try:
        width, height = Image.open(filepath).size
        return width>height
    except IOError:
        pass

#Find out whether the image is portait or landscape in current directory
def orientation():
    file_list = get_filelist()
    vertical = []
    horizontal = []
    counter_v = 0
    counter_h = 0
    
    for index, filename in  enumerate(file_list):  
        if horizontal_pixels(filename):
            horizontal.append(index)
            counter_h += 1
        else:
            vertical.append(index)
            counter_v += 1
    print("Number of portait photos found: ", counter_v)
    print("Number of landscape photos found: ", counter_h)

    if counter_v > 0:
        path = mk_dir(os.getcwd(),"Vertical")   
        for index in vertical:
            shutil.move(file_list[index], path)
    if counter_h > 0:
        path = mk_dir(os.getcwd(),"Horizontal")   
        for index in horizontal:
            shutil.move(file_list[index], path)

if __name__ == "__main__":
    orientation()

