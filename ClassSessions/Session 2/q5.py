class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def delete_tail(head):
    current = head
    while current.next and current.next.next:
        current = current.next
        
    current.next = None
    return head

butterfly = Node("Common Butterfly")
ladybug = Node("Ladybug")
beetle = Node("Scarab Beetle")
butterfly.next = ladybug
ladybug.next = beetle

print_linked_list(butterfly)

# Input List: butterfly -> ladybug -> beetle
print_linked_list(delete_tail(butterfly))