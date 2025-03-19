"""
Slicing a tuple to access ranges of elements.

-->

 What is Slicing?
- Slicing is a technique to retrieve a subset (or range) of elements from a tuple.
- It uses the syntax `tuple_name[start:end:step]`, where:
  - start: The index where slicing begins (inclusive).
  - end: The index where slicing stops (exclusive).
  - step (optional): Determines the interval between elements to include in the slice.


 Key Rules of Slicing:
1. If start is omitted, slicing begins from the first element (index `0`).
2. If end is omitted, slicing continues to the last element.
3. If step is omitted, the default value is `1`, meaning every element within the range is included.
4. Negative indices can be used for slicing, enabling you to slice from the end of the tuple.
5. A negative step can reverse the order of the slice.


 Examples of Slicing (Conceptual):
For a tuple `my_tuple = (10, 20, 30, 40, 50)`:
- `my_tuple[1:4]`: Retrieves elements at indices `1`, `2`, and `3`, resulting in `(20, 30, 40)`.
- `my_tuple[:3]`: Retrieves elements from the start up to (but not including) index `3`, resulting in `(10, 20, 30)`.
- `my_tuple[2:]`: Retrieves elements starting from index `2` to the end, resulting in `(30, 40, 50)`.
- `my_tuple[::2]`: Retrieves every second element, resulting in `(10, 30, 50)`.
- `my_tuple[::-1]`: Reverses the order of the tuple, resulting in `(50, 40, 30, 20, 10)`.


 Key Characteristics of Tuple Slicing:
- Slicing does not modify the original tuple—it creates a new tuple containing the specified range of elements.
- Because tuples are immutable, slicing is a safe way to extract and manipulate portions of a tuple without altering the original data.

Slicing is a highly versatile operation that simplifies accessing subsets of tuple data efficiently.
"""