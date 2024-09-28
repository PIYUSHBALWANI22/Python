"""Write a Python program to count the number of characters (character frequency) in a string """

string = input("Enter a string: ")
countChar = {}

for i in string:
    if i in countChar:
        countChar[i] += 1
    else:
        countChar[i] = 1
    
print(countChar)