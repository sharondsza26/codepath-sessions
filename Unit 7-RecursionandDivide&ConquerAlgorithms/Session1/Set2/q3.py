# Problem 3: Reversing a Scroll
# A wizard is deciphering an ancient scroll and needs to reverse the letters in a word to 
# reveal a hidden message. Write a recursive function to reverse the letters in a given 
# scroll and returns the reversed scroll. Assume scroll only contains alphabetic characters.

# Evaluate the time complexity of your solution. Define your variables and provide a 
# rationale for why you believe your solution has the stated time complexity.

def reverse_scroll(scroll):
    if not scroll:
        return ""
    
    return scroll[-1] + reverse_scroll(scroll[:-1])
# Example Usage:

print(reverse_scroll("cigam"))
print(reverse_scroll("lleps"))
# Example Output:

# magic
# spell