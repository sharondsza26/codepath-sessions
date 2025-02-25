# Problem 4: Good Samaritan
# Superman is doing yet another good deed, using his power of flight to distribute meals 
# for the Metropolis Food Bank. He wants to distribute meals in the least number of trips possible.

# Metropolis Food Bank currently stores meals in n packs where the ith pack contains meals[i] meals.
# There are also m empty boxes which can contain up to capacity[i] meals.

# Given an array meals of length n and capacity of size m, write a function minimum_boxes() 
# that returns the minimum number of boxes needed to redistribute the n packs of meals into boxes.

# Note that meals from the same pack can be distributed into different boxes.

def minimum_boxes(meals, capacity):
    total_meals = sum(meals)
    total_capacity = sum(capacity)
    
    if total_meals == total_capacity:
        print(len(capacity))
        return len(capacity)
    
    elif (total_meals > total_capacity) or (not meals):
        print("0")
        return 0
    
    elif max(capacity) >= total_meals:
        print("1")
        return 1
    
    else:
        capacity.sort(reverse=True)
        i = 0
        while total_meals > 0:
            total_meals -= capacity[i]
            i += 1
        
        print(i)

meals = [1, 3, 2]
capacity = [4, 3, 1, 5, 2]
minimum_boxes(meals, capacity)

meals = [5, 5, 5]
capacity = [2, 4, 2, 7]
minimum_boxes(meals, capacity)
