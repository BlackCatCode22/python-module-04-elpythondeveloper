# Chapter 8 - Lists
# 8.13 List arguments

# File: list_arguments.py
# Description - Use a function called delete_head to remove the first element from a list
# When you pass a list to a function, the function gets a reference to the list.
# If the function modifies a list parameter, the caller sees the change.

# A function named delete_head that takes one argument
# The argument is called t, it will be a list.
def delete_head(t):
    # Delete the element at index 0 from the list t (remove the first element of the list).
    del t[0]

# Initialize a string variable called letter and save a string list into it.
letters = ['a', 'b', 'c']
# Call a function named delete_head and pass the letters list as an argument.
delete_head(letters)
# print the value stored in variable letters
print(letters)