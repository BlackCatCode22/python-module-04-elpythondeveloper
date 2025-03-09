# Chapter 7 - Files
# 7.5 Searching through a file

# File: search3.py
# Description - Read a file and only print out lines which started with the prefix From:
# Use the rstrip method which strips whitespaces from the right side of a string
# Use continue to skip uninteresting lines
# ----------
# rstrip method
# https://docs.python.org/3/library/stdtypes.html#string-methods
# Returns a copy of the string with trailing characters removed.
# ----------

# Opens the file named mbox-short.txt in read mode and assigns the file object to the variable called fhand.
fhand = open('mbox-short.txt')
# ----- for loop -----
# We use the file handle as the sequence in our for loop.
# Iterate through each line in the file.
for line in fhand:
    # remove the trailing characters from the line
    line = line.rstrip()
    # Check a line in the text file,
    # if it starts with From: do the stuff in if statement
    # If not then continue skips the line and start the next iteration of the loop
    if not line.startswith('From:'):
         continue
    # Print the line that starts with From
    print(line)
# ----- for loop -----