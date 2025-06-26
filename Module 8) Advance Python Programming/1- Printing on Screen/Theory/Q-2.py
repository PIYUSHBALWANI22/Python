"""
Formatting outputs using f-strings and format().

--> Formatting outputs is a key aspect of presenting data in a structured and visually appealing way. In Python, two popular approaches to formatting outputs are f-strings and the `format()` method. Here's a theoretical discussion of both:


 1. f-Strings (Formatted String Literals):
Introduced in Python 3.6, f-strings provide a concise and readable way to embed expressions inside string literals. Theoretically, they combine formatting efficiency with the clarity of inline expressions.

# Concepts:
- f-strings are denoted by prefixing the string with the letter `f` or `F`.
- Expressions or variables can be placed within curly braces `{}` and are evaluated at runtime.

# Advantages:
- More concise and readable compared to older formatting methods.
- Offers the ability to embed arbitrary Python expressions directly within the string.

# Example:
```
name = "Piyush"
age = 25
formatted_output = f"My name is {name}, and I am {age} years old."
# Output: My name is Piyush, and I am 25 years old.
```

# Inline Expressions:
```
num = 5
square = f"The square of {num} is {num2}."
# Output: The square of 5 is 25.
```


 2. The `format()` Method:
The `format()` method is a string method that replaces placeholders in a string with specified values. It provides a versatile way to format strings, allowing both positional and keyword arguments.

# Concepts:
- Placeholders are defined using curly braces `{}` in the string.
- The arguments provided to the `format()` function replace these placeholders.

# Advantages:
- Useful for dynamic formatting when positional or named substitutions are needed.
- Supports advanced formatting specifications for numbers, alignment, padding, etc.

# Example:
```
name = "Piyush"
age = 25
formatted_output = "My name is {}, and I am {} years old.".format(name, age)
# Output: My name is Piyush, and I am 25 years old.
```

# Positional and Keyword Arguments:
```
formatted_output = "{1} is learning {0}.".format("Python", "Piyush")
# Output: Piyush is learning Python.

formatted_output = "My name is {name}, and I am {age} years old.".format(name="Piyush", age=25)
# Output: My name is Piyush, and I am 25 years old.
```


 Comparison:
| Feature              | f-Strings                        | `format()` Method                 |
|----------------------|-----------------------------------|-----------------------------------|
| Introduced In    | Python 3.6                       | Python 2.7/3.0                   |
| Readability      | High (inline, concise syntax)     | Moderate (requires external method call) |
| Flexibility      | Supports any expressions         | Suitable for positional/keyword formatting |
| Performance      | Faster (at runtime)              | Slightly slower due to method call |


While both f-strings and the `format()` method allow for powerful formatting of strings, f-strings are generally recommended for their simplicity and performance advantages in modern Python programming.
"""