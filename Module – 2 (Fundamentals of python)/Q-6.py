""" Write python program that swap two number with c variable and without c variable"""

print("With temporary variable")
a = int(input("Enter Number one: "))
b = int(input("Enter Number two: "))
 
c = a
a = b
b = c
print(a)
print(b)

print("Without temporary variable")
a = int(input("Enter Number one: "))
b = int(input("Enter Number two: "))

a = a + b
b = a - b
a = a - b
print(a)
print(b)