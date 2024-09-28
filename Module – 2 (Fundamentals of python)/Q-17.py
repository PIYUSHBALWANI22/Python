"""Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string."""

str1 = input("Enter a string first: ")
str2 = input("Enter a string second: ")

swappedStr1 = str2[:2] + str1[2:]
swappedStr2 = str1[:2] + str2[2:]

result = swappedStr1 + " " + swappedStr2

print("The result after swapping first two characters of string : ",result)