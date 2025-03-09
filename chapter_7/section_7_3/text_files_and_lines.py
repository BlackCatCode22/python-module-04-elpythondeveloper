# Chapter 7 - Files
# 7.3 Text files and lines

# File: text_files_and_lines.py
# Description - In these examples we use the new line character to display a part of a string on a new line.
# In Python, we represent the newline character as a backslash-n in string constants.

# Example 1
# Declare a string variable with a newline character in between the words Hello World!
# and save it in a variable called stuff.
stuff = 'Hello\nWorld!'
# When we print a string that has a newline character, everything after is printed on a new line.
# In this example the newline character \n causes the string World! to be printed on a new line.
print("Example 1 output: ")
print(stuff)

# Example 2
# Declare a string variable with a newline character in between
# the characters X and Y and save it in a variable called stuff.
stuff = 'X\nY'
# In this example the newline character \n causes the character Y to be printed on a new line.
print("Example 2 output: ")
print(stuff)

# # Example 3
# In this example we use the len function go get the number of characters in a string
# The len() function returns the number of items in an object.
# When the object is a string, the len() function returns the number of characters in the string.
print("Example 3 output: ")
# This example gets the number of characters in the string saved in variable stuff.
# Currently the string X\nY is saved in variable stuff. So the len function will return 3
# The value 3 representing 3 characters will be printed.
print(len(stuff))