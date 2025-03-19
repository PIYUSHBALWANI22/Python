"""
Introduction to tuples, immutability.

-->

 What are Tuples?
- A tuple is a collection data type that is used to store an ordered sequence of elements.
- Like lists, tuples can store elements of different data types (e.g., integers, strings, floats, or even other tuples).
- Tuples are represented by parentheses `()` and elements are separated by commas.

Example Concept:  
A tuple storing names might look like this: `names = ("Alice", "Bob", "Charlie")`.


 Key Characteristics of Tuples:
1. Ordered: Tuples maintain the order of elements, just like lists. The order in which elements are added is preserved.
2. Indexed: Elements in a tuple can be accessed using zero-based indexing (`tuple_name[index]`).
3. Allow Duplicates: Tuples can contain duplicate values.
4. Immutable: This is the defining characteristic of tuples.


What is Immutability?
- Immutability means that once a tuple is created, its elements cannot be changed, added, or removed.
- Unlike lists (which are mutable), tuples provide data integrity by ensuring that the stored elements remain constant after creation.

Why is Immutability Useful?
- It helps protect data from unintended modifications, making tuples ideal for use as fixed collections.
- Tuples can be used as keys in dictionaries or as elements in sets (unlike mutable types like lists).


How to Use Tuples:
- You can create a tuple by enclosing elements in parentheses, e.g., `tuple_name = (1, 2, 3)`.
- Access elements using indexing, e.g., `tuple_name[0]` retrieves the first element.
- You can perform operations like slicing and concatenation, but you cannot modify existing elements.


Tuples are simple yet powerful, especially when you need a collection that remains constant throughout your program.
"""