#!/usr/bin/env python
from backend import get_filelist, mk_dir,horizontal_pixels
import os
import shutil


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

