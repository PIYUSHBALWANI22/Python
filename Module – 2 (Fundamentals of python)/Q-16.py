"""Write a Python program to count the occurrences of each word in a given sentence """

sentence = "Here is a small world in a world which is in another world"
words = sentence.split()   
wordCount = {}   

for word in words:
    if word in wordCount:
        wordCount[word]+=1   
    else:
        wordCount[word]=1   

for word, count in wordCount.items():
    print(f"'{word}' occurs {count} time(s).")
