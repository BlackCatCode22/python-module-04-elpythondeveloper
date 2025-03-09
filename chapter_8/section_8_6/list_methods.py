# Chapter 8 - Lists
# 8.6 List methods

# File: list_methods.py
# Description - Using Python methods that work with a list.
# Reference:
# Python provides methods that operate on lists.
# append - adds a new element to the end of a list.
# extend - takes a list as an argument and appends all of the elements.
# sort - arranges the elements of the list from low to high.

# Example 1 - Using the append method to add an element to a list
# Create a list named t and initialize it with the strings a, b and c
t = ['a', 'b', 'c']
print("---------- Example 1 ----------")
print("before appending an element, list t looks like this:", t)
# adds a new element to list t
t.append('d')
print("after appending an element, list t now looks like this:", t)
print("---------- Example 1 ----------")

# Example 2 - Using the extend method
# Create a list named t1 and initialize it with the strings a, b and c
t1 = ['a', 'b', 'c']
# Create a list named t2 and initialize it with the strings d and e
t2 = ['d', 'e']
print("---------- Example 2 ----------")
print("before extending list t1, it looks like this:", t1)
# All the elements in the list that is saved in variable t2 get added to the list saved in variable t1
t1.extend(t2)
print("after extending list t1, it nowlooks like this:", t1)
print("---------- Example 2 ----------")

# Example 3 - Using the sort method
# Create a list named t and initialize it with the strings d, c, e, b, a
t = ['d', 'c', 'e', 'b', 'a']
print("---------- Example 3 ----------")
# before sorting list t it looks like this
print("before sorting list t looks like this:", t)
# All the elements in the list that are saved in variable t get sorted from low to high
t.sort()
print("after sorting list t now it looks like this:", t)
print("---------- Example 3 ----------")