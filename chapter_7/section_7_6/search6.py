# Chapter 7 - Files
# 7.6 Letting the user choose the file name

# File: search6.py
# Description - Ask user to enter a file name
# and then use a for loop to search for subject lines in the input text file.

# Display a message for the user and save the input in a variable called fname
fname = input('Enter the file name: ')
# open the file name stored in variable fname
fhand = open(fname)
# Declare and initialize variable count with zero
count = 0
# ----- for loop -----
# We use the file handle as the sequence in our for loop.
# Iterate through each line in the file.
for line in fhand:
    # if the line starts with the text Subject: then add one to count
    if line.startswith('Subject:'):
        count = count + 1
# ----- for loop -----

# Print the line and display the cound and name of the text file
print('There were', count, 'subject lines in', fname)
