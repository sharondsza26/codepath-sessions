# Problem 3: Encode
# The Riddler is planning to leave a coded message to lead Batman into a trap. 
# Write a function shuffle() that takes in a string, the Riddler's message, 
# and encodes it using an integer array indices. The message will be shuffled such 
# that the character at the ith position in message moves to index indices[i] in the shuffled string. 
# You may assume len(message) is equal to the len(indices).

def shuffle(message, indices):
    msg = ""
    for i in range(len(indices)):
        msg += message[indices[i]]
    
    print(msg)

message = "evil"
indices = [3, 1, 2, 0]
shuffle(message, indices)

message = "findme"
indices = [0, 1, 2, 3, 4, 5]
shuffle(message, indices)