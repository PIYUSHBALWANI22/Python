"""
Using re.search() and re.match() functions in Python’s re module for pattern 
matching. 

--> The `re` module in Python provides powerful tools for working with regular expressions, allowing pattern matching in strings. Among its most commonly used functions for pattern matching are `re.search()` and `re.match()`. These functions differ in their behavior and scope of searching within a string.


 1. `re.search()`

# Definition:
The `re.search()` function scans through the entire string looking for a match to the specified pattern. If a match is found, it returns a match object; otherwise, it returns `None`.

# Theoretical Use Case:
- Useful when you need to locate a pattern anywhere in a string, not just at the beginning.

# Syntax:
```
re.search(pattern, string, flags=0)
```
- `pattern`: The regular expression pattern to be matched.
- `string`: The target string where the pattern will be searched.
- `flags`: Optional modifiers (e.g., `re.IGNORECASE` for case-insensitive matching).

# Example:
```
import re

string = "Hello, Piyush! How are you?"
pattern = r"Piyush"

# Search for 'Piyush' in the string
match = re.search(pattern, string)
if match:
    print(f"Found: {match.group()}")  # Outputs: Found: Piyush
else:
    print("No match found.")
```
- The `re.search()` function scans the entire string and finds "Piyush" even though it is not at the beginning.


 2. `re.match()`

# Definition:
The `re.match()` function checks for a match only at the beginning of the string. If the pattern does not match the start of the string, it returns `None`.

# Theoretical Use Case:
- Useful when you need to ensure that the pattern matches the very start of the string.

# Syntax:
```
re.match(pattern, string, flags=0)
```
- `pattern`: The regular expression pattern to be matched.
- `string`: The target string where the pattern will be checked.
- `flags`: Optional modifiers (e.g., `re.MULTILINE` for multiline processing).

# Example:
```
import re

string = "Hello, Piyush! How are you?"
pattern = r"Hello"

# Match 'Hello' at the beginning of the string
match = re.match(pattern, string)
if match:
    print(f"Found: {match.group()}")  # Outputs: Found: Hello
else:
    print("No match found.")
```
- The `re.match()` function matches "Hello" because it is at the very beginning of the string.


 Key Differences

| Feature                  | `re.search()`                        | `re.match()`                        |
|--------------------------|---------------------------------------|-------------------------------------|
| Scope                | Searches anywhere in the string      | Matches only at the start of the string |
| Use Case             | Locate patterns anywhere             | Ensure patterns occur at the beginning |
| Return Value         | Match object or `None`               | Match object or `None`              |
| Example Input        | `"How is Piyush?"`                   | `"How is Piyush?"`                  |
| Example Pattern      | `"Piyush"` → Match Found             | `"Piyush"` → No Match Found         |


 Advanced Features

# Using Flags:
Both functions support flags to modify matching behavior, such as:
- `re.IGNORECASE`: Case-insensitive matching.
- `re.MULTILINE`: Processes multiple lines independently.

Example:
```
import re

string = "hello, Piyush!"
pattern = r"HELLO"
match = re.search(pattern, string, re.IGNORECASE)
if match:
    print(f"Found: {match.group()}")  # Outputs: Found: hello
```

# Using `group()`:
The `group()` method of the match object retrieves the matched part of the string.


 Conclusion
Theoretically, `re.search()` and `re.match()` cater to different use cases based on the scope of pattern matching required. While `re.match()` is ideal for matching patterns at the start of strings, `re.search()` provides more flexibility by scanning the entire string. Together, they enable precise and efficient pattern matching in Python.
"""