"""
Understanding how to access and manipulate strings. 

--> Here’s a theoretical overview to help you understand string access and manipulation:

What Are Strings?

Strings are sequences of characters and are one of the most commonly used data types in programming. In Python, strings are immutable, meaning their content cannot be changed after they are created.

Accessing Strings
You can access individual characters of a string using indexing:
- Indexes start from `0` for the first character, and negative indexes can be used to access characters from the end.
- Example: If `s = "Hello"`, `s[0]` gives `H` and `s[-1]` gives `o`.

You can also access portions of a string using **slicing**:
- Slicing syntax: `string[start:end:step]`
  - `start`: The starting index (inclusive).
  - `end`: The ending index (exclusive).
  - `step`: The interval at which characters are selected.
- Example: `s[1:4]` gives `ell`, `s[::-1]` reverses the string.

Manipulating Strings
Here are some common string manipulation methods in Python:

1. Removing Whitespace:
   - `strip()` removes leading and trailing whitespace.
   - `lstrip()` or `rstrip()` removes whitespace from the left or right only.

2. Changing Case:
   - `upper()`: Converts all characters to uppercase.
   - `lower()`: Converts all characters to lowercase.
   - `capitalize()`: Capitalizes the first character of the string.
   - `title()`: Capitalizes the first letter of each word.

3. Replacing Content:
   - `replace(old, new)`: Replaces all occurrences of `old` with `new`.

4. Splitting and Joining:
   - `split(delimiter)`: Splits the string into a list of substrings based on the delimiter.
   - `join(iterable)`: Joins elements of an iterable into a string with a specified separator.

5. Finding Substrings:
   - `find(substring)`: Returns the first index of the substring. Returns `-1` if not found.
   - `count(substring)`: Counts the occurrences of a substring.

6. Checking Content:
   - `startswith(substring)`: Checks if the string starts with a specific substring.
   - `endswith(substring)`: Checks if the string ends with a specific substring.
   - `isalnum()`, `isalpha()`, `isdigit()`: Check if the string contains only alphanumeric characters, letters, or digits.

String Immutability
Since strings are immutable, operations like `replace()` or `upper()` don’t modify the original string but instead
return a new string.

"""