# Chapter 8 - Lists
# 8.7 Deleting elements

# File: deleting_elements.py
# Description - Deleting elements from a list.
# Reference:
# https://docs.python.org/3/tutorial/datastructures.html
# There are several ways to delete elements from a list.
# If you know the index of the element you want, you can use pop.
# If you don’t need the removed value, you can use the del statement.
# To remove more than one element, you can use del with a slice index.
# If you know the element you want to remove (but not the index), you can use remove.

# Example 1 - Using pop method to delete an element from list
# If you know the index of the element you want, you can use pop.
# Create a list named t and initialize it with the strings a, b and c
t = ['a', 'b', 'c']
print("---------- Example 1 ----------")
print("Before deleting an element from list t, it looks like this:", t)
# Remove and return the element at index 1 from the list t.
# The removed element b is assigned to the variable x.
# pop modifies the list and returns the element that was removed.
# If you don’t provide an index, it deletes and returns the last element.
x = t.pop(1)
print("After deleting an element from list t, it now looks like this:", t)
print("This is the element that was deleted from list t:", x)
print("---------- Example 1 ----------")

# Example 2 - Using del method to delete an element from list
# If you know the element you want to remove (but not the index), you can use remove.
# Create a list named t2 and initialize it with the strings a, b and c
t2 = ['a', 'b', 'c']
print("---------- Example 2 ----------")
print("Before deleting an element from list t2, it looks like this:", t2)
print("This is the element that will be deleted from list t2:", t2[1])
# Remove  the element at index 1 from the list t2.
del t2[1]
print("After deleting an element from list t2, it now looks like this:", t2)

print("---------- Example 2 ----------")

# Example 3 - Using remove method to delete an element from list
# If you know the element you want to remove (but not the index), you can use remove.
# The return value from remove is None.
# Create a list named t3 and initialize it with the strings a, b and c
t3 = ['a', 'b', 'c']
print("---------- Example 3 ----------")
print("Before deleting an element from list t3, it looks like this:", t3)
print("This is the element that will be removed from list t2:", 'b')
# Remove  the element at index 1 from the list t3.
t3.remove('b')
print("After removing an element from list t3, it now looks like this:", t3)
print("---------- Example 3 ----------")

# Example 4 - Deleting more than one element from a list using del method with a slice index
# Create a list named t4 and initialize it with the strings a, b, c, d, e and f
t4 = ['a', 'b', 'c', 'd', 'e', 'f']
print("---------- Example 4 ----------")
print("Before deleting more than one element from list t4, it looks like this:", t4)
print("These are the elements that will be deleted from list t4:", t4[1:5])
# Delete the elements from index 1 (inclusive) to index 5 (exclusive) from the list t4.
# b has index of 1, c has index of 2, d had index of 3, e has index of 4
# This will delete elements b, c, d, e from list t4
del t4[1:5]
print("After deleting more than one element from list t4, it now looks like this:", t4)
print("---------- Example 4 ----------")