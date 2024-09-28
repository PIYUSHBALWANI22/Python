#What is the purpose continue statement in python?

"""
Ans--> In Python, the continue statement is used within loops (for and while) to skip the current 
iteration and move on to the next one. When the continue statement is encountered, any code 
following it within the loop's body is ignored for that iteration, and the loop proceeds 
with the next cycle. 
For example..
"""

for i in range(1,10):
    if i%2==0:
        continue
    print(i)