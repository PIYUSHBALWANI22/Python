"""
Function arguments (positional, keyword, default).

--> In Python, function arguments are the values you pass to a function when calling it. They determine how the
function behaves. Python supports multiple types of function arguments: positional arguments, keyword arguments,
and default arguments. Here's a detailed explanation: 

1. Positional Arguments
These are the most common type of arguments.

The order (or position) of the arguments in the function call determines which parameter receives which value.

Example:

def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

greet("Piyush", "Balwani")  # Output: Hello, Piyush Balwani!
Here, Piyush is assigned to first_name and Balwani to last_name based on their positions.

2. Keyword Arguments
With keyword arguments, the argument value is assigned to a parameter by specifying the parameter name.

The order of the arguments doesn't matter since parameters are explicitly named.

Example:

def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

greet(last_name="Balwani", first_name="Piyush")  # Output: Hello, Piyush Balwani!
Here, last_name is explicitly set to "Balwani" and first_name to "Piyush", regardless of their order.

3. Default Arguments
You can assign default values to parameters when defining a function. If no value is provided during the function call, the parameter takes the default value.

Example:

def greet(first_name, last_name="Balwani"):
    print(f"Hello, {first_name} {last_name}!")

greet("Piyush")           # Output: Hello, Piyush Balwani!
greet("Piyush", "Shah")   # Output: Hello, Piyush Shah!
In this example, last_name defaults to "Balwani" unless explicitly specified.

Combining Positional, Keyword, and Default Arguments
You can use all three types together, but the order in the function signature must be positional arguments first, followed by default arguments.

Example:

def greet(first_name, last_name="Balwani", title="Mr."):
    print(f"Hello, {title} {first_name} {last_name}!")

greet("Piyush")                      # Output: Hello, Mr. Piyush Balwani!
greet("Piyush", "Shah", title="Dr.") # Output: Hello, Dr. Piyush Shah!
Key Points to Remember
Positional arguments are assigned based on their position in the function call.

Keyword arguments require explicit naming and allow flexibility in the order of arguments.

Default arguments provide predefined values and are only overridden if values are specified.

"""