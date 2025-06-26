"""
Reading from a file using read(), readline(), readlines(). 

--> In Python, there are several methods to read the content of a file, each serving a specific purpose. Here's a explanation of how the `read()`, `readline()`, and `readlines()` methods work for reading from a file:


 1. `read()` Method
- Purpose: Reads the entire content of the file as a single string.
- Theoretical Behavior:
  - Reads all the data from the file starting at the current file pointer position.
  - If the file is large, the `read()` method might consume a significant amount of memory.

Syntax:
```
file.read(size)
```
- `size` (optional): The number of bytes to read. If omitted or set to `-1`, the entire file is read.

Example:
```
with open("example.txt", "r") as file:
    content = file.read()  # Reads the entire file into a string.
    print(content)
```


 2. `readline()` Method
- Purpose: Reads a single line from the file, up to the next newline character (`\n`).
- Theoretical Behavior:
  - Returns the line as a string (including the newline character).
  - Each subsequent call to `readline()` continues from where the previous call left off.

Syntax:
```
file.readline(size)
```
- `size` (optional): The maximum number of characters to read. If omitted, the entire line is read.

Example:
```
with open("example.txt", "r") as file:
    first_line = file.readline()  # Reads the first line.
    second_line = file.readline()  # Reads the second line.
    print(first_line, second_line)
```


 3. `readlines()` Method
- Purpose: Reads all lines in the file and returns them as a list of strings.
- Theoretical Behavior:
  - Each line in the file becomes an element of the list.
  - Useful for processing the file line by line in a loop.

Syntax:
```
file.readlines(sizehint)
```
- `sizehint` (optional): An approximate number of bytes to read. If omitted, all lines are read.

Example:
```
with open("example.txt", "r") as file:
    lines = file.readlines()  # Reads all lines into a list.
    for line in lines:
        print(line.strip())  # Removes extra newline characters.
```


 Comparison of Methods
| Method        | Returns                         | Use Case                              |
|---------------|---------------------------------|---------------------------------------|
| `read()`    | Entire file as a single string | When the full content needs to be loaded at once. |
| `readline()` | A single line as a string      | When processing a file one line at a time.         |
| `readlines()` | A list of all lines           | When iterating over lines as a collection.         |


 Practical Considerations
- When handling very large files, avoid using `read()` or `readlines()` as they load the entire file into memory, which can be inefficient. Instead, process the file line by line using `readline()` or iterate directly over the file object:
  ```
  with open("example.txt", "r") as file:
      for line in file:
          print(line.strip())
  ```

By selecting the appropriate method, you can efficiently handle file reading operations based on the requirements of your program!
"""