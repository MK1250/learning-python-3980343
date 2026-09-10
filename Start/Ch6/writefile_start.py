# LinkedIn Learning Python course by Joe Marini
# write files using the built-in Python file methods


# Open a file for writing and create it if it doesn't exist
sample_file = open("textfile.txt", "w+")
sample_file.write("This is a text for the sample file\n")
sample_file.close()

# Open the file for appending text to the end
# if file is oppened in write mode, it will overwrite the existing file
sample_file = open("textfile.txt", "a+")
sample_file.write("additional data appended onto the file\n")

# write some lines of data to the file


# close the file when done
sample_file.close()
