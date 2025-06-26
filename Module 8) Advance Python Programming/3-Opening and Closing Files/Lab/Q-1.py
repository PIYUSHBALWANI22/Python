"""
Write a Python program to open a file in write mode, write some text, and then close it.
"""

with open("example.txt", "w") as file:
    file.write("Hello, this is a sample text written to the file.\n")
    file.write("Python makes file handling easy!\n")

print("Text has been written to 'example.txt'.")
