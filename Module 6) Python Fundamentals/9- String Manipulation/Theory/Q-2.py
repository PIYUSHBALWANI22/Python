"""
Basic operations: concatenation, repetition, string methods (upper(), lower(), etc.).

--> Explanation of basic string operations and commonly used string methods in Python:

---

Basic Operations

1. Concatenation:
   - Combines two or more strings into a single string using the `+` operator.
   - Example: `"Hello" + " " + "World"` results in `"Hello World"`.
   - Note: Concatenation only works with strings. Mixing strings with other types (like integers) will cause an error unless explicitly converted using `str()`.

2. Repetition:
   - Repeats a string multiple times using the `*` operator.
   - Example: `"Hi " * 3` results in `"Hi Hi Hi "`.
   - Useful for creating repeated patterns or formatting text.

---

Common String Methods

1. `upper()`:
   - Converts all characters in the string to uppercase.
   - Example: `"hello".upper()` results in `"HELLO"`.

2. `lower()`:
   - Converts all characters in the string to lowercase.
   - Example: `"HELLO".lower()` results in `"hello"`.

3. `strip()`:
   - Removes leading and trailing whitespace (or specified characters) from the string.
   - Example: `"   hello   ".strip()` results in `"hello"`.

4. `replace(old, new)`:
   - Replaces all occurrences of a substring (`old`) with another substring (`new`).
   - Example: `"I love Python".replace("Python", "Java")` results in `"I love Java"`.

5. `split(delimiter)`:
   - Splits the string into a list of substrings based on a specified delimiter.
   - Example: `"apple,banana,grape".split(",")` results in `["apple", "banana", "grape"]`.

6. `join(iterable)`:
   - Joins elements of an iterable (like a list or tuple) into a single string, using the string as a separator.
   - Example: `"-".join(["apple", "banana", "grape"])` results in `"apple-banana-grape"`.

7. `capitalize()`:
   - Converts the first character of the string to uppercase, and the rest to lowercase.
   - Example: `"python programming".capitalize()` results in `"Python programming"`.

8. `title()`:
   - Converts the first character of each word in the string to uppercase.
   - Example: `"python programming".title()` results in `"Python Programming"`.

9. `startswith(substring)` and `endswith(substring)`:
   - Check whether a string starts or ends with the specified substring.
   - Example: `"Hello".startswith("He")` is `True`, `"Hello".endswith("lo")` is `True`.

10. `find(substring)`:
    - Returns the index of the first occurrence of the specified substring. Returns `-1` if the substring is not found.
    - Example: `"Python is fun".find("fun")` results in `10`.

11. `count(substring)`:
    - Counts the number of occurrences of a substring within the string.
    - Example: `"banana".count("a")` results in `3`.

"""