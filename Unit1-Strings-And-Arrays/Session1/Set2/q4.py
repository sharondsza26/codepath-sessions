# Problem 4: Last
# Implement a function get_last() that accepts a list of items items and returns the last item in the list.
# If the list is empty, return None.

def get_last(items):
    if not items:
        print("None")
        
    else:
        print(items[-1])

items = ["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]
get_last(items)

items = []
get_last(items)