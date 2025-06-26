"""
Creating custom modules. 

--> Theoretically, creating custom modules in Python involves encapsulating reusable code into separate `.py` files, which can then be imported and used in other programs. Here's a breakdown of the concept:


 Steps to Create a Custom Module:

1. Create a Python File:
   - Write your Python code (functions, classes, variables, etc.) in a file with the `.py` extension. For example, you might name it `my_module.py`.

2. Define Functions and Variables:
   - Include the code you want to reuse. This could include utility functions, constants, or specific classes.

3. Save the File:
   - Place your module file in the same directory as the program that will import it, or ensure it’s in the Python environment’s search path.

4. Import the Module:
   - In another Python script, use the `import` statement to include your module. You can then access its functions, classes, or variables.


 Example (Theoretical):

Suppose you create a module called `math_utils.py`:

```
# math_utils.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

To use this module in another script:

```
# main.py
import math_utils

result = math_utils.add(10, 5)
print(result)  # Output: 15
```

 Additional Notes:
- Custom Path: If your module is in a different directory, you may need to adjust the `PYTHONPATH` environment variable or use relative imports.
- Best Practices: Keep your modules focused and well-documented to make them easy to understand and maintain.
- Packaging: For larger projects, you can organize multiple modules into packages by placing them in a directory with an `__init__.py` file.

Custom modules are an essential aspect of writing clean, modular, and scalable Python code.
"""