# Understand 

# return the middle node
#  if even -> return second node
#  if empty -> return -1

# Plan
# 2 pass single pointer method
# head = [1, 2, 3, 4, 5]
# keep track of count 
# mid = count // 2
# if not head -> return -1
# for loppp, end at mid
    # head = head.next
# return head

# Implement 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    
def find_middle_node(head):
    # Initialize pointers
    count = 0
    current = head 
    
    # If empty
    if not head:
        return -1
    
    # Pass 1 : find len of list
    while current:
        count +=1
        current = current.next
        
    print(count, "count--")
    mid = count // 2
    print(mid, "mid --")
    
    
    # Pass 2 : find and return mid
    for i in range(mid):
        head = head.next
        
    return head.val

# head = [1, 2, 3, 4, 5]
head = (ListNode(1, ListNode(2, None)))
print(find_middle_node(head))