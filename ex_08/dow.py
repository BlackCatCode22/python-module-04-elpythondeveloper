# Chapter 8 - Lists
# ex_08
# File: dow.py
# Description

# Opens the file named mbox-short.txt in read mode and assigns the file object to the variable called han.
han = open('mbox-short.txt')

#Example 2 - using or statement in the guardian if statement
# ----- for loop -----
# loops through every line in the file
for line in han:
    # use rstrip to strip the characters on the right side such as new line character or whitespace
    line = line.rstrip()
    #print('Line:',line)
    # if line == '' :
    #     print('Skip Blank')
    #     continue
    # splits the line into words using the split function
    wds = line.split()
    #print('Words:',wds)
    # guardian in a compound statement
    if len(wds) < 3 or wds[0] != 'From' :
        continue
    # check if the first word in the line is From
    if wds[0] != 'From' :
        #print('Ignore')
        # if the first word in the line is not From then continue to the next iteration of the loop
        continue
    # as the loop iterates through each line then print the following
    # if the first word in the line is From then we print the third word in the line
    print(wds[2])
# ----- for loop -----


# # Example 1
# # ----- for loop -----
# # loops through every line in the file
# for line in han:
#     # use rstrip to strip the characters on the right side such as new line character or whitespace
#     line = line.rstrip()
#     #print('Line:',line)
#     # if line == '' :
#     #     print('Skip Blank')
#     #     continue
#     # splits the line into words using the split function
#     wds = line.split()
#     #print('Words:',wds)
#     # guardian a bit stronger
#     # if the length of the words is less 3 then continue
#     if len(wds) < 3 :
#         continue
#     # check if the first word in the line is From
#     if wds[0] != 'From' :
#         #print('Ignore')
#         # if the first word in the line is not From then continue to the next iteration of the loop
#         continue
#     # as the loop iterates through each line then print the following
#     # if the first word in the line is From then we print the third word in the line
#     print(wds[2])
# # ----- for loop -----