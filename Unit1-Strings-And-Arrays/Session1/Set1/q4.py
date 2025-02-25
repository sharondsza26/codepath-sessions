# Problem 4: Return Item
# Implement a function get_item() that accepts a 0-indexed list items and a non-negative 
# integer x and returns the element at index x in items. If x is not a valid index of items, return None.

def get_item(items, x):
    n = len(items) - 1 
    
    if x > n:
        return None
    
    elif items[x]:
        return items[x]
    

items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
result = get_item(items, x)
print(result)

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
result = get_item(items, x)
print(result)