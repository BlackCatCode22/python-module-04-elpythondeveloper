# Chapter 7 - Files
# 7.8 Writing files

# File: writing_files.py
# Description - Write a string to a text file.

# To write a file, you have to open it with mode w as a second parameter
# If the file already exists, opening it in write mode clears out the old data and starts fresh
# If the file doesn’t exist, a new one is created.
fout = open('output.txt', 'w')
# save a string in variable called line1
# The print statement automatically appends a newline,
# but the write method does not add the newline automatically.
line1 = "This here's the wattle,\n"
# write the string saved in variable line1 then go to a new line
fout.write(line1)
# save a string in variable called line2
line2 = 'the emblem of our land.\n'
# write the string saved in variable line2 then go to a new line
fout.write(line2)

# When ww are done writing, w have to close the file to make sure that the last
# bit of data is physically written to the disk so it will not be lost if the power goes off.
fout.close()

