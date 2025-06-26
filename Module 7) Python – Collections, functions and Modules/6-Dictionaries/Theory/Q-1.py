"""
Introduction to dictionaries: key-value pairs.

-->

 What are Dictionaries?
- A dictionary is a collection data type used to store data in pairs.
- Each pair consists of:
  - A key (which is unique) that acts as an identifier.
  - A value (which can be of any data type) associated with the key.
- Dictionaries are represented using curly braces `{}`. Key-value pairs within the dictionary are separated by commas, and each key is separated from its value by a colon `:`.

Example Concept:  
A dictionary to store student grades might look like this:  
`grades = {"Alice": 85, "Bob": 92, "Charlie": 78}`.  
Here:
  - `"Alice"`, `"Bob"`, and `"Charlie"` are the keys.
  - `85`, `92`, and `78` are the values.


 Key Characteristics of Dictionaries:
1. Unordered:
   - The elements (key-value pairs) in a dictionary are not stored in any specific order.
2. Mutable:
   - You can add, update, or delete key-value pairs after the dictionary is created.
3. Unique Keys:
   - Each key in a dictionary must be unique. If a duplicate key is assigned, the previous value for that key is overwritten.
4. Values Can Be Duplicated:
   - While keys must be unique, values can be repeated.


 Why Use Key-Value Pairs?
- Key-value pairs allow for efficient data storage and retrieval.
- Rather than accessing elements by index (as in lists or tuples), you retrieve values by referring to their unique keys.

Example Concept:  
For `grades = {"Alice": 85, "Bob": 92, "Charlie": 78}`,  
- Accessing a value: `grades["Bob"]` retrieves `92`.


Dictionaries are widely used for organizing and working with structured data.
"""