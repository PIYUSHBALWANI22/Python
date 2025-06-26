"""
How functional programming works in Python.

--> Functional Programming in Python :

Functional programming is a programming paradigm where functions are treated as first-class citizens. It emphasizes the use of functions to perform computation and avoids changing state or mutable data. Python, while not a purely functional programming language, supports functional programming concepts and provides tools to implement them.

---

Key Concepts of Functional Programming in Python

1. First-Class Functions :
   - Functions are treated as first-class citizens, meaning they can be assigned to variables, passed as arguments, and returned from other functions.
   - Example:
     ```
     def greet(name):
         return f"Hello, {name}!"
     greeting = greet  # Assigning the function to a variable
     print(greeting("Piyush"))  # Output: Hello, Piyush!
     ```

2. Immutability :
   - Functional programming emphasizes immutable data. Instead of modifying data, new data structures are created.
   - While Python has mutable types (like lists), programmers can choose to work with immutable types (like tuples) to adhere to this principle.

3. Pure Functions :
   - A pure function is one whose output is determined only by its input arguments and has no side effects (e.g., no modifying global variables or I/O operations).

4. Higher-Order Functions :
   - A higher-order function is a function that either takes another function as an argument or returns a function as a result.
   - Examples of built-in higher-order functions in Python:
     - `map()`: Applies a function to all items in an iterable.
     - `filter()`: Filters elements of an iterable based on a function.
     - `reduce()`: Reduces an iterable to a single value using a function (requires `functools` module).

5. Lambda Functions :
   - Python provides support for writing anonymous (inline) functions using the `lambda` keyword.
   - Example:
     ```
     square = lambda x: x**2
     print(square(5))  # Output: 25
     ```

6. Recursion :
   - Functional programming often uses recursion instead of loops for iterative processes.
   - Python supports recursion, but developers need to be mindful of Python's recursion limit (`sys.setrecursionlimit`).

7. List Comprehensions :
   - Though not exclusive to functional programming, list comprehensions allow concise and expressive transformations of data.


Functional Programming Tools in Python

1. `map(function, iterable)`:
   - Applies a function to each element of an iterable and returns a map object.
   - Example:
     ```
     numbers = [1, 2, 3, 4]
     squared = list(map(lambda x: x**2, numbers))  # Output: [1, 4, 9, 16]
     ```

2. `filter(function, iterable)`:
   - Filters elements of an iterable for which the function returns `True`.
   - Example:
     ```
     even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # Output: [2, 4]
     ```

3. `reduce(function, iterable)`:
   - Reduces an iterable to a single value by applying the function cumulatively (from `functools` module).
   - Example:
     ```
     from functools import reduce
     product = reduce(lambda x, y: x * y, numbers)  # Output: 24
     ```

4. `zip()`:
   - Combines multiple iterables into a single iterable of tuples.
   - Example:
     ```
     names = ["Alice", "Bob"]
     scores = [85, 90]
     paired = list(zip(names, scores))  # Output: [('Alice', 85), ('Bob', 90)]
     ```

5. List Comprehensions :
   - Provides a functional way to process iterables concisely.
   - Example:
     ```
     doubled = [x * 2 for x in numbers]  # Output: [2, 4, 6, 8]
     ```


Advantages of Functional Programming in Python :

- Code is often shorter, clearer, and more concise.
- Easier debugging and testing, as pure functions have no side effects.
- Promotes modular and reusable code.


Limitations in Python :

- Python is not a pure functional programming language, so adhering strictly to functional principles might not always align with Pythonic conventions.
- Recursive function calls can be less efficient due to Python's recursion limits.


"""