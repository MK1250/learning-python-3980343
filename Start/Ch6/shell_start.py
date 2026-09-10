#
# Example file for working with filesystem shell methods
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path
import shutil
from zipfile import ZipFile
# make a duplicate of an existing file
# if path.exists("newfile.txt"):
#     # get the path to the file in the current directory
#     src = path.realpath("newfile.txt.txt")
        
#     # # let's make a backup copy by appending "bak" to the name
#     # dst = src + ".bak"
#     # # # now use the shell to make a copy of the file
#     # shutil.copy(src,dst)

#     # # rename the original file
#     # os.rename("newfile.txt", "newfile.txt")
    
#     # now put things into a ZIP archive
#     # root_dir, tail = path.split(src)
#     # shutil.make_archive("archive", "zip", root_dir)

#     # more fine-grained control over ZIP files
#     with ZipFile("testzip.zip", "w") as newzip:
#         newzip.write("newfile.txt")
#         newzip.write("textfile.txt.bak")



## Code Challenger: Files
# Count the size in bytes of text files in a directory

def file_info():
    # List the contents of the main path file
    items = os.listdir('.') # '.' means current directory (list of files in a directory)
    totalByte = 0

    #Iterate over each file and determine the size of each file if it is a txt file
    for item in items:
        if os.path.splitext(item)[1] == '.txt':
            full_path = os.path.join('.', item)
            # statinfo = os.stat(full_path)

            # Add the size to the total byte count if it is a text file
            totalByte += full_path

    # Return the total bytes
    print(totalByte)
