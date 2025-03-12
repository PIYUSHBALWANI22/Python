"""
Write a Python program that uses a custom iterator to iterate over a list of integers.
"""

class CustomIterator:
    def __init__(self,numbers):
        self.numbers=numbers
        self.index=0

    def __iter__(self):
        return self 
    
    def __next__(self):
        if self.index<len(self.numbers):
            value=self.numbers[self.index]
            self.index +=1
            return value 
        else : 
            raise StopIteration
        
number_list=[10,20,30,40,50]

custom_iter=CustomIterator(number_list)

print("Iterating over the list : ")
for number in custom_iter:
    print(number)