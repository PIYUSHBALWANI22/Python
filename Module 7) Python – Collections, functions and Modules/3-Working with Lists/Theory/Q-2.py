"""
Sorting and reversing a list using sort(), sorted(), and reverse(). 

-->

1. sort()
- Purpose : Sorts the elements of a list *in-place* (modifies the original list) in ascending or descending order.
- Key Characteristics :
  - The default behavior is to sort in ascending order.
  - It includes an optional `reverse` parameter. Setting `reverse=True` sorts the list in descending order.
  - It works only for lists and modifies the list directly (no new list is created).
- Syntax : `list_name.sort()` or `list_name.sort(reverse=True)`.


2. sorted()
- Purpose : Returns a *new sorted list* without modifying the original list.
- Key Characteristics :
  - Like `sort()`, the default behavior is to sort in ascending order, but it also accepts a `reverse` parameter.
  - It works on any iterable, not just lists (e.g., tuples, dictionaries).
- Syntax : `sorted(list_name)` or `sorted(list_name, reverse=True)`.

Key Difference Between sort() and sorted():
- `sort()` modifies the original list, while `sorted()` creates a new, sorted copy of the list.


3. reverse()
- Purpose : Reverses the order of elements in a list *in-place* (modifies the original list).
- Key Characteristics :
  - This method does not sort the elements; it only reverses their current order.
  - It does not create a new list.
- Syntax : `list_name.reverse()`.

 Example Concept :
For a list `list_name = [3, 1, 4, 2]`:
- `list_name.sort()` results in `[1, 2, 3, 4]` (ascending order).
- `sorted(list_name, reverse=True)` results in `[4, 3, 2, 1]` (descending order, with original list unchanged).
- `list_name.reverse()` reverses the current order, e.g., `[4, 2, 1, 3]`.


These methods provide great flexibility for organizing and manipulating lists.
"""