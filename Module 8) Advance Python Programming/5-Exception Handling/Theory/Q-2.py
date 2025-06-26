"""
Understanding multiple exceptions and custom exceptions.

-->  Understanding Multiple Exceptions

When working with exceptions in Python, there are scenarios where multiple types of exceptions might arise. Python allows us to handle multiple exceptions effectively by associating different exception types with separate `except` blocks or combining them into a single block.

---

# Handling Multiple Exceptions with Separate `except` Blocks
In this approach, each potential exception is caught and handled individually with its own `except` block.

Example:
```
try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    result = numerator / denominator
    print(f"The result is {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid numeric inputs.")
```

Here:
- `ZeroDivisionError` is handled if the denominator is zero.
- `ValueError` is handled if non-numeric input is entered.


# Handling Multiple Exceptions in a Single Block
You can combine multiple exceptions into a single `except` block by grouping them in a tuple.

Example:
```
try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    result = numerator / denominator
    print(f"The result is {result}")
except (ZeroDivisionError, ValueError) as e:
    print(f"Error occurred: {e}")
```


 Custom Exceptions

Custom exceptions allow developers to create their own specific exception types that represent unique error conditions in their application. These exceptions are defined by subclassing the built-in `Exception` class.


# Why Use Custom Exceptions?
1. To represent application-specific errors.
2. To make exception handling more meaningful and structured.
3. To improve code readability and maintainability.


# Defining and Raising Custom Exceptions
You can create a custom exception by subclassing the `Exception` class and raising it as needed.

Example:
```python
# Define a custom exception
class NegativeValueError(Exception):
    def __init__(self, message="Negative values are not allowed."):
        self.message = message
        super().__init__(self.message)

# Use the custom exception
try:
    number = int(input("Enter a positive number: "))
    if number < 0:
        raise NegativeValueError("You entered a negative value.")
    print(f"Your number is {number}")
except NegativeValueError as e:
    print(f"Custom Exception: {e}")
```


# Combining Custom Exceptions with Multiple Exceptions
Custom exceptions can also be combined with built-in exceptions for robust error handling.

Example:
```
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be between 0 and 120."):
        self.message = message
        super().__init__(self.message)

try:
    age = int(input("Enter your age: "))
    if age < 0 or age > 120:
        raise InvalidAgeError("Age must be a realistic value.")
except (ValueError, InvalidAgeError) as e:
    print(f"Error: {e}")
```


 Key Considerations
1. Prioritize Specificity: Handle specific exceptions before generic ones.
2. Error Descriptions: Provide meaningful error messages to improve debugging.
3. Custom Exceptions: Use them for complex or domain-specific error scenarios.

By handling multiple exceptions and defining custom exceptions, you can make your programs theoretically more robust, clear, and easier to debug.
"""