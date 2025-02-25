# Problem 5: Container with Most Honey
# Christopher Robin is helping Pooh construct the biggest hunny jar possible. 
# Help his write a function that accepts an integer array height of length n. 
# There are n vertical lines drawn such that the two endpoints of the 
# ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that t
# he container contains the most honey.

# Return the maximum amount of honey a container can store.

# Notice that you may not slant the container.

def most_honey(height):
    max_honey = 0
    left = 0
    right = len(height) -1
    
    while left < right :
        
        honey_height = min(height[left], height[right]) * (right - left)
        max_honey = max(honey_height, max_honey)
        
        if height[left] < height[right]:
            left += 1
            
        else:
            right -= 1
            
    print(max_honey)
        

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
most_honey(height)

height = [1, 1]
most_honey(height)