"""
Practical Example 8: Write a Python program to check if a person is eligible to donate blood 
using a nested if. 
"""

age=int(input("Enter your age : "))
weight=int(input("Enter your weight : "))

if age>18:
    if weight>50:
        print("You are eligble to donate blood 👍🏻")
    else :
        print("You are not eligble to donate blood👎🏻")
else:
    print("You are under age and not eligble to donate blood👎🏻")