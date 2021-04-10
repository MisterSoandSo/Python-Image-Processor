#!/usr/bin/env python

import os, sys
import urllib.request
import config

# Create folder if it does not exist in the directory and return path
def mk_dir(parent_dir, directory):
    path = os.path.join(parent_dir, directory)
    print("Downloading path: ", path)
    
    if not os.path.exists(path):
        os.makedirs(path)
    return path

# Download images from directory if you know the link
def download_batch(ulink, directory,num_Images,i_type):
    path = mk_dir(os.getcwd(), directory)
    url_Img_LINK = ulink + directory+"/"
    print("Downloading from: ", url_Img_LINK)
    
    for x in range(num_Images):
        image_Name = str(x+1) 
        if x<9:
            file_Name = path +"/"+ str(0) +image_Name + i_type
        else:
            file_Name = path +"/"+ image_Name + i_type
        try:
            urllib.request.urlretrieve(url_Img_LINK + image_Name + i_type, file_Name)
        except:
            pass
     
    print("Finished Downloading ...")

if __name__ == "__main__":
    image_Format = ['.jpg','.png','.gif']
    if len(sys.argv) >3:
        # System Arguments:
        link_cfg = config.config.get('link'+ sys.argv[1])
        directory = sys.argv[2]
        num_Images = int(sys.argv[3])
        i_Type = image_Format[0] #default value
        if len(sys.argv) >4:
            i_Type = image_Format[int(sys.argv[4])]
            
        #Execute Command:
        download_batch(link_cfg, directory,num_Images,i_Type)
        
    else:
        print("Cannot execute: Not enough arguments.")





