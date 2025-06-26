"""
Write a Python program to handle exceptions in a simple calculator (division by zero, invalid 
input). 
"""

try :
    num1=float(input("Enter the first number : "))
    num2=float(input("Enter the second number : "))

    # performing division
    result=num1/num2

except ZeroDivisionError:
    print("Error : Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
else:
    print(f"Result: {result}")
finally:
    print("Calculation complete.")