# Title:       Python Sprint Q5 
# Description: A program to parse through text
#              and check frequency of each word.
# Author:      Noah Whiffen - SD12 - Group 20
# Date:        June 17, 2024
     
text = input("Enter the text you would like to check: ") # Input text you would like parsed.
words = text.split() # Splits the text in to words.
freqDict = {} # Empty dictionary 
    
# Count the frequency of each word.
for word in words:
    if word in freqDict:
        freqDict[word] += 1
    else:
        freqDict[word] = 1

# Store the results in the dictionary.
print()
print(freqDict)
    
# A dictionary is a data structure which stores data in key value pairs. They are mutable and unordered.