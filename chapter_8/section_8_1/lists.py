# Chapter 8 - Lists
# 8.1 A list is a sequence

# File: lists.py
# Description - How to declare a list and access list elements.
# A list is a sequence of values. The values in list are called elements or sometimes items.

# Example 1 - A List of Strings
# Creates a new list object and assigns the name cheeses to the list object
# and adds three string elements to the list.
cheeses = ['Cheddar', 'Edam', 'Gouda']
# Prints the list saved in the variable called cheeses
print("This is a list of strings:", cheeses)

# Example 2 - A List of Integers
# Creates a new list object and assigns the name numbers to the list object
# and adds four integer elements to the list.
numbers = [10, 20, 30, 40]
# Prints the list saved in the variable called numbers
print("This is a list of integers:", numbers)

# Example 3 - An empty list
# Creates a new list object and assigns the name empty to the list object
# A list that contains no elements is called an empty list.
# We can create one with empty brackets, [].
empty = []
# Prints the list saved in the variable called numbers
print("This is an empty list:", empty)

# Example 4 - Print 3 lists at once in the console
print(cheeses, numbers, empty)