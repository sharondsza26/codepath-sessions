# Problem 1: String Array Equivalency
# Given two string arrays word1 and word2, return True if the two arrays represent the same string, 
# and False otherwise.

# A string is represented by an array if the array elements concatenated in order forms the string.

def are_equivalent(word1, word2):
    str1 = "".join(word1)
    str2 = "".join(word2)
    
    if str1.lower() == str2.lower():
        return True
    
    return False

word1 = ["bat", "man"]
word2 = ["b", "atman"]
print(are_equivalent(word1, word2))

word1 = ["alfred", "pennyworth"]
word2 = ["alfredpenny", "word"]
print(are_equivalent(word1, word2))

word1  = ["cat", "wom", "an"]
word2 = ["catwoman"]
print(are_equivalent(word1, word2))