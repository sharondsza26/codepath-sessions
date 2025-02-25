# Problem 8: Find the Villain
# Write a function find_villain() that accepts a list crowd and a value villain as 
# parameters and returns a list of all indices where the villain is found hiding in the crowd.

def find_villain(crowd, villain):
    v = []
    for i in range(len(crowd)):
        if crowd[i] == villain:
            v.append(i)
            
    print(v)
    

crowd = ['Batman', 'The Joker', 'Alfred Pennyworth', 'Robin', 'The Joker', 'Catwoman', 'The Joker']
villain = 'The Joker'
find_villain(crowd, villain)