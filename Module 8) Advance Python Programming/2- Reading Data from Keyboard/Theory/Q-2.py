"""
Converting user input into different data types (e.g., int, float, etc.). 

--> Converting user input into different data types is essential for handling and processing user-entered data correctly. Since the `input()` function in Python always returns the user input as a string, theoretical conversion methods are required to manipulate or process input as other data types.

---

 Theoretical Explanation of Data Type Conversion

1. `int()`:
   - Converts the string input into an integer.
   - Useful when working with whole numbers.
   - If the input contains non-numeric characters, a `ValueError` is raised.

   Example:
   ```
   age = input("Enter your age: ")  # User enters "25"
   age = int(age)  # Converts the string "25" into the integer 25.
   ```

2. `float()`:
   - Converts the string input into a floating-point number.
   - Ideal when dealing with decimal values.

   Example:
   ```
   height = input("Enter your height in meters: ")  # User enters "5.8"
   height = float(height)  # Converts the string "5.8" into the float 5.8.
   ```

3. `bool()`:
   - Converts the string into a boolean.
   - Any non-empty string evaluates to `True`, while an empty string evaluates to `False`.

   Example:
   ```
   response = input("Do you agree? (yes/no): ")  # User enters "yes"
   agreement = bool(response)  # Converts "yes" to True.
   ```

4. `list()` or `tuple()`:
   - Converts user input into a list or tuple. Requires the input to be preformatted as a string that can be split.

   Example:
   ```
   items = input("Enter comma-separated values: ")  # User enters "1,2,3"
   items_list = items.split(",")  # ['1', '2', '3']
   items_tuple = tuple(items_list)  # ('1', '2', '3')
   ```

5. `eval()` (Theoretical Only):
   - Evaluates user input as a Python expression.
   - While it theoretically offers flexibility (e.g., converting strings to integers, floats, or other objects), it is considered insecure and should be avoided in practice due to potential code injection risks.

   Example (not recommended in practice):
   ```
   value = input("Enter a value: ")  # User enters "10"
   converted_value = eval(value)  # Interprets "10" as an integer.
   ```

---

 Combining Type Conversion with Error Handling
To avoid runtime errors during conversion, it's essential to validate or handle exceptions theoretically.

Example:
```
user_input = input("Enter a number: ")
try:
    number = int(user_input)
    print(f"Converted to integer: {number}")
except ValueError:
    print("Invalid input! Please enter a valid number.")
```


 Summary
Theoretically, type conversion of user input allows flexibility to manipulate the data based on the program's requirements. Using built-in functions like `int()`, `float()`, or `bool()` ensures the data aligns with its intended use. Proper validation and error handling are critical to ensure robust user interaction.
"""