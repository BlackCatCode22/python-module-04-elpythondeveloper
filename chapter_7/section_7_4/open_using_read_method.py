# Chapter 7 - Files
# 7.4 Reading files

# File: open_using_read_method.py
# Description - Using the read method to open a file.

# Opens the file named mbox-short.txt in read mode and assigns the file object to the variable called fhand.
fhand = open('mbox-short.txt')
# the entire contents (all 94,626 characters) of the file mbox-short.txt
# are read directly into the variable called inp
inp = fhand.read()
# Use the len function to get the number of characters stored in variable inp.
# Print the number of characters returned by the len function.
print("The file mbox-short.txt contains ",len(inp), " characters.")
# We use string slicing to print out the first
# 20 characters of the string data stored in variable inp.
print("The first 20 characters in the string inside of mbox-short.txt are: ",inp[:20])