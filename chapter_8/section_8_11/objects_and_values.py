# Chapter 8 - Lists
# 8.11 Objects and values

# File: objects_and_values.py
# Description - This program looks for lines where the line starts with From,
# and uses the split method to split those lines, and then print out the third word in the line.
#
# Reference:
# built-in functions
# https://docs.python.org/3/tutorial/datastructures.html
# https://docs.python.org/3/library/functions.html
# https://www.w3schools.com/python/ref_string_split.asp

# Example 1 - Use the is operator to Check whether two strings refer to the same object.
print("----- Example 1 - Check two strings -----")
a = 'banana'
b = 'banana'
# Check if the variables a and b refer to the exact same object in memory using the is operator.
# Evaluates to True if and only if a and b refer to the exact same object in memory.
print("string stored in variable a is: ", a)
print("string stored in variable b is: ", b)
print("Do they refer to the same object in memory?: ", a is b)
print("----- Example 1 - Check two strings -----")

# Example 2 - Use the is operator to Check whether two lists of integers refer to the same object.
print("----- Example 2 - Check two lists of integers -----")
a = [1, 2, 3]
b = [1, 2, 3]
# Check if the variables a and b refer to the exact same object in memory using the is operator.
# Evaluates to True if and only if a and b refer to the exact same object in memory.
# If two objects are identical, they are also equivalent,
# but if they are equivalent, they are not necessarily identical.
print("The list of integers stored in variable a is: ", a)
print("The list of integers stored in variable b is: ", b)
print("Do they refer to the same object in memory?: ", a is b)
print("----- Example 2 - Check two lists of integers -----")