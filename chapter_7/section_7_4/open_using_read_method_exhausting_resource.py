# Chapter 7 - Files
# 7.4 Reading files

# File: open_using_read_method_exhausting_resource.py
# Description - Using the read method to open a file and showing how a read method can exhaust it's resource.

# When we use the read method to read a file. It is a good idea
# to store the output of read as a variable because
# each call to read exhausts the resource.

# Opens the file named mbox-short.txt in read mode and assigns the file object to the variable called fhand.
fhand = open('mbox-short.txt')

# Call 1
# The entire contents (all 94,626 characters) of the file mbox-short.txt are read.
# The len function gets the number of characters of the characters that are read
# The value returned by len function is printed.
# Since this is the first call using read, the characters are read.
print("Call 1 - The file mbox-short.txt contains ",len(fhand.read()), " characters.")

# Call 2
# If we try to use the read character a second time, the characters will be 0
# It's best to read the contents a file into a variable instead of calling directly.
print("Call 2 - The file mbox-short.txt contains ",len(fhand.read()), " characters.")
