"""
Anonymous functions (lambda functions).

--> Anonymous functions, also known as lambda functions, are functions that do not have a name. They are primarily used for short, simple operations and are defined using the `lambda` keyword.

1. Syntax:
   - A lambda function is written as:
     ```
     lambda arguments: expression
     ```
   - It can have any number of arguments, but only a single expression.
   - The expression is evaluated and returned.

2. Characteristics:
   - They are limited to a single line of code.
   - They don't have a `def` keyword or a function name.
   - Typically used for short-lived tasks where defining a full function might be unnecessary.

3. Use Cases:
   - Often used with functions like `map()`, `filter()`, and `reduce()`.
   - Helpful for quick computations or operations within other functions or programs.

4. Limitations:
   - Since they are restricted to a single expression, they lack readability and versatility for complex logic.
   - Cannot include statements or annotations.

For example
```
lambda x, y: x + y
```

"""