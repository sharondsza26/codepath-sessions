# Problem 9: Common Cause
# Write a function common_elements() that takes in two lists lst1 and lst2 and 
# returns a list of the elements that are common to both lists.

def common_elements(lst1, lst2):
    common_lst = []
    for i in lst1:
        if i in lst2:
            common_lst.append(i)

    print(common_lst)

# Example 1:
# Input: lst1 = ["super strength", "super speed", "x-ray vision"], lst2 = ["super speed", "time travel", "dimensional travel"]
# Output: ["super speed"]

# Example 2:
# Input: lst1 = ["super strength", "super speed", "x-ray vision"], lst2 = ["martial arts", "stealth", "master detective"]
# Output: []


lst1 = ["super strength", "super speed", "x-ray vision"]
lst2 = ["super speed", "time travel", "dimensional travel"]
common_elements(lst1, lst2)

lst1 = ["super strength", "super speed", "x-ray vision"]
lst2 = ["martial arts", "stealth", "master detective"]
common_elements(lst1, lst2)