# Chapter 7 - Files
# 7.5 Searching through a file

# File: search1.py
# Description - Read a file and only print out lines which started with the prefix From:

# For example, if we wanted to read a file and only print out lines which started with
# the prefix “From:”, we could use the string method startswith to select only those
# lines with the desired prefix

# Opens the file named mbox-short.txt in read mode and assigns the file object to the variable called fhand.
fhand = open('mbox-short.txt')
# ----- for loop -----
# We use the file handle as the sequence in our for loop.
# Iterate through each line in the file.
for line in fhand:
    # Check a line in the text file, if it starts with From: do the stuff in if statement
    if line.startswith('From:'):
        # Print the line that starts with From:
        print(line)
# ----- for loop -----