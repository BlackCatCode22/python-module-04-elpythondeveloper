# Chapter 7 - Files
# 7.11 Exercises

# File: ex_07_01.py
# Description - Write a program to read through a file and print the contents
# of the file (line by line) all in upper case. Executing the program will
# look as follows:
#
# python shout.py
# Enter a file name: mbox-short.txt
# FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN 5 09:14:16 2008
# RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
# RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
# BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
# SAT, 05 JAN 2008 09:14:16 -0500

# Opens the file named mbox-short.txt in read mode and assigns the file object to the variable called fh.
fh = open('mbox-short.txt')
# Print the file handle save in fh.
# This prints information about the file object, not the file's contents.
#print(fh)

# ----- for loop -----
# loops through every line in the file
for lx in fh:
    # use rstrip to strip the characters on the right side such as new line character
    ly = lx.rstrip()
    # as the loop iterates through each line the line is printed
    # using the upper() method to make all the characters in the line Upper Case
    print(ly.upper())
# ----- for loop -----
