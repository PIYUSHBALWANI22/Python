"""
Write a Python program to generate random numbers using the random module.
"""
import random

randInt=random.randint(1,100)
print(f"Random integer (1-100): {randInt}")

randFloat=random.random()
print(f"Random float (0-1): {randFloat}")

randRange=random.randrange(10,100,5)
print(f"Random number (10-100, step 5): {randRange}")

list=["BMW", "Mercedes", "Pagani", "TATA"]
randChoice=random.choice(list)
print(f"Random choice from list : {randChoice}")