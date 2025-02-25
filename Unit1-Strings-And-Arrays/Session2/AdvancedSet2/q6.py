# Problem 6: Insert Interval
# Implement a function insert_interval() that accepts an array of non-overlapping intervals intervals 
# where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is 
# sorted in ascending order by starti. The function also accepts an interval new_interval = [start, end] that 
# represents the start and end of another interval.

# Insert new_interval into intervals such that intervals is still sorted in ascending order by starti and intervals 
# still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

# You don't need to modify intervals in-place. You can make a new array and return it.

def insert_interval(intervals, new_interval):
    merged = []
    intervals.append(new_interval)
    intervals.sort()
    merged.append(intervals[0])
    
    for i in range(1, len(intervals)):
        prev_start, prev_end = merged[-1]
        curr_start, curr_end = intervals[i]
        
        if prev_end >= curr_start: #overlap
            print(i)
            merged[-1] = [prev_start, max(prev_end, curr_end)]
            print(intervals, "//")
            
        else:
            merged.append(intervals[i])
            
            
    print(merged)
            
    


intervals = [[1, 3], [6, 9]]
new_interval = [2, 5]
insert_interval(intervals, new_interval)

intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
new_interval = [4, 8]
insert_interval(intervals, new_interval)