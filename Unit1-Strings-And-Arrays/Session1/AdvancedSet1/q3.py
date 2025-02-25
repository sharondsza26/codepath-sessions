# Problem 3: T-I-Double Guh-Er II
# T-I-Double Guh-Er: That spells Tigger! Write a function tiggerfy() 
# that accepts a string word and returns a new string that removes any substrings 
# t, i, gg, and er from word. The function should be case insensitive.

def tiggerfy(word):
    word = word.lower()
    substrings = ["t", "i", "gg", "er"]
    
    for sub in substrings:
        word = word.replace(sub, "")  
    
    print(word)
    return word
            

word = "Trigger"
tiggerfy(word)

word = "eggplant"
tiggerfy(word)

word = "Choir"
tiggerfy(word)