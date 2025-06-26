"""
Accessing tuple elements using positive and negative indexing.

-->

 1. Positive Indexing
- Definition: Positive indexing starts from `0` and moves forward through the tuple.
- Each position in the tuple is assigned a sequential index, with `0` representing the first element, `1` the second, and so on.
- Positive indexing is used when accessing elements from the *start* of the tuple.

Example Concept:  
For a tuple `my_tuple = ("a", "b", "c", "d")`:  
- `my_tuple[0]` retrieves the first element, `"a"`.  
- `my_tuple[2]` retrieves the third element, `"c"`.


 2. Negative Indexing
- Definition: Negative indexing starts from `-1` and moves backward through the tuple.
- The last element is assigned the index `-1`, the second last is `-2`, and so on.
- Negative indexing is useful when accessing elements from the *end* of the tuple.

Example Concept:  
For the same tuple `my_tuple = ("a", "b", "c", "d")`:  
- `my_tuple[-1]` retrieves the last element, `"d"`.  
- `my_tuple[-3]` retrieves the third last element, `"b"`.


 Key Characteristics:
- Positive indexing allows forward traversal, while negative indexing enables reverse traversal.
- Both methods provide flexibility to access specific elements in a tuple without modifying it, aligning with the tuple's immutable nature.

"""