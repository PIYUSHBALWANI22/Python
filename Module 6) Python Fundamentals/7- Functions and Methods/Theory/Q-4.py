"""
Built-in methods for strings, lists, etc.

--> Python provides a wide range of **built-in methods** for data types like strings, lists, dictionaries, and tuples. These methods simplify operations such as data manipulation, searching, and formatting. Below is an overview of some common built-in methods for **strings**, **lists**, and other data types.

---

1. String Methods
Strings in Python are immutable, and string methods return a new string while leaving the original one unmodified. Some commonly used string methods include:

- `lower()` - Converts all characters to lowercase.
- `upper()` - Converts all characters to uppercase.
- `strip()` - Removes leading and trailing spaces.
- `replace(old, new)` - Replaces occurrences of `old` with `new`.
- `split(delimiter)` - Splits the string into a list based on the specified `delimiter`.
- `join(iterable)` - Joins elements of an iterable (e.g., a list) into a string, separated by the specified string.
- `find(sub)` - Returns the index of the first occurrence of the substring `sub`. Returns `-1` if not found.
- `startswith(prefix)` - Checks if the string starts with the specified `prefix`.
- `endswith(suffix)` - Checks if the string ends with the specified `suffix`.

---

2. List Methods
Lists are mutable, and their methods allow you to modify their content. Some common list methods include:

- `append(element)` - Adds an element to the end of the list.
- `extend(iterable)` - Extends the list by appending all elements from an iterable.
- `insert(index, element)` - Inserts an element at the specified index.
- `remove(element)` - Removes the first occurrence of the specified element.
- `pop(index)` - Removes and returns the element at the specified index (default is the last element).
- `index(element)` - Returns the index of the first occurrence of the specified element.
- `count(element)` - Returns the number of occurrences of the specified element.
- `sort()` - Sorts the list in ascending order (can be modified with parameters).
- `reverse()` - Reverses the order of elements in the list.

---

3. Dictionary Methods
Dictionaries are mutable mappings of key-value pairs. Common dictionary methods include:

- `get(key, default)` - Returns the value for the specified key or a default value if the key is not found.
- `keys()` - Returns a view object containing all the keys.
- `values()` - Returns a view object containing all the values.
- `items()` - Returns a view object containing all the key-value pairs as tuples.
- `update(other_dict)` - Updates the dictionary with key-value pairs from another dictionary.
- `pop(key)` - Removes and returns the value associated with the specified key.
- `clear()` - Removes all key-value pairs from the dictionary.

---

4. Tuple Methods
Tuples are immutable, so they have fewer methods compared to lists. Common tuple methods include:

- `count(element)` - Returns the number of occurrences of the specified element.
- `index(element)` - Returns the index of the first occurrence of the specified element.

---

5. Set Methods
Sets are mutable collections of unique elements. Common set methods include:

- `add(element)` - Adds an element to the set.
- `remove(element)` - Removes the specified element (raises an error if not found).
- `discard(element)` - Removes the specified element (does not raise an error if not found).
- `union(other_set)` - Returns a set containing all unique elements from both sets.
- `intersection(other_set)` - Returns a set containing elements common to both sets.
- `difference(other_set)` - Returns a set containing elements in the first set but not in the second.


"""