# Problem 1: Calculating Village Size
# In the kingdom of Codepathia, the queen determines how many resources to distribute to a 
# village based on its class. A village's class is equal to the number of digits in its population. 
# Given an integer population, write a function get_village_class() that returns the number of 
# digits in population.

# Implement the solution iteratively.
# Implement the solution recursively.
# Discuss: what are the similarities between the two solutions? What are the differences?
def get_village_class_iterative(population):
    digit = 0
    # print(population // 10)
    while population > 0:
        population = population // 10
        digit += 1
        
    return digit

def get_village_class_recursive(population):
    if population == 0:
        return 0
    
    population = population // 10
    
    return 1 + get_village_class_recursive(population)

# Example Usage:

print(get_village_class_iterative(432))
print(get_village_class_recursive(432))
print(get_village_class_iterative(9))
print(get_village_class_recursive(9))

# Example Output:

# 3
# 3
# 1
# 1