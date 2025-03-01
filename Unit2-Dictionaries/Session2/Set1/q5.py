# Problem 5: Calculating Conservation Statistics
# You are given a 0-indexed integer array species_populations of even length, 
# where each element represents the population of a particular species in a wildlife reserve.

# As long as species_populations is not empty, you must repetitively:

# Find the species with the minimum population and remove it.
# Find the species with the maximum population and remove it.
# Calculate the average population of the two removed species.
# The average of two numbers a and b is (a+b)/2.

# For example, the average of 200 and 300 is (200+300)/2=250.

# Return the number of distinct averages calculated using the above process.

# Note that when there is a tie for a minimum or maximum population, any can be removed.

def distinct_averages(species_populations):
    avg_set = set()
    
    while species_populations:
        min_population = min(species_populations)
        max_population = max(species_populations)
        
        average = (min_population + max_population) / 2
        avg_set.add(average)
        
        species_populations.remove(min_population)
        species_populations.remove(max_population)
        
    return len(avg_set)

species_populations1 = [4,1,4,0,3,5]
species_populations2 = [1,100]

print(distinct_averages(species_populations1))
print(distinct_averages(species_populations2)) 