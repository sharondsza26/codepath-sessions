# Problem 3: Remove Duplicates
# Write a function remove_dupes() that accepts a sorted array items, and removes the duplicates 
# in-place such that each element appears only once. Return the length of the modified array. 
# You may not create another array; your implementation must modify the original input array items.

def remove_dupes(items):
    if not items:  # Edge case: empty list
        return 0

    write_index = 1  # Position to write the next unique element

    for i in range(1, len(items)):
        if items[i] != items[i - 1]:  # Compare with the previous element
            items[write_index] = items[i]  # Overwrite the duplicate
            write_index += 1  # Move to the next position

    # Trim the list to the new length
    del items[write_index:]

    print(write_index)
    return write_index  
            

items = ["extract of malt", "haycorns", "honey", "honey", "thistle", "thistle"]
remove_dupes(items)

items = ["extract of malt", "haycorns", "honey", "thistle"]
remove_dupes(items)