# Problem 7: Performances with Maximum Audience II
# If you used a dictionary as part of your solution to max_audience_performances() 
# in the previous problem, try reimplementing the function without using a dictionary. 
# If you implemented max_audience_performances() without using a dictionary, try solving
# the problem with a dictionary.

# Once you've come up with your second solution, compare the two. Is one solution 
# better than the other? Why or why not?

def max_audience_performances(audiences):
    audience_count = {}
    max_audience = 0
    
    for i in range(len(audiences)):
        audience_count[audiences[i]] = audience_count.get(audiences[i], 0) + 1
        max_audience = max(max_audience, audiences[i])
            
    return max_audience * audience_count[max_audience]

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))