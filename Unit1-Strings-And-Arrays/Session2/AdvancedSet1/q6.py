# Problem 6: Merge Intervals
# Write a function merge_intervals() that accepts an array of intervals 
# where intervals[i] = [starti, endi], merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

def merge_intervals(intervals):
    intervals.sort()
    merged = [intervals[0]]
    for i in range(1, len(intervals)):
        prev_merged_start, prev_merged_end = merged[-1]
        curr_start, curr_end = intervals[i]
        
        if prev_merged_end >= curr_start:
            merged[-1] = [prev_merged_start, max(prev_merged_end, curr_end)]
            
        else:
            merged.append(intervals[i])
            
    print(merged)
            


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
merge_intervals(intervals)

intervals = [[1, 4], [4, 5]]
merge_intervals(intervals)