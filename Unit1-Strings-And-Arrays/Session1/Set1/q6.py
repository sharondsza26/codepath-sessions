# Problem 6: Double Trouble
# Help Winnie the Pooh double his honey! Write a function doubled() that accepts a list of integers
# hunny_jars as a parameter and multiplies each element in the list by two. Return the doubled list.

def doubled(hunny_jars: list):
    # total = 0
    for i in range(len(hunny_jars)):
        hunny_jars[i] = hunny_jars[i] * 2
        
    return hunny_jars

hunny_jars = [1, 2, 3]
print(doubled(hunny_jars))
