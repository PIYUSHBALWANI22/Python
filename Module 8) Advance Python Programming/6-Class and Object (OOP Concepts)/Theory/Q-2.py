"""
Difference between local and global variables. 

--> Local and global variables in Python are distinguished based on their scope and lifetime.


 1. Local Variables
- Definition: Local variables are variables declared inside a function and are only accessible within that function.
- Scope: Limited to the block of code (e.g., a function) in which they are defined.
- Lifetime: The variable exists only while the function is executing. Once the function terminates, the variable is destroyed, and its memory is released.
- Theoretical Purpose: Local variables are used to store data that is specific to the execution of a particular function.

Example:
```
def my_function():
    local_var = 10  # Local variable
    print(local_var)  # Accessible within the function only

my_function()
# print(local_var)  # Error: local_var is not accessible outside the function
```


 2. Global Variables
- Definition: Global variables are variables declared outside any function and are accessible from any part of the program, including inside functions.
- Scope: Global, meaning they can be accessed from anywhere in the program.
- Lifetime: They exist throughout the program’s execution unless explicitly deleted.
- Theoretical Purpose: Global variables are used to store data that needs to be shared and accessed by multiple parts of the program.

Example:
```
global_var = 5  # Global variable

def my_function():
    print(global_var)  # Accessible inside the function

my_function()
print(global_var)  # Accessible outside the function
```


 Key Differences
| Feature            | Local Variables                      | Global Variables                    |
|--------------------|--------------------------------------|-------------------------------------|
| Defined In     | Inside a function                   | Outside all functions               |
| Scope          | Limited to the function             | Accessible throughout the program   |
| Lifetime       | Exists only during function execution| Exists for the program’s lifetime   |
| Usage Purpose  | Function-specific computations      | Shared data across functions        |
| Modification   | Directly modifiable inside the function| Must use `global` keyword for modification inside functions |


 3. Modifying Global Variables in a Function
To modify a global variable inside a function, the `global` keyword must be used to explicitly refer to the global variable.

Example:
```
counter = 0  # Global variable

def increment():
    global counter  # Access and modify the global variable
    counter += 1

increment()
print(counter)  # Outputs: 1
```

Without the `global` keyword, Python will treat the variable as a local variable and raise an error if it’s not initialized inside the function.


 Best Practices
1. Minimize Global Variables:
   - Overuse of global variables can make the program harder to debug and maintain.
2. Prefer Local Variables:
   - Use local variables for function-specific tasks to ensure modularity and prevent unintended side effects.


In conclusion, the key theoretical difference lies in their scope and lifetime, with local variables being function-specific and temporary, while global variables are accessible and persistent throughout the program’s lifecycle.
"""