"""
Write a Python program to demonstrate the creation of variables and different data types. 

"""
# Demonstrating variable creation and data types in Python

# Integer
age = 25
print(f"Age (Integer): {age}, Type: {type(age)}")

# Float
height = 5.9
print(f"Height (Float): {height}, Type: {type(height)}")

# String
name = "Alice"
print(f"Name (String): {name}, Type: {type(name)}")

# Boolean
is_student = True
print(f"Is Student (Boolean): {is_student}, Type: {type(is_student)}")

# List (a collection of items)
fruits = ["Apple", "Banana", "Cherry"]
print(f"Fruits (List): {fruits}, Type: {type(fruits)}")

# Tuple (immutable collection of items)
dimensions = (1920, 1080)
print(f"Dimensions (Tuple): {dimensions}, Type: {type(dimensions)}")

# Dictionary (key-value pairs)
person = {"name": "Alice", "age": 25, "is_student": True}
print(f"Person (Dictionary): {person}, Type: {type(person)}")

# Set (unique and unordered collection)
unique_numbers = {1, 2, 3, 3, 2, 1}
print(f"Unique Numbers (Set): {unique_numbers}, Type: {type(unique_numbers)}")

# NoneType (represents the absence of a value)
value = None
print(f"Value (NoneType): {value}, Type: {type(value)}")
