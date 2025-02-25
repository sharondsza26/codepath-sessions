# Problem 5: Best Set
# As part of the festival, attendees cast votes for their favorite set. 
# Given a dictionary votes that maps attendees id numbers to the artist they voted for, 
# return the artist that had the most number of votes. If there is a tie, 
# return any artist with the top number of votes.

def best_set(votes):
    freq_map = {}
        
    for i in votes.values():
        freq_map[i] = freq_map.get(i, 0) + 1
        
    return max(freq_map, key=freq_map.get)
        
    

votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))