# Problem 8: Exclusive Elements
# Given two lists lst1 and lst2, write a function exclusive_elemts() 
# that returns a new list that contains the elements which are in lst1 but not in lst2 and the elements 
# that are in lst2 but not in lst1.

def exclusive_elemts(lst1, lst2):
    exclusive_element = []
    for i in lst1:
        if i in lst2:
            continue
        else:
            exclusive_element.append(i)
            
    for i in lst2:
        if i in lst1:
            continue
        else:
            exclusive_element.append(i)


lst1 = ["pooh", "roo", "piglet"]
lst2 = ["piglet", "eeyore", "owl"]
print(exclusive_elemts(lst1, lst2))

lst1 = ["pooh", "roo"]
lst2 = ["piglet", "eeyore", "owl", "kanga"]
print(exclusive_elemts(lst1, lst2))

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["pooh", "roo", "piglet"]
print(exclusive_elemts(lst1, lst2))