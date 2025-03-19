"""
Understanding list methods like append(), insert(), remove(), pop(). 

--> 

1. append()
- Purpose : Adds a new element to the *end* of a list.
- Key Points :
  - The list size increases by one.
  - The original list is directly modified; no new list is created.
- Syntax : `list_name.append(element)`
- Use Case : When you want to add a single item to the end of an existing list.

2. insert()
- Purpose : Inserts an element at a specific index in the list.
- Key Points :
  - The index specifies where the new element is added.
  - Other elements in the list are shifted to make space for the new element.
- Syntax : `list_name.insert(index, element)`
- Use Case : When you want to add an item to a specific position in the list instead of the end.


3. remove()
- Purpose : Removes the *first occurrence* of a specified element from the list.
- Key Points :
  - If the element does not exist, it may raise an error.
  - Only the first matching element is removed, even if there are duplicates.
- Syntax : `list_name.remove(element)`
- Use Case : When you want to delete a specific value from the list.


4. pop()
- Purpose : Removes an element from the list *at a specified index* and returns it.
- Key Points :
  - The default index is `-1` if none is provided, meaning it removes the last element by default.
  - The size of the list decreases by one.
  - The removed element can be stored or used elsewhere, as it is returned.
- Syntax : `list_name.pop(index)`
- Use Case : When you need to remove and retrieve an element simultaneously.


Each of these methods is essential for modifying lists dynamically, depending on whether you're adding, removing, or extracting elements.
"""