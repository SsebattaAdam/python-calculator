file_path = "example.txt"

# Open the file in read mode
file_object = open(file_path, "r")

# Read the entire content of the file
content = file_object.read()

# Print a message along with the file's content
print("File content:")
print(content)

# Close the file
file_object.close()


# Writing to a File:
file_path = "example.txt"

# Open the file in write mode
file_object = open(file_path, "w")

# Write data to the file
file_object.write("Hello, world!")

# Close the file
file_object.close()

# Open the file in read mode
file_object = open(file_path, "r")

# Read and print the file's content
file_content = file_object.read()
print(file_content)

# Close the file
file_object.close()


# appending to a file
file_path = "example.txt"

# Open the file in append mode
file_object = open(file_path, "a")

# Append data to the file
file_object.write("\nThis is an appended line.")

# Close the file
file_object.close()

# Print a message
print("Data appended to the file:", file_path)


# Exception Handling with Files

file_path = "nonexistent_file.txt"
file_object = None

try:
    # Open the file
    file_object = open(file_path, "r")

    # Read the content
    content = file_object.read()
    print(content)

except FileNotFoundError:
    print("File not found.")

except Exception as e:
    print("An error occurred:", str(e))

finally:
    # Close the file (executes regardless of exceptions)
    if file_object is not None:
        file_object.close()
