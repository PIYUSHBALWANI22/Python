"""
Practical Example 5: Write a Python program to find greater and less than a number using 
if_else.
"""

 
num = int(input("Enter a number: "))
 
x = 10

if num > x:
    print(f"{num} is greater than {x}.")
elif num < x:
    print(f"{num} is less than {x}.")
else:
    print(f"{num} is equal to {x}.")
