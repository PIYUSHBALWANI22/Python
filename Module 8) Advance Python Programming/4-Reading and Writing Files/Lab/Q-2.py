"""
Write a Python program to write multiple strings into a file.
"""

with open("example.txt", "w") as file:
    lines = [
        "Hello, this is the first line.\n",
        "Python makes file handling simple!\n",
        "This is the third line of the file.\n"
    ]
    
    file.writelines(lines)

print("Multiple strings have been written to 'example.txt'.")
