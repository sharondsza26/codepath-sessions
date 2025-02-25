# Problem 4: Count Digits
# Given a non-negative integer n, write a function count_digits() 
# that returns the number of digits in n. You may not cast n to a string.

def count_digits(n):
    if n == 0:
        return 1
    
    digits = 0
    while n > 0:
        digits += 1
        n //= 10
        
    return digits

n = 964
print(count_digits(n))

n = 0
print(count_digits(n))