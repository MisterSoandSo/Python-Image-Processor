#!/usr/bin/env python
from backend import get_filelist, mk_dir,cp_files
import os
import random

if __name__ == "__main__":
    numImage = 3000
    file_list = get_filelist()
    print(len(file_list))
    randomIndex = random.sample(range(len(file_list)), numImage)
    print("Number of random images selected:", numImage)
    cp_files(randomIndex, file_list, mk_dir(os.getcwd(),"RandSelect"))
