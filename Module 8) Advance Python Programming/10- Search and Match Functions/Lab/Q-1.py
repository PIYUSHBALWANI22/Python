"""
Write a Python program to search for a word in a string using re.search().
"""

import re

text = "The quick brown fox jumps over the lazy dog."

word = "fox"

match = re.search(r'\b' + re.escape(word) + r'\b', text)

if match:
    print(f"'{word}' was found in the string.")
else:
    print(f"'{word}' was not found in the string.")