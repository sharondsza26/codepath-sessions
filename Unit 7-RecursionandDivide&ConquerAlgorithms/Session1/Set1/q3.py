# Problem 3: Counting Unique Suits
# Some of Iron Man's suits are duplicates. Given a list of strings suits where each string 
# is a suit in Stark's collection, count the total number of unique suits in the list.

# Implement the solution iteratively.
# Implement the solution recursively.
# Discuss: what are the similarities between the two solutions? What are the differences?
# Evaluate the time complexity of each solution. Are they the same? Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

def count_suits_iterative(suits):
    suit_set = set(suits)
    return len(suit_set)

def count_suits_recursive(suits, unique_suits=None):
    if unique_suits is None:
        unique_suits = set()
        
    if not suits:
        return len(unique_suits)
    
    unique_suits.add(suits[0])
    return count_suits_recursive(suits[1:],unique_suits)

# Example Usage:

print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))

# Example Output:

# 3
# 2