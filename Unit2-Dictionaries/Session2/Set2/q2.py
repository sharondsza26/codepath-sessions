# Problem 2: Unique Travel Souvenirs
# As a seasoned traveler, you've collected a variety of souvenirs from different destinations. 
# You have an array of string souvenirs, where each string represents a type of souvenir. 
# You want to know if the number of occurrences of each type of souvenir in your collection is unique.

# Write a function that takes in an array souvenirs and returns True if the number of occurrences 
# of each value in the array is unique, or False otherwise.
from collections import Counter
def unique_souvenir_counts(souvenirs):
    count = Counter(souvenirs)
    # Get the list of occurrences (values) and check if they're unique by comparing with the set of counts
    return len(count.values()) == len(set(count.values()))

souvenirs1 = ["keychain", "hat", "hat", "keychain", "keychain", "postcard"]
souvenirs2 = ["postcard", "postcard", "postcard", "postcard"]
souvenirs3 = ["keychain", "magnet", "hat", "candy", "postcard", "stuffed bear"]

print(unique_souvenir_counts(souvenirs1))  
print(unique_souvenir_counts(souvenirs2)) 
print(unique_souvenir_counts(souvenirs3))