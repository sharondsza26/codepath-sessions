# Problem 4: Palindromic Name
# Queen Ada is superstitious and believes her children will only have good fortune 
# if their name is symmetrical and reads the same forward and backward. Write a recursive 
# function that takes in a string comprised of only lowercase alphabetic characters name and 
# returns True if the name is palindromic and False otherwise.

# Evaluate the time complexity of your solution. Define your variables and provide a rationale 
# for why you believe your solution has the stated time complexity.

def is_palindrome(name):
    if len(name) <= 1:
        return True
    
    if name[0] != name[-1]:
        return False
    
    return is_palindrome(name[1:-1])

# Example Usage:

print(is_palindrome("eve"))
print(is_palindrome("ling"))
print(is_palindrome(""))
# Example Output:

# True
# True
# False