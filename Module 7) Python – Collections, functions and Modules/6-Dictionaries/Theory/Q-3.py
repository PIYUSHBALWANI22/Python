"""
Dictionary methods like keys(), values(), and items().

-->

 1. keys() Method
- Purpose: Returns all the keys in the dictionary as a view object.
- Key Characteristics:
  - The view object behaves like a dynamic collection that reflects any changes made to the dictionary.
  - The keys are returned in the form of an iterable, which can be converted to a list if needed.

Syntax: `dict_name.keys()`

Conceptual Example:  
For `my_dict = {"a": 1, "b": 2, "c": 3}`:  
- `my_dict.keys()` returns `dict_keys(['a', 'b', 'c'])`.

---

 2. values() Method
- Purpose: Returns all the values in the dictionary as a view object.
- Key Characteristics:
  - The view object reflects changes to the dictionary dynamically.
  - It contains all the values in the dictionary.

Syntax: `dict_name.values()`

Conceptual Example:  
For `my_dict = {"a": 1, "b": 2, "c": 3}`:  
- `my_dict.values()` returns `dict_values([1, 2, 3])`.

---

 3. items() Method
- Purpose: Returns all key-value pairs in the dictionary as a view object.
- Key Characteristics:
  - Each key-value pair is represented as a tuple (`key, value`).
  - The view object is iterable and reflects changes dynamically.

Syntax: `dict_name.items()`

Conceptual Example:  
For `my_dict = {"a": 1, "b": 2, "c": 3}`:  
- `my_dict.items()` returns `dict_items([('a', 1), ('b', 2), ('c', 3)])`.

---

 Key Characteristics of These Methods:
- The returned view objects (`dict_keys`, `dict_values`, and `dict_items`) are dynamic—meaning any changes made to the dictionary will automatically update the view objects.
- These methods are useful for iteration, checking for membership, and converting dictionaries to lists for further processing.

"""