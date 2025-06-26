"""
Write a Python program to sort a list using both sort() and sorted().
"""
list1=[10,22,30,14,40]
list1.sort()
print(f"List after using sort() : {list1}")
sortedList=sorted(list1,reverse=True)
print(f"List after using sorted() in decending order : {sortedList}")