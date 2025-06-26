"""
Using the super() function to access properties of the parent class.

--> The `super()` function in Python is used to give access to the properties and methods of a parent class from within a child class. It is a powerful feature of Object-Oriented Programming (OOP) that enables seamless inheritance and method overriding.


 Theoretical Explanation of `super()`

1. Definition:
   - The `super()` function returns a proxy object that allows you to refer to the parent class without explicitly naming it.
   - It is primarily used to call a parent class's method or constructor (`__init__`) within the child class.

2. Theoretical Purpose:
   - Avoids explicitly naming the parent class, making code more maintainable and less prone to errors when the parent class name changes.
   - Supports the Method Resolution Order (MRO) in multiple inheritance, ensuring that the correct parent method is called in the proper order.


 Syntax:
```
super().method_name(arguments)
```
Here:
- `method_name`: Refers to the method or property of the parent class you want to access.
- `arguments`: Represents the parameters passed to the parent class's method or constructor.


 1. Using `super()` to Call Parent Class Constructor

When a child class needs to initialize the attributes of its parent class, `super()` is used to call the parent class's constructor.

Example:
```
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call Parent's __init__
        self.age = age

child = Child("Piyush", 25)
print(child.name)  # Outputs: Piyush
print(child.age)   # Outputs: 25
```


 2. Using `super()` to Access Parent Class Methods

The `super()` function can also be used to invoke specific methods of the parent class.

Example:
```
class Parent:
    def greet(self):
        print("Hello from Parent!")

class Child(Parent):
    def greet(self):
        super().greet()  # Call Parent's greet method
        print("Hello from Child!")

child = Child()
child.greet()
# Outputs:
# Hello from Parent!
# Hello from Child!
```


 3. `super()` in Multiple Inheritance

In cases of multiple inheritance, `super()` resolves the Method Resolution Order (MRO), ensuring that parent classes are called in the correct linear hierarchy.

Example:
```
class A:
    def method(self):
        print("Method from Class A")

class B(A):
    def method(self):
        print("Method from Class B")
        super().method()  # Call A's method

class C(B):
    def method(self):
        print("Method from Class C")
        super().method()  # Call B's method

c = C()
c.method()
# Outputs:
# Method from Class C
# Method from Class B
# Method from Class A
```
Here, `super()` ensures the parent methods are called following the C3 Linearization Algorithm.


 Advantages of `super()`
1. Code Maintainability: Avoids hardcoding the parent class name, making the code dynamic.
2. MRO Support: Guarantees correct method execution order in multiple inheritance scenarios.
3. Reusability: Facilitates access to parent class properties and methods without re-implementing them.


In conclusion, the `super()` function is a cornerstone feature for managing inheritance effectively. It simplifies access to parent class functionality, ensuring structured and maintainable code when building complex class hierarchies.
"""