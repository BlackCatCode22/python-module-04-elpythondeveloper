# Chapter 8 - Lists
# 8.8 Lists and functions

# File: lists_and_functions.py
# Description - Using built-in functions with lists
# Reference:
# There are a number of built-in functions that can be used on lists that allow you
# to quickly look through a list without writing your own loops:
# https://docs.python.org/3/tutorial/datastructures.html
# https://docs.python.org/3/library/functions.html
# https://docs.python.org/3/library/functions.html#len
# https://docs.python.org/3/library/functions.html#max
# https://docs.python.org/3/library/functions.html#min
# https://docs.python.org/3/library/functions.html#sum
# The sum() function only works when the list elements are numbers.
# The functions max(), min(), len() work with lists of strings and other types.

# Example 1 - Using built-in functions with an integer list
#
# Create a list named nums and initialize it with the integers 3,41,12,9,74,15
nums = [3, 41, 12, 9, 74, 15]
# Prints the length (number of elements) in the list saved in variable nums.
print(len(nums))
# Print the maximum value (largest element) in the list saved in variable nums.
print(max(nums))
# Print the minimum value (smallest element) in the list saved in variable nums.
print(min(nums))
# Print the sum of all elements in the list saved in variable nums.
print(sum(nums))
# Print the average of the elements in the list saved in variable nums.
# It is calculated by dividing the sum of the elements by the length of the list.
# The answer is a floating-point number.
print(sum(nums)/len(nums))