# Problem 3: Delete Minimum
# Pooh is eating all of his hunny jars in order of smallest to largest. Given a list of integers 
# hunny_jar_sizes, write a function delete_minimum_elements() that continuously removes the minimum element 
# until the list is empty. 
# Return a new list of the elements of hunny_jar_sizes in the order in which they were removed.

def delete_minimum_elements(hunny_jar_sizes):
    if not hunny_jar_sizes:
        return []
     
    min_elements = []
    while hunny_jar_sizes:
        min_hunny = min(hunny_jar_sizes)
        min_elements.append(min_hunny)
        hunny_jar_sizes.remove(min_hunny)
        
    return min_elements


hunny_jar_sizes = [5, 3, 2, 2, 2, 2, 4, 1]
print(delete_minimum_elements(hunny_jar_sizes))

hunny_jar_sizes = [5, 3, 2, 4, 1]
delete_minimum_elements(hunny_jar_sizes)

hunny_jar_sizes = [5, 2, 1, 8, 2]
delete_minimum_elements(hunny_jar_sizes)