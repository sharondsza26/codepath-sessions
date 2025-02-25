# Problem 11: T-I-Double Guh-ER
# Signs in the Hundred Acre Wood have been losing letters as Tigger bounces around 
# stealing any letters he needs to spell out his name. Write a function tiggerfy() 
# that accepts a string s, and returns a new string with the letters t, i, g, e, and r from it.

def tiggerfy(s):
    tigger = ['t', 'i', 'g', 'e', 'r']
    new_str = ""
 
    for i in range(len(s)):
        if s[i].lower() in tigger:
            new_str += ""
            
        else:
            new_str += s[i]
            
    print(new_str)

s = "suspicerous"
tiggerfy(s)

s = "Trigger"
tiggerfy(s)

s = "Hunny"
tiggerfy(s)