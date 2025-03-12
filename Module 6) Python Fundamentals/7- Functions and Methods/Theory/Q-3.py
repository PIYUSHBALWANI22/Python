"""
Scope of variables in Python. 

--> The scope of variables in Python defines the part of the program where a variable is accessible and can be used. Python follows the LEGB (Local, Enclosing, Global, Built-in) rule to determine the scope of variables. Here's a theoretical overview:

1. Local Scope
A variable declared inside a function belongs to the local scope and is accessible only within that function.

It is created when the function is called and is destroyed when the function exits.

Example: Variables defined inside functions.

2. Enclosing Scope
This refers to variables defined in the enclosing function (a function containing a nested function). These variables are not global but can be accessed by the nested function.

It is often referred to as a nonlocal scope.

Example: Variables in outer functions of a nested function.

3. Global Scope
Variables defined outside any function or block belong to the global scope. They are accessible throughout the program unless overshadowed by a local variable of the same name.

To modify a global variable inside a function, the global keyword must be used.

Example: Variables defined at the top level of a program or module.

4. Built-in Scope
This is the outermost scope containing all the built-in names in Python, such as len() and print().

These names are always available, but it's advisable not to override them.

LEGB Rule
When Python encounters a variable, it searches for its value in the following order:

Local Scope: Inside the current function.

Enclosing Scope: In the function(s) enclosing the current function.

Global Scope: At the top level of the module or script.

Built-in Scope: Python's predefined built-in namespace.

If the variable is not found in any of these scopes, a NameError is raised.

Important Notes
The global keyword allows modifying global variables inside a function.

The nonlocal keyword is used to modify variables in the enclosing (non-global) scope.
"""