# Problem 2: HulkSmash
# Write a function hulk_smash() that accepts an integer n and returns a 1-indexed 
# string array answer where:

# answer[i] == "HulkSmash" if i is divisible by 3 and 5.
# answer[i] == "Hulk" if i is divisible by 3.
# answer[i] == "Smash" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.

def hulk_smash(n):
    smash = []
    
    for i in range(1, n+1):
        if i%3 == 0:
            smash.append("Hulk")
            
        elif i%5 == 0:
            smash.append("Smash")
            
        elif i%3 == 0 and i%5 ==0 :
            smash.append("HulkSmash")
            
        else:
            smash.append(str(i))
            
    print(smash)

n = 3
hulk_smash(n)

n = 5
hulk_smash(n)

n = 15
hulk_smash(n)