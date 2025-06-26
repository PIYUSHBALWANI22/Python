"""
Write Python programs to demonstrate different types of inheritance (single, multiple, 
multilevel, etc.).
"""

class Animal:
    def speak(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def bark(self):
        print("Dog barks.")

dog = Dog()
dog.speak()  # Inherited method
dog.bark()   # Own method