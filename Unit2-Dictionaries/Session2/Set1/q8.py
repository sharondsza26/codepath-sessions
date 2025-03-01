# Problem 8: Equivalent Species Pairs
# In an effort to understand species diversity in different habitats, researchers 
# are analyzing species pairs observed in various regions. Each pair is represented 
# by a list [a, b] where a and b represent two species observed together.

# A species pair [a, b] is considered equivalent to another pair [c, d] if and only if 
# either (a == c and b == d) or (a == d and b == c). This means that the order of species 
# in a pair does not matter.

# Your task is to determine the number of equivalent species pairs in the list of observed species pairs.

from collections import defaultdict


def num_equiv_species_pairs(species_pairs):
    pair_counts = defaultdict(int)
    equivalent_pairs = 0
    
    for a, b in species_pairs:
        pair = tuple(sorted([a,b]))
        equivalent_pairs += pair_counts[pair]  # Add the count of this pair seen before
        pair_counts[pair] += 1
        
    # print(equivalent_pairs)
            
    return equivalent_pairs

species_pairs1 = [[1,2],[2,1],[3,4],[5,6]]
species_pairs2 = [[1,2],[1,2],[1,1],[1,2],[2,2]]

print(num_equiv_species_pairs(species_pairs1))
print(num_equiv_species_pairs(species_pairs2))