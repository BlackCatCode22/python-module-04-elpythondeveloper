# Chapter 8 - Lists
# 8.10 Parsing lines

# File: search5.py
# Description - This program looks for lines where the line starts with From,
# and uses the split method to split those lines, and then print out the third word in the line.
#
# Reference:
# built-in functions
# https://docs.python.org/3/tutorial/datastructures.html
# https://docs.python.org/3/library/functions.html
# https://www.w3schools.com/python/ref_string_split.asp

# Open the file named mbox-short.txt in read mode and then assign the file handle to the variable called fhand.
fhand = open('mbox-short.txt')
# ----- for loop -----
# This loop iterates through each line in the file.
for line in fhand:
    # Remove any trailing whitespace from the current line
    # then assign the cleaned line back to the line variable.
    line = line.rstrip()
    # If the line does not start with From skip to the next iteration of the loop.
    if not line.startswith('From '): continue
    # Split the line into a list of words, using whitespace as the delimiter,
    # and then assign the resulting list to the variable called words.
    words = line.split()
    # Print the element at index 2 of the 'words' list (the third word in the line).
    print(words[2])
# ----- for loop -----