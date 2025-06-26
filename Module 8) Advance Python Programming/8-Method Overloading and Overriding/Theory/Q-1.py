"""
Method overloading: defining multiple methods with the same name but different 
parameters. 

--> Method overloading is a concept in object-oriented programming that allows multiple methods with the same name but different parameters to coexist within the same class. It enables methods to be designed to perform similar or related actions but on different input data.


 Theoretical Explanation of Method Overloading

1. Definition:
   - Method overloading involves defining multiple methods with the same name but differing in the number, type, or sequence of parameters.
   - It increases the flexibility and readability of a program by allowing a single method name to handle a variety of input data types or formats.

2. Purpose:
   - To simplify and standardize the method names in a class.
   - To enable methods to handle different use cases or input data formats without requiring unique names for each variation.

3. Example in Other Languages:
   - Some languages like Java or C++ explicitly support method overloading as part of their syntax, where multiple methods with the same name can exist in a class but must differ in their parameter list.


 Method Overloading in Python

Python does not support method overloading in the traditional sense as other languages do. If multiple methods with the same name are defined in a Python class, the last one overrides all previous definitions. However, method overloading can be simulated using techniques like:

1. Default Arguments:
   You can achieve method overloading by using default argument values to handle variations in the input.

   Example:
   ```
   class Calculator:
       def add(self, a, b=0):  # Default value for the second parameter
           return a + b

   calc = Calculator()
   print(calc.add(5))       # Outputs: 5 (only one argument provided)
   print(calc.add(5, 3))    # Outputs: 8 (two arguments provided)
   ```

2. Variable-Length Arguments:
   The `*args` and `kwargs` syntax allows a method to accept a variable number of positional or keyword arguments, emulating overloading.

   Example:
   ```
   class Calculator:
       def multiply(self, *args):  # Accepts any number of arguments
           result = 1
           for num in args:
               result *= num
           return result

   calc = Calculator()
   print(calc.multiply(2, 3))      # Outputs: 6
   print(calc.multiply(2, 3, 4))   # Outputs: 24
   ```

3. Explicit Parameter Checking:
   The method can inspect the type and number of arguments at runtime to behave differently based on input.

   Example:
   ```
   class Greeting:
       def greet(self, person=None):
           if person is None:
               print("Hello, World!")
           else:
               print(f"Hello, {person}!")

   greeter = Greeting()
   greeter.greet()           # Outputs: Hello, World!
   greeter.greet("Piyush")   # Outputs: Hello, Piyush!
   ```


 Key Differences Between Python and Traditional Method Overloading

| Feature                  | Python                                   | Traditional OOP (e.g., Java, C++)    |
|--------------------------|------------------------------------------|-------------------------------------|
| Support for Overloading | Indirect, using default or variable arguments | Directly supported                 |
| Behavior             | Only the last-defined method is retained | Multiple methods can coexist        |
| Flexibility          | More dynamic, resolved at runtime        | Static, resolved at compile-time    |


 Advantages of Method Overloading
1. Simplifies method naming by grouping related actions under a single name.
2. Increases code readability and maintainability.
3. Provides flexibility for handling different types or numbers of inputs.

 Limitations in Python
- Overloading is not natively supported, so developers need to implement workarounds.
- If not carefully implemented, simulation of overloading can make code harder to debug.

In summary, while Python does not support method overloading in the traditional sense, it provides dynamic tools like default arguments, variable-length arguments, and runtime checks to emulate the behavior and achieve similar functionality. This aligns with Python's design philosophy of simplicity and flexibility.
"""