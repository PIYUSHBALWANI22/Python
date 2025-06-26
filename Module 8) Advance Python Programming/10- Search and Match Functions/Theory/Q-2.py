"""
Difference between search and match. 

--> The difference between `re.search()` and `re.match()` in Python's `re` module lies in where they look for a pattern in a string:

 1. Scope of Matching
- `re.search()`:
  - Scans the entire string to find the first occurrence of the specified pattern.
  - If the pattern appears anywhere in the string, it returns a match object.
- `re.match()`:
  - Only checks for a match at the beginning of the string.
  - If the pattern doesn’t match the start of the string, it returns `None`.
  

 2. Use Cases
- `re.search()`:
  - Ideal for finding a pattern anywhere in the string.
  - Example: Searching for a keyword that might appear in any part of a sentence.
- `re.match()`:
  - Useful when you want to ensure that a string starts with a specific pattern.
  - Example: Validating if a string begins with a certain prefix or format.


 3. Example Comparison
```
import re

string = "Hello, Piyush! How are you?"
pattern = r"Piyush"

# Using re.search()
search_result = re.search(pattern, string)
if search_result:
    print(f"'search' Found: {search_result.group()}")  # Outputs: Found: Piyush

# Using re.match()
match_result = re.match(pattern, string)
if match_result:
    print(f"'match' Found: {match_result.group()}")  # No output (Piyush is not at the start)
else:
    print("'match' Did not find the pattern.")  # Outputs: Did not find the pattern.
```


 4. Key Differences at a Glance

| Feature             | `re.search()`                | `re.match()`                  |
|---------------------|-----------------------------------|-----------------------------------|
| Where it Searches | Scans the entire string           | Checks only the start of the string |
| Match Requirement | Pattern can appear anywhere       | Pattern must appear at the beginning |
| Returns          | Match object or `None`           | Match object or `None`            |


In summary, use `re.search()` when you need to find a pattern at any position in the string, and `re.match()` when the pattern must match the very start of the string. These differences make them suited to different validation and searching scenarios.
"""