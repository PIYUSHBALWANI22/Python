"""
Write a Python program to match a word in a string using re.match().
"""

import re

text = "The quick brown fox jumps over the lazy dog."

word = "The"

match = re.match(r'\b' + re.escape(word) + r'\b', text)

if match:
    print(f"'{word}' was found at the beginning of the string.")
else:
    print(f"'{word}' was not found at the beginning of the string.")