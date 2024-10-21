#How memory is managed in Python?

"""
Ans-->  In python memory management is handeled automatically by python memmory manager.

1) Memory allocation :
      stack memory-> used for managing functions calls and variables. it holds references to objects but
      not the object themselves.
      heap memory-> where objects like integers,lists and dictionary are stored. The heap is dynamically
      allocated and python handels the allocation of the objects in the heap automatically.

2) Memory manager : python's memory manager takes care of allocating and deallocating memory it is divided into
                    diffrent layers :
            
      1) Object-specific memory managers: Handle specialized object types like integers and strings.

      2) General-purpose memory manager: Handles the allocation of larger objects and structures, like complex user-defined objects.

      The PyObject_Malloc function is used for most allocations. Python uses an internal memory pool mechanism called PyMalloc to manage small objects efficiently.

3) Garbage Collection : Python uses automatic garbage collection to clean up memory that is no longer in use
                        preventing memory leaks. The key mechanism for this is :

      1) Reference Counting: Each object in Python has a reference count, which tracks how many references point to it. When this count drops to zero, the memory for the object is automatically freed.

      2) Cycle Detector: Python's garbage collector also deals with cyclic references (objects referencing each other in a cycle, preventing the reference count from reaching zero). Python’s cyclic garbage collector (part of the gc module) runs periodically to clean up objects involved in these cycles.

4) Memory Management Tools : Python provides built-in modules and functions to help manage memory:

                  gc module: This allows control over the garbage collector, including functions like gc.collect() to manually trigger garbage collection.

                  sys module: Functions like sys.getsizeof() can be used to get the size of objects in bytes.

5) Memory Optimization : 

      1) Interning: Python applies interning for certain small immutable objects (like small integers and strings) to save memory by reusing objects.

      2) Object Pools: Python optimizes memory usage for small objects (objects smaller than 256 bytes) by pooling memory blocks, reducing overhead.

In general, Python abstracts away much of the low-level memory management, allowing developers to focus on writing code without worrying about manual memory allocation and deallocation.
"""
