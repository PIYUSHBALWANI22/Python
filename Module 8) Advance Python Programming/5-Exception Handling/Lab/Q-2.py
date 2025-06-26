"""
Write a Python program to demonstrate handling multiple exceptions.
"""

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = num1 / num2
    
    with open("example.txt", "r") as file:
        content = file.read()
        print("\nFile Content:\n", content)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
except FileNotFoundError:
    print("Error: The file 'example.txt' was not found.")
except Exception as e: 
    print(f"An unexpected error occurred: {e}")
else:
    print(f"Result: {result}")
finally:
    print("Program execution completed.")
