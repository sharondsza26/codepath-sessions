# Problem 3: Squash Spaces
# Write a function squash_spaces() that takes in a string s as a parameter and 
# returns a new string with each substring with consecutive spaces reduced to a single space. 
# Assume s can contain leading or trailing spaces, but in the result should be trimmed. 
# Do not use any of the built-in trim methods.

def squash_spaces(s):
    result = []
    space_found = False
    i = 0
    
    while i < len(s):
        if s[i] == ' ':
            if not space_found:
                result.append(' ')
            space_found = True        
        
        else:
            result.append(s[i])
            space_found = False
            
        i += 1
        
    if result:
        if result[-1] == ' ':
            result.pop()
            
        if result[0] == ' ':
            result.pop(0)
        
    print("".join(result))
        
        

s = "   Up,     up,   and  away!   "
squash_spaces(s)

s = "With great power comes great responsibility."
squash_spaces(s)