# Python Image Processor - dupRemover
The script find all duplicates in current directory and sub directory. It recursively read in all folders in current directory and return list of file locations that is then plugged in as binary and  returned as a string object of double length, containing only hexadecimal digits. The hash key is used to compared the images for exact duplicates.

## Usage
To use this script, put the code inside the image directory that you plan to process and ru nthe following command:
`<python dupRemover.py>`

## Install
`<pip install hashlib>`
`<pip install glob>`

## Dependency
 - hashlib
 - glob
 - os

## Bugs
 - None
