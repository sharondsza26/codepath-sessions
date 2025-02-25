# Problem 9: Merge Strings Alternately
# Write a function merge_alternately() that accepts two strings word1 and word2. 
# Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

def merge_alternately(word1, word2):
    len_str = min(len(word1), len(word2))
    print(len_str)
    new_str = ''
    
    for i in range(len_str):
        new_str += word1[i] + word2[i]
            
    
    new_str += word1[len_str:] + word2[len_str:]
        
    print(new_str)

word1 = "wol"
word2 = "oze"
merge_alternately(word1, word2)

word1 = "hfa"
word2 = "eflump"
merge_alternately(word1, word2)

word1 = "eyre"
word2 = "eo"
merge_alternately(word1, word2)