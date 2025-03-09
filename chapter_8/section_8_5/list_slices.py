# Chapter 8 - Lists
# 8.5 List slices

# File: list_slices.py
# Description - Using the slice operator to slice a list.
# Reference:
# If you omit the first index, the slice starts at the beginning.
# If you omit the second, the slice goes to the end.
# If you omit both, the slice is a copy of the whole list.
# Since lists are mutable, it is often useful to make a copy before performing operations
# that fold, spindle, or mutilate lists.

# Example 1 - Using the slice operator to slice a string list, using first and second index
# Create a list named t and initialize it with the strings a, b, c, d, e and f
t = ['a', 'b', 'c', 'd', 'e', 'f']
# Print a string literal followed by a slice of the list t.
# The slice t[1:3] extracts elements from index 1 (inclusive) up to index 3 (exclusive),
# So this prints elements b, c
print("---------- Example 1 ----------")
print("Example 1 sliced list:", t[1:3])
print("---------- Example 1 ----------")

# Example 2 - Using the slice operator to slice a string list, omitting the first index
print("---------- Example 2 ----------")
# If we omit the first index, the slice starts at the beginning.
# This gets all the elements from the beginning of all the way to the element with index 4 (exclusive)
# So this prints elements a, b, c, d
print("Example 2 sliced list:", t[:4])
print("---------- Example 2 ----------")

# Example 3 - Using the slice operator to slice a string list, omitting the second index
print("---------- Example 3 ----------")
# If we omit the second index, the slice goes to the end.
# This gets all the elements from index 3 (inclusive) up to the end
# So this prints elements d, e, f
print("Example 3 sliced list:", t[3:])
print("---------- Example 3 ----------")