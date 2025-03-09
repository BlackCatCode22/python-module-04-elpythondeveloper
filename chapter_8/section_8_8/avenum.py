# Chapter 8 - Lists
# 8.8 Lists and functions

# File: avenum.py
# Description - Using a while loop to get values from a user and then compute the average.
# Output:
# Enter a number: 34
# Enter a number: 67
# Enter a number: done
# Average: 50.5

# initialize a variable called total with 0
total = 0
# initialize a variable called count with 0
count = 0
# ----- while loop -----
# an infinite loop that continues until the user enters done
while (True):
    # Prompt the user to enter a number and store the input as a string in the variable called inp.
    inp = input('Enter a number: ')
    # If the user inputs done then break out of the loop.
    if inp == 'done': break
    # Convert the input string to a floating-point number and store it in the variable called value
    value = float(inp)
    # Add the value input to the value stored in variable total
    total = total + value
    # Add one to the value stored in variable count
    count = count + 1
# ----- while loop -----
# ----- display output -----
# Calculate average by dividing total by count. The result is a floating-point number and is saved in average.
average = total / count
print('Average:', average)
# ----- display output -----

