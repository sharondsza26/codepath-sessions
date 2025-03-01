# Problem 4: Prioritizing Endangered Species Observations
# In your work with a wildlife conservation database, you have two lists: observed_species 
# and priority_species. The elements of priority_species are distinct, and all elements in 
# priority_species are also in observed_species.

# Write a function prioritize_observations() that sorts the elements of observed_species such 
# that the relative ordering of items in observed_species matches that of priority_species. 
# Species that do not appear in priority_species should be placed at the end of observed_species 
# in ascending order.

def prioritize_observations(observed_species, priority_species):
    priority_set = set(priority_species)
    priority_order = []
    observed_order = []
    priority_count = {}
        
    
    for i in observed_species:
        if i in priority_set:   
            priority_count[i] = priority_count.get(i, 0) + 1
            
        else:
            observed_order.append(i)
            
    for i in priority_species:
        count = priority_count[i]
        priority_order.extend([i] * count)
            
    
    priority_order.extend(sorted(observed_order))
    return priority_order
            
    

observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
priority_species1 = ["🐯", "🦌", "🐘", "🦁"]  

observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]

print(prioritize_observations(observed_species1, priority_species1))
print(prioritize_observations(observed_species2, priority_species2)) 
