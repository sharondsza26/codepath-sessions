# Problem 5: Finding the Shallowest Point
# As the captain of the cruise ship, you need to take a detour to steer clear of an incoming storm. Given an array of integers depths representing the varying water depths along your potential new route, write a function find_shallowest_point() to help you decide whether the new route is deep enough for your ship. The function should use a divide-and-conquer approach to return the shallowest point (minimum value) in depths. You may not use the built-in min() function.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def find_shallowest_point(arr):
    if len(arr) == 1:
        return arr[0]

    mid = len(arr) // 2
    left_min = find_shallowest_point(arr[:mid])
    right_min = find_shallowest_point(arr[mid:])

    return left_min if left_min < right_min else right_min
# Example Usage:

print(find_shallowest_point([5, 7, 2, 8, 3]))
print(find_shallowest_point([12, 15, 10, 21]))
# Example Output:

# 2
# 10