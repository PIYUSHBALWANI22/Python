"""Write a Python program to sum of three given integers. However, if two values are equal sum will be zero."""

num1 = int(input("Enter the number one : "))
num2 = int(input("Enter the number two : "))
num3 = int(input("Enter the number three : "))
if num1 == num2 or num2 == num3 or num1 == num3:
   print(int(0))
else:
   sum = num1 + num2 + num3
   print(f"sum of all three numbers is {sum}")