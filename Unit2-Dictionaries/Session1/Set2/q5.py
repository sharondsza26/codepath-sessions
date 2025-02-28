# Problem 5: Name the Node
# NASA has asked the public to vote on a new name for one of the nodes in the 
# International Space Station. Given a list of strings votes where each string in the 
# list is a voter's suggested new name, implement a function get_winner() that returns 
# the suggestion with the most number of votes.

# If there is a tie, return either option.

from collections import Counter


def get_winner(votes):
    count = Counter(votes)
    
    return max(count, key=count.get)

votes1 = ["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert", "Colbert"]
votes2 = ["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert"]

print(get_winner(votes1))
print(get_winner(votes2))