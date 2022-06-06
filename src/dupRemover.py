#!/usr/bin/env python
from backend import get_filelist
import hashlib
import os

# Read the file in binary and  returned as a string object of double length, containing only hexadecimal digits. 
# If hash does not exist, add into hash_keys. If exist, add index of file onto duplicates
def find_duplicates(file_list, cur_dir,DEBUG=False):
    duplicates = []
    hash_keys = dict()
    for index, filename in  enumerate(file_list): 
        if os.path.isfile(filename):
            with open(filename, 'rb') as f:
                filehash = hashlib.md5(f.read()).hexdigest()
            if filehash not in hash_keys: 
                hash_keys[filehash] = index
            else:
                duplicates.append((index,hash_keys[filehash]))

    if DEBUG == True:
        print("Number of duplicates: ", len(duplicates)) 

    for index in duplicates:
        os.remove(file_list[index[0]])
    
    print("Duplicates in: ", cur_dir , " processed!")


if __name__ == "__main__":
    find_duplicates(get_filelist(), os.getcwd())  


