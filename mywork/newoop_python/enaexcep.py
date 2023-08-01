import os

# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode.
# There are four different methods (modes) for opening a file:
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists


# Checking if a File Exists
file_path = "ena.txt"
if os.path.exists(file_path):
    print("File exists.")
else:
    print("File does not exist.")


# Reading the Entire File Content


f = open("ena.txt", "a")
# Write some text to the file
f.write("This is some more text")
f.close()
print("Text appended to the file successfully.")

#  Opening a file in write mode
f = open("ena.txt", "w")
f.write("This is some new text")
f.close()
print("Text written to the file successfully.")


# trying to access the written cotent onto the file


file_path = "ena.txt"
# Open the file in append mode
with open(file_path, "a") as f:
    # Write some text to the file
    f.write("This is some more text")
# Read the appended content
with open(file_path, "r") as f:
    content = f.read()
    print(content)

# By looping through the lines of the file, you can read the whole file, line by line:

# Example
# Loop through the file line by line

f = open("ena.txt", "r")
for x in f:
    print(x)


# Open the file "demofile3.txt" and overwrite the content
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

# open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())




# Delete a File
# To delete a file, you must import the OS module, and run its os.remove() function

import os
os.remove("demofile.txt")

# Check if file exists, then delete it:

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
