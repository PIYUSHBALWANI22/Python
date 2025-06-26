"""
Method overriding: redefining a parent class method in the child class.

-->  Method Overriding in Python

Method overriding is a feature of inheritance in Python that allows a child class to redefine a method inherited from its parent class. This enables the child class to provide a specific implementation of the method while retaining the method's name and interface.


 Theoretical Explanation

1. Definition:
   - In method overriding, a method in the child class has the same name, parameters, and signature as a method in the parent class.
   - The implementation in the child class overrides the parent class method when called on an instance of the child class.

2. Purpose:
   - To customize or extend the behavior of a parent class's method in the child class.
   - Enables polymorphism by allowing objects of different classes to be treated uniformly while exhibiting different behavior.


 Key Features of Method Overriding
- Inheritance Required: The child class must inherit from the parent class.
- Same Method Signature: The overriding method must have the same name and parameters as the parent method.
- Parent Class Access: The parent class method can still be accessed using the `super()` function or by explicitly calling the parent class's method.


 Example of Method Overriding

Example 1: Redefining the Method in the Child Class
```
class Parent:
    def show_message(self):
        print("Message from the Parent class.")

class Child(Parent):
    def show_message(self):
        print("Message from the Child class.")

child = Child()
child.show_message()  # Outputs: Message from the Child class.
```
- The `show_message()` method in the `Child` class overrides the method from the `Parent` class.


Example 2: Accessing the Parent Method Using `super()`
```
class Parent:
    def show_message(self):
        print("Message from the Parent class.")

class Child(Parent):
    def show_message(self):
        super().show_message()  # Calls the Parent's method
        print("Message from the Child class.")

child = Child()
child.show_message()
# Outputs:
# Message from the Parent class.
# Message from the Child class.
```
- The `super().show_message()` call invokes the parent class's implementation before executing the child class's overridden method.


Example 3: Polymorphism with Method Overriding
Polymorphism allows us to write code that works with objects of different classes, treating them uniformly.

```
class Animal:
    def speak(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def speak(self):
        print("The dog barks.")

class Cat(Animal):
    def speak(self):
        print("The cat meows.")

def make_animal_speak(animal):
    animal.speak()

dog = Dog()
cat = Cat()

make_animal_speak(dog)  # Outputs: The dog barks.
make_animal_speak(cat)  # Outputs: The cat meows.
```
- Here, the `speak()` method is overridden in both `Dog` and `Cat` classes, and the correct method is called depending on the type of object passed.


 Key Differences: Overriding vs Overloading
| Feature              | Method Overriding                 | Method Overloading                 |
|----------------------|------------------------------------|------------------------------------|
| Definition       | Redefining a method in the child class | Same method name but different parameters |
| Inheritance      | Requires inheritance              | Doesn't require inheritance        |
| Method Signature | Must remain the same              | Can differ in parameters           |


 Advantages of Method Overriding
1. Flexibility: Allows child classes to customize inherited behaviors.
2. Polymorphism: Supports polymorphic behavior where the method called depends on the object type.
3. Code Reusability: Enables code reuse from parent classes while tailoring methods for specific needs.

In conclusion, method overriding is a crucial aspect of inheritance and polymorphism in Python, enabling developers to create highly flexible and maintainable object-oriented programs.
"""