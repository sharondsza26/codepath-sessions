def max_subarray_sum(arr):
    max_sum = float('-inf')  # Initialize max_sum to the smallest possible number
    current_sum = 0

    for num in arr:
        current_sum += num
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0

    return max_sum

# Input handling
inputArr_size = int(input())  # Read size of the list
arr = list(map(int, input().split()))  # Read space-separated integers

# Output the maximum subarray sum
print(max_subarray_sum(arr))
