def is_symmetrical_title(title):
    left = 0
    right = len(title) - 1
    
    while left < right:
        if title[left].isalpha() and title[right].isalpha():
            if title[left].lower() == title[right].lower() :
                left += 1
                right -= 1
                
            else:
                return False
                
        elif not title[left].isalpha():
            left += 1
            
        elif not title[right].isalpha():
            right -= 1
            
        
            
    return True
    

print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 
print(is_symmetrical_title("A B 123 B A"))