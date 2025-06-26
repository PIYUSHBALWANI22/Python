"""
How to check the type of a variable dynamically using type().

--> 
    In python, the built-in type() function is used to determine the type of variable dynamically
    at runtime. This can help you understand the datatype of variable during execution.

    Syntax : type(variable)

    vriable : The Variable whose type wants to be check.

    Returns : The type of the variable as a class object.

    Examples : 

        1.Checking basic datatypes 

            num = 14
            print(type(num)) # Output: <class 'int'>

            pi = 3.14
            print(type(pi))  # Output: <class 'float'>

            name = "Alice"
            print(type(name))  # Output: <class 'str'>

            is_valid = True
            print(type(is_valid))  # Output: <class 'bool'>

        2.Checking complex datatypes

            fruits = ["Apple", "Banana", "Cherry"]
            print(type(fruits))  # Output: <class 'list'>

            dimensions = (1920, 1080)
            print(type(dimensions))  # Output: <class 'tuple'>

            person = {"name": "Alice", "age": 30}
            print(type(person))  # Output: <class 'dict'>

            unique_numbers = {1, 2, 3, 3}
            print(type(unique_numbers))  # Output: <class 'set'>

"""