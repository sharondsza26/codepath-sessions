# Problem 6: Reverse Vowels of a String
# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in 
# both lower and upper cases and more than once.

def reverse_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowels_order = []
    new_str = ''
    
    for i in range(len(s)):
        if s[i] in vowels:
            vowels_order.append(s[i])
            
    print(vowels_order)
            
    for i in range(len(s)):
        if s[i] in vowels:
            new_str += vowels_order.pop()
            
        else:
            new_str += s[i]

    print(new_str)
    
s = "robin"
reverse_vowels(s)

s = "BATgirl"
reverse_vowels(s)

s = "batman"
reverse_vowels(s)