"""
Common list operations: concatenation, repetition, membership. 

-->

 1. Concatenation
- Concatenation is the process of combining two or more lists into a single list.
- The `+` operator is used for concatenation.
- It does not modify the original lists but creates a new list containing all the elements of the lists being combined.

Key Concept :
If `list1 = [1, 2, 3]` and `list2 = [4, 5, 6]`, then `list1 + list2` results in `[1, 2, 3, 4, 5, 6]`.


 2. Repetition
- Repetition is the process of duplicating the elements in a list a specified number of times.
- The `*` operator is used for repetition.
- This operation also creates a new list and does not alter the original list.

Key Concept :
If `list1 = [1, 2, 3]` and you perform `list1 * 3`, the result will be `[1, 2, 3, 1, 2, 3, 1, 2, 3]`.


 3. Membership
- The membership operation is used to check whether an element exists in a list.
- The `in` operator is used to verify membership and returns a boolean value (`True` or `False`).
- The `not in` operator can check for absence of an element in the list.

Key Concept :
If `list1 = [1, 2, 3]`, then:
- `2 in list1` returns `True`.
- `4 in list1` returns `False`.

---

These operations are powerful tools that make working with lists flexible and efficient.
"""