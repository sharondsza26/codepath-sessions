# Problem 4: Sum of Digits
# Write a function sum_of_digits() that accepts an integer num and returns the sum of num's digits.
# This problem may benefit from either floor division, which is where the result of dividing two numbers 
# is rounded down. 
# Use a search engine or a generative AI tool to research how to perform floor division in Python.

def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
        
    return total
        

num = 423
print(sum_of_digits(num))

num = 4
print(sum_of_digits(num))