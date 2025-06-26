"""
Creating and accessing elements in a tuple.

--> 


 1. Creating a Tuple
- A tuple is created by enclosing elements in parentheses `()` and separating them with commas.
- Tuples can contain elements of any data type (e.g., integers, strings, floats, or even other tuples).
- To create an empty tuple, simply use `()`.

Examples:
- A tuple of numbers: `numbers = (1, 2, 3)`
- A tuple of mixed data types: `mixed = (42, "hello", 3.14)`
- An empty tuple: `empty = ()`
- A single-element tuple: Add a trailing comma to differentiate it from a plain value, e.g., `single = (5,)`.


 2. Accessing Elements in a Tuple
- Elements in a tuple can be accessed using indexing or slicing, similar to lists.

# Indexing:
- Use an index to retrieve a specific element. Indexing starts from `0` (positive indexing) or from `-1` (negative indexing for reverse order).
- Example: For the tuple `my_tuple = (10, 20, 30, 40)`,  
  - `my_tuple[0]` retrieves the first element (`10`).
  - `my_tuple[-1]` retrieves the last element (`40`).

# Slicing:
- Slicing retrieves a range of elements from a tuple.
- Use the syntax `tuple_name[start:end]` to specify the range (start index is inclusive, end index is exclusive).
- Example: For `my_tuple = (10, 20, 30, 40)`,  
  - `my_tuple[1:3]` retrieves `(20, 30)`.


 Key Characteristics:
- Tuples are immutable, so their elements cannot be changed after creation.
- While elements cannot be modified, you can still access or iterate over them.

Tuples are perfect when you need a collection of values that should remain constant.
"""