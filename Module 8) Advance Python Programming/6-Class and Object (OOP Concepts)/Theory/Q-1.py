"""
Understanding the concepts of classes, objects, attributes, and methods in Python. 

--> In Python, the concepts of classes, objects, attributes, and methods are foundational to Object-Oriented Programming (OOP). Theoretically, they enable the modeling of real-world entities, behaviors, and relationships within code.


 1. Classes
- Definition: A class is a blueprint or template for creating objects. It defines the structure and behavior (attributes and methods) that objects of the class will have.
- Theoretical Purpose: Classes encapsulate data and functionality into a single logical unit, promoting modularity and code reuse.

Syntax:
```
class ClassName:
    # Class body: attributes and methods
    pass
```

Example:
```
class Car:
    wheels = 4  # Class attribute
    def start(self):  # Method
        print("The car has started.")
```


 2. Objects
- Definition: An object is an instance of a class. It is a concrete representation of the class, with its own specific data and the ability to perform actions (methods).
- Theoretical Purpose: Objects provide a way to use and manipulate the data and behavior defined in the class.

Syntax:
```
object_name = ClassName()
```

Example:
```
my_car = Car()  # Create an object of the Car class
print(my_car.wheels)  # Access the class attribute (Output: 4)
my_car.start()  # Call the method (Output: The car has started.)
```


 3. Attributes
- Definition: Attributes are variables associated with a class or object. They store the data or state of an object.
- Types:
  - Class Attributes: Shared by all objects of the class.
  - Instance Attributes: Unique to each object, defined inside the class's methods (typically `__init__`).

Syntax:
```
class ClassName:
    class_attribute = value  # Class attribute
    def __init__(self, param):
        self.instance_attribute = param  # Instance attribute
```

Example:
```
class Person:
    species = "Homo sapiens"  # Class attribute
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age

p1 = Person("Alice", 30)
p2 = Person("Bob", 25)
print(p1.name, p1.age)  # Outputs: Alice 30
print(Person.species)   # Outputs: Homo sapiens
```


 4. Methods
- Definition: Methods are functions defined inside a class that describe the behavior or actions of the class and its objects. They operate on the attributes of the class or object.
- Types:
  - Instance Methods: Require an object to call and often work with instance attributes (`self` refers to the specific object).
  - Class Methods: Use `@classmethod` decorator and work with class attributes (`cls` refers to the class).
  - Static Methods: Use `@staticmethod` decorator and do not access class or instance attributes directly.

Syntax:
```
class ClassName:
    def instance_method(self, args):
        # Behavior or actions
        pass
```

Example:
```
class Calculator:
    def add(self, x, y):  # Instance method
        return x + y
    @classmethod
    def info(cls):  # Class method
        print("This is a Calculator class.")
    @staticmethod
    def greet():  # Static method
        print("Hello from Calculator!")

calc = Calculator()
print(calc.add(5, 3))  # Outputs: 8
Calculator.info()  # Outputs: This is a Calculator class.
Calculator.greet()  # Outputs: Hello from Calculator!
```


 Relationships Between These Concepts
1. A class defines a template.
2. An object is an instance of that template.
3. The attributes describe the data of the object.
4. The methods define the behavior or actions of the object.


 Key Advantages
- Encapsulation: Combines data (attributes) and behavior (methods) in a single unit.
- Modularity: Allows breaking down complex problems into simpler, manageable components.
- Code Reuse: Classes and objects can be reused across different programs.

Theoretically, this combination of classes, objects, attributes, and methods forms the backbone of OOP, enabling developers to write clean, reusable, and extensible code.
"""