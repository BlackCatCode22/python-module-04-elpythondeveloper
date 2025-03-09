# Chapter 7 - Files
# 7.2 Opening files

# File: opening_files.py
# Description - In this example, we open the file mbox.txt.
# mbox.txt is stored in the same folder as this program.

# When we want to read or write a file (say on your hard drive), we first must open the file.
# When we open a file, you are asking the operating system to find the file by name and make sure the file exists.
# If the open is successful, the operating system returns us a file handle.
# The file handle is not the actual data contained in the file, but instead it is a handle that
# we can use to read the data. You are given a handle if the requested file exists and
# you have the proper permissions to read the file.
# If the file does not exist, open will fail with a traceback and you will not get a
# handle to access the contents of the file.

# Opens the file named mbox.txt in read mode and assigns the file object to the variable called fhand.
fhand = open('mbox.txt')
# Prints the file object stored in variable fhand to the console.
# This will typically display information about the file object, not the file's contents.
print(fhand)
