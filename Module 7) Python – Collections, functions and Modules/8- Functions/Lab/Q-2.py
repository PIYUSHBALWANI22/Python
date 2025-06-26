"""
Write a Python program to create a calculator using functions. 
"""
def add(x,y):
    return x+y

def substract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y==0:
        return "Error ! Division by zero."
    return x/y

print("""
      
      1. Add
      2. Substraction
      3. Multiplication
      4. Divide
""")

user=input("Enter your choice : ")
num1=float(input("Enter first number : "))
num2=float(input("Enter second number : "))


if user == "1":
    print(f"Result : {add(num1,num2)}" )

elif user == "2":
    print(f"Result : {substract(num1,num2)}")

elif user == "3":
    print(f"Result : {multiply(num1,num2)}")

elif user == "4" :
    print(f"Result : {divide(num1,num2)}")

else :
    print("Invalid input !!..please enter from given.")