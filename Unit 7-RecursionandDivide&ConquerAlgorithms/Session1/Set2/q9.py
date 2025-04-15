# Problem 9: Weaving Spells II
# Below is an iterative solution to the weaving_spells() function from the previous problem. Compare your recursive solution to the iterative solution below.

# Discuss with your podmates. Which solution do you prefer?

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

def weave_spells(spell_a, spell_b):
    # If either list is empty, return the other
    if not spell_a:
        return spell_b
    if not spell_b:
        return spell_a

    # Start with the first node of spell_a
    head = spell_a
    
    # Loop through both lists until one is exhausted
    while spell_a and spell_b:
        # Store the next pointers
        next_a = spell_a.next
        next_b = spell_b.next
        
        # Weave spell_b after spell_a
        spell_a.next = spell_b
        
        # If there's more in spell_a, weave it after spell_b
        if next_a:
            spell_b.next = next_a
        
        # Move to the next nodes
        spell_a = next_a
        spell_b = next_b

    # Return the head of the new woven list
    return head