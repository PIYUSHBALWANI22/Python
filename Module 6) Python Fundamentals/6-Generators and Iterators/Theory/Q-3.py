"""
Understanding iterators and creating custom iterators.

--> Iterators are fundamental concept in programing that allows sequential access to the elements in a collection 
    without exposing its underlying respresentation. Here's an overview of understanding iterators and creating cutsom 
    iterators :

    Understanding Iterators 

        1) What is an Iterator?

            An iterator is an object that enables traversing through all the elements of a collection (like lists, tuples, or dictionaries) one element at a time.

            Iterators adhere to the Iterator Protocol, meaning they must implement two methods:

            __iter__(): Returns the iterator object itself.

            __next__(): Returns the next element from the collection. If no more elements are present, it raises a StopIteration exception. 

        2) How Iterators Work

            When you create an iterator, it maintains the state of where it is in the collection.

            This ensures that elements can be accessed one by one, without needing to know the structure or size of the collection.

            Iterators are often used with loops (like for in Python) for convenience.

        3) Difference Between Iterable and Iterator

            Iterable: Any object that can return an iterator (e.g., lists, dictionaries). They have an __iter__() method.

            Iterator: An object that can be iterated upon. It keeps track of the current position and has both __iter__() and __next__() methods.


    Creating Custom Iterators

        Custom iterators are helpful when you want to define your own way to iterate over data or objects. Here's the process for creating one:

        1) Define a Class : 

            Create a class that represents your custom collection or data structure.

        2) Implement the __iter__() Method :

            This method should return the iterator object. In most cases, this is self.

        3) Implement the __next__() Method

            Define how the next element is retrieved.

            Keep track of the current position in the collection using an instance variable.

            When there are no more items to return, raise a StopIteration exception.
"""