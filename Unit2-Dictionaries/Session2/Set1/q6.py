# Problem 6: Wildlife Reintroduction
# As a conservationist, your research center has been raising multiple endangered species 
# and is now ready to reintroduce them into their native habitats. You are given two 0-indexed 
# strings raised_species and target_species. The string raised_species represents the list of 
# species available to release into the wild at your center, where each character represents a 
# different species. The string target_speciesrepresents a specific sequence of species you want 
# to form and release together.

# You can take some species from raised_species and rearrange them to form new sequences.

# Return the maximum number of copies of target_species that can be formed by taking species 
# from raised_species and rearranging them.

from collections import Counter


def max_species_copies(raised_species, target_species):
    min_copies = float('inf')
    
    raised_count = Counter(raised_species)
    target_count = Counter(target_species)
    
    for species, count in target_count.items():
        if species in target_count:
            min_copies = min(min_copies, raised_count[species] // count)
            
    return min_copies

raised_species1 = "abcba"
target_species1 = "abc"
print(max_species_copies(raised_species1, target_species1))  # Output: 1

raised_species2 = "aaaaabbbbcc"
target_species2 = "abc"
print(max_species_copies(raised_species2, target_species2)) # Output: 2