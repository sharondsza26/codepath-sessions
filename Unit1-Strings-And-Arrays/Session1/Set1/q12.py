# Problem 12: Thistle Hunt
# Pooh, Piglet, and Roo are looking for thistles to gift their friend Eeyore. 
# Write a function locate_thistles() that takes in a list of strings items and returns a list of 
# the indices of any elements with value "thistle". The indices in the resulting list 
#   should be ordered from least to greatest.

def locate_thistles(items):
    result = []
    for i in range(len(items)):
        if items[i] == "thistle":
            result.append(i)
            
    print(result)
    

items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
locate_thistles(items)

items = ["book", "bouncy ball", "leaf", "red balloon"]
locate_thistles(items)