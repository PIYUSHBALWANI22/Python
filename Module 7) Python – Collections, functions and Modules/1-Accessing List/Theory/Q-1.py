"""
Understanding how to create and access elements in a list. 

-->

1. Creating a List :
A list is a collection of items, which can be of different data types (like numbers, strings, or even other lists). Lists are usually represented with square brackets `[]`, and their elements are separated by commas.
- A list is initialized by defining the elements inside brackets.
- Lists are ordered, meaning the order in which you add elements is maintained.
- Lists are also mutable, allowing you to modify elements after creation.

Example : If you want a list of fruits, you'd define it as something like `["apple", "banana", "cherry"]`.


2. Accessing Elements in a List :
To access elements in a list, you typically use an index. The index represents the position of an element in the list:
- Indexing starts from `0` for the first element, `1` for the second, and so on.
- Negative indexing is also possible, where `-1` represents the last element, `-2` the second last, and so forth.
- You can access a single element or retrieve a subset of elements using slicing.

Access Example Concepts :
- For the first element: `list_name[0]`
- For a range of elements: `list_name[start:end]` (excluding the element at the `end` index).


Special Characteristics :
- Lists allow duplication of elements (e.g., `["apple", "apple", "banana"]`).
- Lists may contain mixed data types (e.g., `[123, "text", True]`).

"""