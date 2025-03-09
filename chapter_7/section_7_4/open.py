# Chapter 7 - Files
# 7.4 Reading files

# File: open.py
# Description - A for loop that reads through and counts each of the lines in a file.

# Opens the file named mbox-short.txt in read mode and assigns the file object to the variable called fhand.
fhand = open('mbox-short.txt')
# Initialize a counter variable called count to 0.
count = 0
# ----- for loop -----
# We use the file handle as the sequence in our for loop.
# Iterate through each line in the file.
for line in fhand:
    # Increment the counter 'count' by 1 for each line.
    count = count + 1
# ----- for loop -----
# Print the final value stored in variable count with a descriptive label.
print('Line Count:', count)