"""
Practical Example 7: Write a Python program to calculate grades based on percentage using 
if-else ladder. 
"""

percentage=float(input("Enter your percentage : "))

if percentage<=100 and percentage>=90:
    print(f"Your grade is A with percentage {percentage}")
elif percentage<90 and percentage>=60:
    print(f"Your grade is B with percentage {percentage}")
elif percentage<60 and percentage>=35:
    print(f"Your grade is c with percentage {percentage}")

else :
    print("Fail..🤡")