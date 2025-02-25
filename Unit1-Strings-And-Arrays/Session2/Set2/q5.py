# Problem 5: Move Zeroes
# Write a function move_zeroes that accepts an integer array nums and returns a new list 
# with all 0s moved to the end of list. The relative order of the non-zero elements in the original list 
# should be maintained.

def move_zeroes(lst):
    zero_list = []
    count = 0
    for i in range(len(lst)):
        if lst[i] == 0:
            count += 1
            
        else:
            zero_list.append(lst[i])
            
    for i in range(count):
        zero_list.append(0)
            
    print(zero_list)

lst = [1, 0, 2, 0, 3, 0]
move_zeroes(lst)