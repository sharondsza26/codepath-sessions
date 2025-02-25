# Problem 5: Total Honey
# Winnie the Pooh wants to know how much honey he has. Write a function sum_honey() 
# that accepts a list of integers 
# hunny_jars and returns the sum of all elements in the list. Do not use the built-in function sum().

def sum_honey(hunny_jars: list):
    total = 0
    for i in range(len(hunny_jars)):
        total += hunny_jars[i]
        
    return total

hunny_jars = [2, 3, 4, 5]
total = sum_honey(hunny_jars)
print(total)

hunny_jars = []
print(sum_honey(hunny_jars))