# Problem 10: Up and Down
# Write a function up_and_down() that accepts a list of integers lst as a parameter. 
# The function should return the number of odd numbers minus the number of even numbers in the list.

def up_and_down(lst):
    odd = 0
    even = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            even += 1
            
        else:
            odd += 1
            
    print(odd - even)

lst = [1, 2, 3]
up_and_down(lst)

lst = [1, 3, 5]
up_and_down(lst)

lst = [2, 4, 10, 2]
up_and_down(lst)