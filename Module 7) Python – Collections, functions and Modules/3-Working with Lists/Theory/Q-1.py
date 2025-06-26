"""
Iterating over a list using loops. 

-->

What is Iteration?
- Iteration is the process of accessing each element in a list, one at a time.
- Loops are commonly used for iteration, allowing us to systematically perform operations on each element.


Common Loops for List Iteration :
 1. For Loop :
- Purpose : Iterates over each element in the list directly.
- Key Concept : The loop variable takes the value of each element in the list, one at a time.
- Syntax : 
  ```
  for element in list_name:
      # Perform an action with 'element'
  ```

Example Concept :
For a list `list_name = [10, 20, 30]`, a `for` loop processes `10`, then `20`, and finally `30`.

---

2. While Loop :
- Purpose : Iterates over a list based on a condition (commonly using an index).
- Key Concept : You maintain a counter (or index) that increments with each iteration until a specified condition is met.
- Syntax:
  ```
  index = 0
  while index < len(list_name):
      # Perform an action with 'list_name[index]'
      index += 1
  ```

Example Concept :
For the same list `list_name = [10, 20, 30]`, a `while` loop starts at index `0`, processes the element at that index (`10`), then increments the index to process the next element (`20`), and so on.


Key Characteristics of Iterating Over Lists :
- A `for` loop is straightforward and ideal when you need to process each element sequentially.
- A `while` loop offers more control but requires careful management of the index and condition to avoid infinite loops.

Iteration is a core concept for working with lists, allowing actions like processing, modifying, or filtering elements.
"""