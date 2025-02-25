# Problem 6: Squared
# Write a function squared() that accepts a list of integers numbers as a parameter and 
# squares each item in the list. Return the squared list.

def squared(numbers):
    squared_nums = []
    for i in range(len(numbers)):
        squared_nums.append(numbers[i] * numbers[i])
        
    print(squared_nums)
    

numbers = [1, 2, 3]
squared(numbers)