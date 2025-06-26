"""
Writing to a file using write() and writelines().

--> Theoretically, in Python, you can write content to a file using two primary methods: `write()` and `writelines()`. Each serves specific purposes, depending on whether you're adding single or multiple lines of text to a file.

---

 1. `write()` Method
- Purpose: The `write()` method allows writing a single string to the file.
- Theoretical Behavior:
  - It does not automatically add a newline character (`\n`). If a newline is required between entries, it must be explicitly included in the string.
  - Writing to a file opened in write (`w`) or append (`a`) mode is allowed.

# Syntax:
```
file.write(string)
```
- `string`: The text to be written to the file.

# Example:
```
with open("example.txt", "w") as file:
    file.write("Hello, world!")  # Writes "Hello, world!" to the file.
    file.write("\nThis is the second line.")  # Adds a second line.
```


 2. `writelines()` Method
- Purpose: The `writelines()` method is used to write multiple strings (usually lines) to the file in a single operation.
- Theoretical Behavior:
  - Accepts an iterable (e.g., a list or tuple) of strings.
  - Unlike `write()`, it does not automatically add newline characters between the strings. You must include `\n` in the strings if needed.

# Syntax:
```
file.writelines(iterable)
```
- `iterable`: A sequence of strings to be written to the file.

# Example:
```
lines = ["First line\n", "Second line\n", "Third line\n"]
with open("example.txt", "w") as file:
    file.writelines(lines)  # Writes all lines in the list to the file.
```


 Comparison of `write()` vs `writelines()`
| Feature             | `write()`                           | `writelines()`                      |
|---------------------|--------------------------------------|-------------------------------------|
| Input           | Single string                       | Iterable of strings (e.g., list)    |
| Newline Handling| Must be manually included            | Must be manually included in each string |
| Use Case        | Writing single entries or strings    | Writing multiple lines in one step  |


 Considerations When Writing to Files
1. Opening the File:
   - Use write mode (`w`) to create or overwrite the file.
   - Use append mode (`a`) to add content to an existing file without erasing it.

2. Automatic Resource Management:
   - Using the `with` statement is highly recommended, as it ensures the file is properly closed after writing.

3. Error Handling:
   - Proper exception handling, such as using `try-except`, can prevent data corruption or unexpected issues.


By employing `write()` and `writelines()` effectively, you can handle a wide range of file-writing operations, adapting to whether you're writing single strings or entire collections of lines.
"""