"""
Write a Python program to remove elements from a list using pop() and remove().
"""

list1=[10,20,30,"Python",50,60,70]
print(f"Before removing elements {list1}")
list1.pop(4)
list1.remove("Python")
print(f"After removing elements {list1}")