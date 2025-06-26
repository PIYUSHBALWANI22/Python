"""
Accessing, adding, updating, and deleting dictionary elements.

-->

 1. Accessing Dictionary Elements
- Purpose: Retrieve the value associated with a specific key in the dictionary.
- Method:
  - Use the key inside square brackets: `dict_name[key]`. If the key doesn’t exist, it raises an error.
  - Alternatively, use the `get()` method: `dict_name.get(key)`. If the key doesn’t exist, it returns `None` (or a default value if specified).

Example Concept:  
For `my_dict = {"a": 10, "b": 20, "c": 30}`:
- `my_dict["b"]` retrieves `20`.
- `my_dict.get("d")` retrieves `None` (since `"d"` is not a key).


 2. Adding Elements to a Dictionary
- Purpose: Add a new key-value pair to the dictionary.
- Method:
  - Assign a value to a new key: `dict_name[new_key] = value`. If the key already exists, the value is updated instead of adding a new pair.

Example Concept:  
For `my_dict = {"a": 10, "b": 20}`:
- Adding: `my_dict["c"] = 30` results in `{"a": 10, "b": 20, "c": 30}`.


 3. Updating Dictionary Elements
- Purpose: Modify the value of an existing key in the dictionary.
- Method:
  - Assign a new value to the key: `dict_name[key] = new_value`.

Example Concept:  
For `my_dict = {"a": 10, "b": 20}`:
- Updating: `my_dict["b"] = 50` changes the dictionary to `{"a": 10, "b": 50}`.


 4. Deleting Dictionary Elements
- Purpose: Remove a specific key-value pair or all elements from the dictionary.
- Methods:
  - Use the `del` statement: `del dict_name[key]` to delete a specific key-value pair.
  - Use the `pop()` method: `dict_name.pop(key)` to remove a key-value pair and return its value.
  - Use the `clear()` method: `dict_name.clear()` to remove all key-value pairs, leaving an empty dictionary.

Example Concept:  
For `my_dict = {"a": 10, "b": 20, "c": 30}`:
- Deleting a key: `del my_dict["b"]` results in `{"a": 10, "c": 30}`.
- Popping a key: `my_dict.pop("a")` removes `"a"` and returns `10`, leaving `{"b": 20, "c": 30}`.
- Clearing: `my_dict.clear()` results in `{}`.


Dictionaries are incredibly versatile for organizing and working with data.
"""