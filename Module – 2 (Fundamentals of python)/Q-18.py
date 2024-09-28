"""Write a Python program to add 'ing' at the end of a given str (length 
should be at least 3). If the given string already ends with 'ing' then add 
'ly' instead if the string length of the given string is less than 3, leave it 
unchanged. """

str = input("Enter a string: ")
if  len(str) <3:
    print(str)
else:
    if str[-3:] == 'ing':
     result = str + 'ly'
    else:
        result = str + 'ing'
    print(result)