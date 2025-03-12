"""
String slicing

--> String slicing is a technique in Python that allows you to extract a portion or subset of a string based on specified indices. It provides a flexible and powerful way to access and manipulate string data.

---

Syntax for String Slicing
The general syntax for string slicing is:

`string[start:end:step]`

- `start` (optional): The index of the first character to include in the slice. Defaults to `0` if omitted.
- `end` (optional): The index of the first character to *exclude* from the slice. Defaults to the length of the string if omitted.
- `step` (optional): The interval or step size to skip characters. Defaults to `1` if omitted.

---

How Slicing Works
1. Extract a Substring:
   - To get a specific portion of a string, provide `start` and `end` indices.
   - Example: If `s = "Hello, World!"`, `s[0:5]` results in `"Hello"`.
   
2. Skip Characters:
   - Use the `step` parameter to skip characters.
   - Example: `s[::2]` will take every second character from the string.

3. Omitting Indices:
   - You can omit `start` or `end` to slice from the beginning or up to the end of the string.
   - Example:
     - `s[:5]` extracts the first 5 characters.
     - `s[7:]` extracts everything from index 7 onward.

4. Negative Indices:
   - Use negative indices to slice from the end of the string.
   - Example:
     - `s[-6:]` extracts the last 6 characters.
     - `s[::-1]` reverses the string by stepping backward.

5. **Default Values**:
   - If no values are specified, the entire string is returned as is: `s[:]`.

---

Examples of String Slicing
1. Basic Slicing:
   - `s[2:8]`: Extracts characters from index 2 (inclusive) to index 8 (exclusive).

2. Skipping Characters:
   - `s[::3]`: Takes every third character.

3. Reversing the String:
   - `s[::-1]`: Reverses the string using a negative `step`.

4. Working with Negative Indices:
   - `s[-5:-2]`: Extracts characters from the 5th-to-last to the 3rd-to-last (exclusive).

---

Why Use String Slicing?
- Efficiently extract substrings without writing complex loops.
- Simplify operations like reversing a string, skipping characters, or working with parts of strings.
- Enhance code readability when working with indices.

"""