""" Write a Python program to count occurrences of a substring in a string."""

def count_substring(string, substring):
    count = 0
    start = 0

    while start < len(string):
        pos = string.find(substring, start)

        if pos == -1: # If substring not found it will break the loop
            break

        count += 1 # If found it will increment count and update start position
        start = pos + 1  # move past the last found substring

    return count

string = "hello hello hello hello"
substring = "hello"
print(f"The substring '{substring}' appears {count_substring(string, substring)} times.")
