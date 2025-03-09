# Chapter 8 - Lists
# 8.9 Lists and strings

# File: lists_and_strings.py
# Description - Using built-in functions with lists
# Reference:
# A string is a sequence of characters and a list is a sequence of values, but a list
# of characters is not the same as a string. To convert from a string to a list of
# characters, you can use list
# built-in functions
# https://docs.python.org/3/tutorial/datastructures.html
# https://docs.python.org/3/library/functions.html
# https://docs.python.org/3/library/functions.html#func-list

# Example 1 - Convert a string to a list
# Create a string variable and assign it the value spam
s = 'spam'
# Convert the string stored in variable s into a list of individual characters
# and assign the resulting list to the variable called t.
t = list(s)
print("----- Example 1 - Convert a string to a list -----")
# print the value stored in variable t which is a list because string s got converted to a list
print("This is the list stored in variable t: ", t)
print("----- Example 1 - Convert a string to a list -----")

# Example 2 - Break a string into words using the split method.
# Initialize a string variable called s and save a string into it.
s = 'pining for the fjords'
print("----- Example 2 - Break a string into words using split method -----")
print("This is the original string that I will split into words: ",s)
# Split the string s into a list of words, using whitespace as the delimiter,
# and assign the resulting list to the variable called t.
# Once we have split a string into a list of words, we can use the
# index operator (square bracket) to look at a particular word in the list.
t = s.split()
# print the value stored in variable t
print("This is the a list of words after splitting the string: ",t)
print("----- Example 2 - Break a string into words using split method -----")

# Example 3 - Break a string into words using the split method and a hyphen as a delimiter.
# We can call split with an optional argument called a delimiter that specifies
# which characters to use as word boundaries. This example uses a hyphen as a delimiter.
# Initialize a string variable called s and save a string with hyphens into it.
s = 'spam-spam-spam'
delimiter = '-'
print("----- Example 3 - Break a string into words using split method and a hyphen delimiter -----")
print("This is the original string that I will split into words: ",s)
x = s.split(delimiter)
# print the value stored in variable x
print("This is the a list of words after splitting the string with the hyphen delimeter: ",x)
print("----- Example 3 - Break a string into words using split method and a hyphen delimiter -----")

# Example 4 - Use join to concatenate a list of strings
# join is the inverse of split. It takes a list of strings and concatenates the elements.
# join is a string method, so we have to invoke it on the delimiter and pass the list as a parameter.

# Initialize a string variable called t and save a string list into it.
t = ['pining', 'for', 'the', 'fjords']
# Create a string variable named delimiter and assign it a space character ' '.
delimiter = ' '
print("----- Example 4 - Use join to concatenate a list of strings -----")
print("This is the list of strings I will be concatenating into one string: ",t)
# Use the join method of the string delimiter to concatenate the elements of the list t
# into a single string. Each element is separated by the space delimiter.
# The resulting string is created, but it's not stored in a variable or printed.
print("This is the concatenated list of strings as one single string: ",delimiter.join(t))
print("----- Example 4 - Use join to concatenate a list of strings -----")