# Chapter 8 - Lists
# 8.2 Lists are mutable

# File: mutable_lists.py
# Description - How to declare a list and access list elements.
# A list is a sequence of values. The values in list are called elements or sometimes items.
# Reference:
# The syntax for accessing the elements of a list is the same as for accessing the
# characters of a string: the bracket operator. The expression inside the brackets
# specifies the index. The indices start at 0.
# Unlike strings, lists are mutable because we can change the order of items
# in a list or reassign an item in a list.

# Example 1 - A List of Integers
# Creates a new list object and assigns the name numbers to the list object
# and adds two integer elements to the list.
numbers = [17, 123]
# Modifies the element at index 1 (the second element) of the numbers list
# changing its value from 123 to 5.
numbers[1] = 5
# Prints the list saved in the variable called numbers
print("This is a list of integers:", numbers)

# Example 2 - Using in operator with a list
# Creates a new list object and assigns the name cheeses to the list object
# and adds three string elements to the list.
cheeses = ['Cheddar', 'Edam', 'Gouda']
# Check if the string Edam is present within the cheeses list.
# If the string Edam is present in the list, then this line evaluates to True
# If the string Edam is not present in the list, then this line evaluates to False
'Edam' in cheeses
# Prints the list saved in the variable called cheeses
print("This is the cheeses list:", cheeses)
print("Is the string Edam present in the cheeses list?", 'Edam' in cheeses)