"""
Introduction to closures and decorators. 

--> In Python, closures and decorators are advanced concepts related to functions that enhance code modularity, reusability, and maintainability.

Closures
A closure is a function that captures and remembers the variables from its enclosing scope, even after that scope has finished executing. 
This allows a function to maintain state information across multiple calls without using global variables or class instances. 
Closures are created when a nested (inner) function references variables from its outer function.

Key Characteristics of Closures:
The inner function must be defined inside an outer function.
The inner function must reference variables from the outer function.
The outer function must return the inner function.
Closures are useful for data encapsulation, function factories, and callback mechanisms.

Decorators
A decorator is a higher-order function that takes another function as input and extends or modifies its behavior without 
changing its actual code. 
In Python, decorators are commonly used for tasks such as logging, enforcing access control, authentication, 
and performance measurement.

Decorators work by wrapping a function inside another function, allowing additional functionality to be executed before or after
 the original function runs.
Python provides built-in decorators such as @staticmethod, @classmethod, and @property, and also allows the creation of custom 
decorators.

Key Characteristics of Decorators:
They modify the behavior of functions without altering their structure.
They are implemented using function closures.
They are applied using the @decorator_name syntax.
Both closures and decorators leverage Python’s first-class functions feature, meaning functions can be passed as arguments,
 returned from other functions, and assigned to variables. These concepts help make Python code more efficient, flexible, 
 and maintainable.
"""
