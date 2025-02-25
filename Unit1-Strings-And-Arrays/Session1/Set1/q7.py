# Problem 7: Poohsticks
# Winnie the Pooh and his friends are playing a game called Poohsticks where they drop sticks in 
# a stream and race them. They time how long it takes each player's stick to float under Poohsticks 
# Bridge to score each round.

# Write a function count_less_than() to help Pooh and his friends determine how many players 
# should move on to the next round of Poohsticks. count_less_than() should accept a list of integers 
# race_times and an integer threshold and return the number of race times less than threshold.

def count_less_than(race_times, threshold):
    count = 0
    if not race_times:
        return 0
    
    for i in range(len(race_times)):
        if threshold == race_times[i] :
            return count
            
        else:
            count += 1

race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
print(count_less_than(race_times, threshold))

race_times = []
threshold = 4
print(count_less_than(race_times, threshold))