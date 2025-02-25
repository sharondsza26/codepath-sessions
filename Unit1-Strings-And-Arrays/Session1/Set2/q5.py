# Problem 5: Concatenate
# Write a function concatenate() that takes in a list of strings words and 
# returns a string concatenated that concatenates all elements in words.

def concatenate(words):
    concatenated = ""
    for i in range(len(words)):
        concatenated += words[i]
        
    print(concatenated)
    
words = ["vengeance", "darkness", "batman"]
concatenate(words)

words = []
concatenate(words)