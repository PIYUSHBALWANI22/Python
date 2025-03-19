"""
Basic list manipulations: addition, deletion, updating, and slicing.

-->

1. Addition
- **Adding elements to a list** involves inserting new items either at the end or at a specific position.
- Common methods include:
  - **append()**: Adds a single element to the end of the list.
  - **extend()**: Adds multiple elements (from another list or iterable) to the end of the list.
  - **insert()**: Adds an element at a specified index, shifting the other elements to accommodate it.

Key Concept :  
For a list `list_name = [1, 2, 3]`:
- `list_name.append(4)` results in `[1, 2, 3, 4]`.
- `list_name.extend([5, 6])` results in `[1, 2, 3, 4, 5, 6]`.
- `list_name.insert(1, 10)` results in `[1, 10, 2, 3]`.

---

2. Deletion
- Removing elements from a list can be done in various ways:
  - remove() : Removes the *first occurrence* of a specific value.
  - pop(): Removes an element at a specified index (or the last element if no index is given) and returns it.
  - del statement : Deletes an element (or a slice of elements) by index.
  - clear(): Removes all elements from the list, leaving it empty.

Key Concept :  
For a list `list_name = [1, 2, 3, 4]`:
- `list_name.remove(2)` results in `[1, 3, 4]`.
- `list_name.pop(1)` removes and returns `2`, resulting in `[1, 3, 4]`.
- `del list_name[0:2]` removes the first two elements, resulting in `[3, 4]`.

---

3. Updating 
- Changing elements in a list involves directly assigning new values to specific indices.
- Since lists are mutable, elements can be modified in-place.

Key Concept :  
For a list `list_name = [1, 2, 3]`:
- `list_name[1] = 20` updates the element at index `1`, resulting in `[1, 20, 3]`.
- You can also update multiple elements using slicing, e.g., `list_name[0:2] = [10, 30]`, resulting in `[10, 30, 3]`.

---

4. Slicing
- Slicing is used to access or manipulate a subset of elements in a list.
- The syntax `list_name[start:end:step]` allows:
  - Accessing a range of elements.
  - Updating a slice of elements.
  - Deleting a slice of elements.

Key Concept :  
For a list `list_name = [1, 2, 3, 4, 5]`:
- Accessing: `list_name[1:4]` retrieves `[2, 3, 4]`.
- Updating: `list_name[1:4] = [20, 30, 40]` results in `[1, 20, 30, 40, 5]`.
- Deleting: `del list_name[1:3]` removes `[20, 30]`, resulting in `[1, 40, 5]`.

---

These manipulations form the foundation of working with lists and give you the flexibility to modify them as needed.
"""