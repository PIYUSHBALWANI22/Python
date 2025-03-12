"""
Python variables and memory allocation.

-->

    PYTHON VARIABLES

        1.Defination :

            A variable is a name that references a value stored in memory.

            Variable in python are dynamically typed, meaning you don't need to declare
            the type of variable. The type is determined at runtime based on the value assigned.

        2.Assignment :

            The assignment operator " = " is used to assign a value to a variable.

            Example : x=10, name="Piyush"

        3.Type : Python variables can store values of any data type, such as integers, floats, strings,
                 lists or custom objects.

    MEMORY ALLOCATION IN PYTHON

        1.Memory Model 

            Python uses two main memory areas :

                Stack memory : 

                    Stores variable names (references).

                    Acts as a symbol table mapping variable names to memory locations of values.

                Heap memory :

                    Stores the actual object (values).

                    Allocates memory dynamically when objects are created.

        2.Object Reference 

            Variables in Python act as reference to objects in memory rather than holding the 
            value directly.

            Multiple variables can reference the same object.

            Example : 

                x=10

                y=x  # both x and y refers the same object in the memory

        3.Dynamic Memory Management

            Python's memory management is handeled by the Python Memory Manager.

            It allocates the memory for objects on the heap when created and uses techniques 
            like garbage collection to free unused memory.

    GARBAGE COLLECTION 

        1.Defination :

            Garbage collection is the process of automatically deallocating memory for objects 
            that are no longer use.

            Python uses refrence counting and cyclic garbage collector.

        2.Reference counting :

            Each object has a reference count that tracks how many variable refrence it.

            When the reference count drops to zero, the memory is deallocated.

        3.Cyclic garbage collector :

            Detects and cleans up reference cycles (e.g. objects referencing each other). 
"""