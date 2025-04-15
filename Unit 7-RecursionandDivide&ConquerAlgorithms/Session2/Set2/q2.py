# Problem 2: Finding Tour Dates
# Your favorite artist is doing a short residency in your city and you're hoping to 
# attend one of their concerts! But because of school, you're only free one day this month 😭. 
# Given a sorted list of integers tour_dates representing the days this month your favorite 
# artist is playing, and an integer available representing the day you are available, write a 
# recursive function can_attend() that returns True if you will be able to attend one of their 
# concerts (some date in tour_dates matches available) and False otherwise.

# Your solution must have O(log n) time complexity.

def can_attend(tour_dates, available):
    def binary_search(left, right):
        if left > right:
            return False
        mid = (left + right) // 2
        if tour_dates[mid] == available:
            return True
        elif tour_dates[mid] > available:
            return binary_search(left, mid - 1)
        else:
            return binary_search(mid + 1, right)
    
    return binary_search(0, len(tour_dates) - 1)
# Example Usage:

print(can_attend([1, 3, 7, 10, 12], 12))
print(can_attend([1, 3, 7, 10, 12], 5))
# Example Output:

# True
# False