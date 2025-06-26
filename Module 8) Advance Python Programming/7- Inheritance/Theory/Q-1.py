"""
Single, Multilevel, Multiple, Hierarchical, and Hybrid inheritance in Python.

--> Inheritance is a cornerstone concept of Object-Oriented Programming (OOP) in Python, enabling a class to acquire properties and methods from another class. Python supports various types of inheritance to model relationships between classes effectively.


 1. Single Inheritance
- Definition: Involves one child class inheriting from a single parent class.
- Purpose: Enables the reuse of code and creates a straightforward parent-child relationship.

Example:
```
class Parent:
    def greet(self):
        print("Hello from the Parent class!")

class Child(Parent):  # Inheriting from Parent
    def say_hello(self):
        print("Hello from the Child class!")

child = Child()
child.greet()  # Outputs: Hello from the Parent class!
child.say_hello()  # Outputs: Hello from the Child class!
```


 2. Multilevel Inheritance
- Definition: Involves a chain of inheritance where a class inherits from another class, which itself inherits from yet another class.
- Purpose: Models a linear hierarchy, enabling each level to build upon the previous one.

Example:
```
class Grandparent:
    def grandparent_method(self):
        print("Method from the Grandparent class.")

class Parent(Grandparent):  # Inheriting from Grandparent
    def parent_method(self):
        print("Method from the Parent class.")

class Child(Parent):  # Inheriting from Parent
    def child_method(self):
        print("Method from the Child class.")

child = Child()
child.grandparent_method()  # Outputs: Method from the Grandparent class.
child.parent_method()  # Outputs: Method from the Parent class.
child.child_method()  # Outputs: Method from the Child class.
```


 3. Multiple Inheritance
- Definition: Involves a class inheriting from more than one parent class.
- Purpose: Enables a child class to inherit features from multiple sources.

Example:
```
class Parent1:
    def method1(self):
        print("Method from Parent1.")

class Parent2:
    def method2(self):
        print("Method from Parent2.")

class Child(Parent1, Parent2):  # Inheriting from both Parent1 and Parent2
    def child_method(self):
        print("Method from Child class.")

child = Child()
child.method1()  # Outputs: Method from Parent1.
child.method2()  # Outputs: Method from Parent2.
child.child_method()  # Outputs: Method from Child class.
```

> Note: In the case of conflicts (e.g., methods with the same name), Python resolves them using the Method Resolution Order (MRO), following a depth-first, left-to-right approach.


 4. Hierarchical Inheritance
- Definition: Involves multiple child classes inheriting from the same parent class.
- Purpose: Models situations where multiple derived classes share the same base class.

Example:
```
class Parent:
    def parent_method(self):
        print("Method from the Parent class.")

class Child1(Parent):  # Inheriting from Parent
    def child1_method(self):
        print("Method from Child1 class.")

class Child2(Parent):  # Inheriting from Parent
    def child2_method(self):
        print("Method from Child2 class.")

child1 = Child1()
child1.parent_method()  # Outputs: Method from the Parent class.
child1.child1_method()  # Outputs: Method from Child1 class.

child2 = Child2()
child2.parent_method()  # Outputs: Method from the Parent class.
child2.child2_method()  # Outputs: Method from Child2 class.
```


 5. Hybrid Inheritance
- Definition: Combines two or more types of inheritance into a single model.
- Purpose: Provides flexibility to create complex class relationships.

Example:
```
class Parent:
    def parent_method(self):
        print("Method from the Parent class.")

class Child1(Parent):  # Single Inheritance
    def child1_method(self):
        print("Method from Child1 class.")

class Child2(Parent):  # Single Inheritance
    def child2_method(self):
        print("Method from Child2 class.")

class GrandChild(Child1, Child2):  # Multiple Inheritance
    def grandchild_method(self):
        print("Method from the GrandChild class.")

grandchild = GrandChild()
grandchild.parent_method()  # Outputs: Method from the Parent class.
grandchild.child1_method()  # Outputs: Method from Child1 class.
grandchild.child2_method()  # Outputs: Method from Child2 class.
grandchild.grandchild_method()  # Outputs: Method from the GrandChild class.
```

> Note: Just as with multiple inheritance, MRO plays a critical role in resolving method or attribute conflicts in hybrid inheritance.


 Summary of Inheritance Types

| Type          | Number of Parents       | Number of Levels | Key Feature                                     |
|--------------------|-----------------------------|-----------------------|----------------------------------------------------|
| Single         | One parent, one child       | Single level          | Straightforward parent-child relationship          |
| Multilevel     | Single parent-child chain   | Multiple levels       | Models linear inheritance hierarchy               |
| Multiple       | Two or more parents         | Single or multiple    | Inherits from multiple sources simultaneously     |
| Hierarchical   | One parent, multiple children| Single level          | Multiple classes share a common base class        |
| Hybrid         | Combination of types        | Flexible              | Creates complex inheritance models                |

---

In theory, inheritance allows Python programmers to design modular, reusable, and scalable code. Each type of inheritance serves specific design patterns, enabling efficient modeling of real-world hierarchies and relationships.
"""