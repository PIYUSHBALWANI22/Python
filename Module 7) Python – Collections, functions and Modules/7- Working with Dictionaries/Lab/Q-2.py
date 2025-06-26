"""
Write a Python program to merge two lists into one dictionary using a loop. 
"""
keys=["name","age","city"]
values=["Piyush", 20, "Ahmedabad"]

my_dict={}
for i in range(len(keys)):
    my_dict[keys[i]]=values[i]

print(f"Merged Dictionary : {my_dict}")