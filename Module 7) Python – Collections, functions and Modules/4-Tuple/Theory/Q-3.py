"""
Basic operations with tuples: concatenation, repetition, membership.

-->


 1. Concatenation
- Purpose: Combines two or more tuples into a single tuple.
- Key Characteristics:
  - The `+` operator is used for concatenation.
  - It creates a new tuple that includes all elements from the tuples being concatenated.
  - The original tuples remain unchanged.

Key Concept:  
If `tuple1 = (1, 2)` and `tuple2 = (3, 4)`, then `tuple1 + tuple2` results in `(1, 2, 3, 4)`.


 2. Repetition
- Purpose: Repeats the elements in a tuple a specified number of times.
- Key Characteristics:
  - The `*` operator is used for repetition.
  - It creates a new tuple with repeated elements.
  - The original tuple remains unchanged.

Key Concept:  
If `tuple1 = (1, 2)`, then `tuple1 * 3` results in `(1, 2, 1, 2, 1, 2)`.


 3. Membership
- Purpose: Checks whether an element exists in a tuple.
- Key Characteristics:
  - The `in` operator is used to verify if a value is present.
  - The `not in` operator checks if a value is absent.
  - Returns a boolean value (`True` or `False`).

Key Concept:  
If `tuple1 = (1, 2, 3)`, then:
- `2 in tuple1` returns `True`.
- `4 in tuple1` returns `False`.


These operations make tuples versatile for handling fixed collections of data.
"""