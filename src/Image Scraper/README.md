# Image Scrapper
A Python 3.7 webscrapper script that grabs images from specfic websites. It is designed with a config file to handle multiple webhost links.

# DISCLAIMER
This code was built as an academic exercise. The code provides examples on how to webscrap for images in a controlled setting. I am not responsible for deviations of this code and how it is used outside the scope of what it was intended for.

## Usage Instruction
1. Fill in links that you wish to use in the `<config-template.py>` and rename it to `<config.py>`
2. To use this script, put the code inside the directory that you plan to use and run the following command: `<python img_Batch.py <Link Number> <Directory> <Number of Images> <Image Type>>`
	- Link Number: based off the index number of config file content
	- Directory: the directory address of image storage folder
	- Number of Images: number images to download
	- Image Type: default to 0 if no argument given. ['.jpg','.png','.gif']
3. Wait for images to finish downloading.

## Dependency
	- urllib

## Bugs 
	- 
