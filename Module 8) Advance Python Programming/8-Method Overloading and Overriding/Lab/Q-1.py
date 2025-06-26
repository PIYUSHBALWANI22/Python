"""
Write Python programs to demonstrate method overloading and method overriding.
"""
#Method overloading
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()

print("Sum (2 arguments):", calc.add(5, 3))

print("Sum (1 argument):", calc.add(5))

print("Sum (3 arguments):", calc.add(5, 3, 2))

#Method overriding

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

animal = Animal()
dog = Dog()

animal.sound()  # Parent class method
dog.sound()     # Overridden method in child class