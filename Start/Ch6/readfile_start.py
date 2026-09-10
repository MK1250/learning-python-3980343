#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#

    
# Open the file and read the contents
sample_file = open("textfile.txt", "r")
if sample_file.mode == 'r':
    # use the read() function to read the entire file
    # contents  = sample_file.read()
    # print(contents)
    fileLines = sample_file.readlines()
    for line in fileLines:
        print(line)
sample_file.close()