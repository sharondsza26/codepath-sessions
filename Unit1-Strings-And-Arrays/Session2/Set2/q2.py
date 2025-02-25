# Problem 2: Count Even Strings
# Implement a function count_evens() that accepts a list of strings lst as a parameter. 
# The function should return the number of strings with an even length in the list.

def count_evens(lst):
    num = 0
    for i in lst:
        if len(i) % 2 == 0:
            num += 1
            
    return num

lst = ["na", "nana", "nanana", "batman", "!"]
print(count_evens(lst))

lst = ["the", "joker", "robin"]
print(count_evens(lst))

lst = ["you", "either", "die", "a", "hero", "or", "you", "live", "long", "enough", "to", "see", "yourself", "become", "the", "villain"]
print(count_evens(lst))