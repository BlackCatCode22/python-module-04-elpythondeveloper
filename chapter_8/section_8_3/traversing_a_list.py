# Chapter 8 - Lists
# 8.3 Traversing a list

# File: traversing_a_list.py
# Description - How to declare a list and access list elements.
# A list is a sequence of values. The values in list are called elements or sometimes items.
# Reference:
# The most common way to traverse the elements of a list is with a for loop.
# The syntax is the same as it is done for strings.

# Example 1 - Traversing the Cheese List
# This example shows how to traverse a list with a for loop
#
# Creates a new list object and assigns the name cheeses to the list object
# and adds three string elements to the list.
cheeses = ['Cheddar', 'Edam', 'Gouda']
# ----- for loop -----
# Start a for loop that iterates through each element in the cheeses list,
# assigning each element to the variable cheese in each iteration.
for cheese in cheeses:
    # Print the current value of the cheese variable,
    # which represents an element from the cheeses list.
    print(cheese)
# ----- for loop -----

# Example 2 - Use the range and len functions with a List of Integers
# This example using the range and len functions and the indices of a list to update elements in the list.
#
# Creates a new list object and assigns the name numbers to the list object
# and adds two integer elements to the list.
# Create a list named numbers and initialize it with the integers 17 and 123.
numbers = [17, 123]
# ----- for loop -----
# Start a for loop that iterates through a sequence of numbers from 0 up to
# (but not including) the length of the numbers list.
# The current index is assigned to the variable i in each iteration.
for i in range(len(numbers)):
    # Multiply the element at index i in the numbers list by 2,
    # and then assign the result back to the same element. This doubles each element in the list.
    numbers[i] = numbers[i] * 2
    # Print the modified element at index i of the numbers list,
    # which now holds the doubled value.
    # The print statement executes before the loop moves on to the next iteration.
    # The loop only ends after the print statement has executed for the final item in the list.
    print(numbers[i])
# ----- for loop -----

