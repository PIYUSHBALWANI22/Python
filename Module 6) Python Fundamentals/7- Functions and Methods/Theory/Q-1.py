"""
Defining and calling functions in Python.

--> In Python, functions are reusable blocks of code that perform a specific task. They are defined using the def keyword, followed by
    the function name, parentheses (which may contain parameters), and a colon. The function body contains the code that executes when the
    function is called.

    Defining Functions 

        To create a function, use the following syntax:

        def function_name(parameters):
        return result  

        function_name is the name of the function.

        parameters are optional values passed to the function when it is called. These are used as input for the function's operations.

        The return statement is optional and is used to send a result back to the calling code.

    Calling Functions 

        To execute a function, you simply use its name followed by parentheses. If the function accepts parameters, provide the required arguments inside the parentheses.

            Example:

            def greet(name):
                print(f"Hello, {name}!")

            greet("Piyush")
            Output: Hello, Piyush !

    Key Points

        Reusability: Functions can be reused multiple times in the code, reducing redundancy.

            Parameters and Arguments: Functions can take input (parameters) and use them to perform operations.

            Return Values: Functions can return results, making them versatile for complex operations. Example:

            python
            def add(a, b):
                return a + b

            result = add(3, 5)
            print(result)  # Outputs: 8
            Built-in vs. User-defined Functions:

            Python has built-in functions like print() and len().

            User-defined functions are created by the programmer as needed.

            Scope and Lifetime: Variables within a function have local scope, meaning they are only accessible within the function.

            Functions make code modular, easier to read, and maintainable.
"""