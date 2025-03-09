# Chapter 8 - Lists
# 8.4 List operations

# File: list_operations.py
# Description - How to use operators with lists.
# Reference:
# The + operator concatenates lists.
# the * operator repeats a list a given number of times.

# Example 1 - Using the + operator
# This example shows how to concatenate two lists using the + operator
#
# Create a list named a and initialize it with the integers 1, 2 and 3.
a = [1, 2, 3]
# Create a list named b and initialize it with the integers 4, 5 and 6.
b = [4, 5, 6]
# Concatenate the lists a and b, creating a new list that is saved in variable c
# The new list contains all the elements of a followed by all the elements of b.
c = a + b
print("---------- Example 1 ----------")
print("This Example 1 list a:", a)
print("This Example 1 list b:", b)
# Prints the list saved in the variable called c
print("When I concatenate list a and b this is the new list:", c)
print("---------- Example 1 ----------")

# Example 2 - Using the * operator to repeat a list 4 times
# This example shows how to repeat a list using the * operator
#
# Create a list named list2 and initialize it with the integer 0.
list2 = [0]
# Using the * operator to repeat the list 4 times and save the new list in a variable called x
#[0] * 4
x = list2 * 4
print("---------- Example 2 ----------")
print("This Example 2 list2:", list2)
# Prints the list saved in the variable called x
print("This is the list2 repeated 4 times:", x)
print("---------- Example 2 ----------")

# Example 3 - Using the * operator to repeat a list 3 times
# This example shows how to repeat a list using the * operator
#
# Create a list named list3 and initialize it with the integers 1, 2 and 3.
list3 = [1,2,3]
# Using the * operator to repeat the list 3 times and save the new list in a variable called y
# [1, 2, 3] * 3
y = list3 * 3
print("---------- Example 3 ----------")
print("This Example 3 list3:", list3)
# Prints the list saved in the variable called y
print("This is the list3 repeated 3 times:", y)
print("---------- Example 3 ----------")