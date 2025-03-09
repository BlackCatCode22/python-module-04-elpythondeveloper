# Chapter 8 - Lists
# 8.12 Aliasing

# File: aliasing.py
# Description - This program looks for lines where the line starts with From,
# and uses the split method to split those lines, and then print out the third word in the line.
#
# Reference:
# built-in functions
# https://docs.python.org/3/tutorial/datastructures.html
# https://docs.python.org/3/library/functions.html
# https://www.w3schools.com/python/ref_string_split.asp

# Create a list named a and initialize it with the integers 1, 2, and 3.
a = [1, 2, 3]
# Assign the list a to the variable b. Now, b references the same list object as a.
b = a
# Check if a and b refer to the same object in memory using the is operator.
# This will evaluate to True because b is assigned the same list as a.
b is a

# Modify the element at index 0 of the list b to 17.
# Since a and b reference the same list, this change affects both variables.
b[0] = 17
# Print the list stored in variable a.
# The output will show the modified list [17, 2, 3].
print(a)
