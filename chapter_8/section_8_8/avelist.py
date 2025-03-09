# Chapter 8 - Lists
# 8.8 Lists and functions

# File: avelist.py
# Description - Using a while loop to get values from a user that are saved in a list and then computer average.
# Output:
# Enter a number: 24
# Enter a number: 20
# Enter a number: 28
# Enter a number: done
# Average: 24.0

# Initialize and empty list and save it in a variable called numlist
numlist = list()
# ----- while loop -----
# an infinite loop that continues until the user enters done
while (True):
    # Prompt the user to enter a number and store the input as a string in the variable called inp.
    inp = input('Enter a number: ')
    # If the user inputs done then break out of the loop.
    if inp == 'done': break
    # Convert the input string to a floating-point number and store it in the variable called value
    value = float(inp)
    # the input value is appended to the list saved in variable numlist
    numlist.append(value)
# ----- while loop -----
# ----- calculation -----
# Calculate the average of numbers input by the user.
# The sum of the values in the list stored in numlist is divided by
# the length (number of elements) in the list stored in numlist.
# The result is a floating-point number and is saved in average.
average = sum(numlist) / len(numlist)
# ----- calculation -----
# ----- display output -----
# Print the value stored in variable called average.
print('Average:', average)
# ----- display output -----