"""Write a Python function to insert a string in the middle of a string."""

str = "Welcome python "
insertStr = " to "
result = len(str) // 2
ans = str[:result] + insertStr + str[result:]
print(ans)