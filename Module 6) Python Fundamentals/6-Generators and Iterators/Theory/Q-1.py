"""
Understanding how generators work in Python.
-->  
     Generators in python are a special type of iterable, like lists or tuples, but they differ in how they produce
     their elements. They allow for efficient computation by generating items one at a time, rather than computing 
     all items at once and sroring them in memeory. 


     1) What are Generators?

            Generators are functions that return an itreator and use the yield keyword to produce a sequence of values 
            lazily, one at a time.

            Unlike normal functions that terminate with a return statement, a generator function saves its safe after 
            each yield and can resume from where it left off.

    2) Key features of Generators

            Lazy evaluation : Generators produce items only when requested, saving memory and improving performance,
            especially for large data sets.

            State preservation : After yielding a value, the function pauses execution and retains local variable,
            so it can coninue from the same point when called again.

            Efficient iteration : No need to compute or store all items at once.

    3) Benefits of Generators 

            Memory Efficiency : Generatord produce one item at a time, making them ideal for large data sets or infinite sequences 
            where stroing the entire list in memory would be impractical.

            Lazy Evaluation : Only generate values as needed, which can lead to performance improvemnts in scenarios where some
            values may never be used.

            Cleaner Code : Often, generators can replace complex itrator logic whith cleaner, more initutive function.

    4) Generators Expressions 

            Similar to list comprehensions, Python also supports a concise syntax to create generators using parantheses instead of
            suqare brackets :

            # Generator expression to yield squares of numbers from 0 to 9
            squares = (x * x for x in range(10))

            This expression creates a generator that computes each square on demand.

    5) When and why to use Generator

            Large Data Sets : When processing huge files or data streams where loading the entire content into memory would be inefficient.

            Infinite Sequence : Generators can model infinite data streams(e.g., continually reading from a network socket) without
            exhausting memory since they generate one element at a time. 

            Data Pipelines : They enable the building of pipelines where data is transformed step-by-step, thus simplifying operations like 
            filtering or mapping without needing intermidate list.

            Generators are a cornerstone of Python's approach to handling itreation and are particularly invaluable in data processing,
            stream handling, and scenarios requiring lazy evaluation. Their ability to pause and resume seamlessly makes your programs 
            flexible, efficient, and often more readable.

"""