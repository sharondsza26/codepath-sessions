# Problem 8: Weaving Spells
# A magician can double a spell's power if they merge two incantations together. Given the heads of two linked lists spell_a and spell_b where each node in the lists contains a spell segment, write a recursive function weave_spells() that weaves spells in the pattern:

# a1 -> b1 -> a2 -> b2 -> a3 -> b3 -> ...

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
    if not spell_a:
        return spell_b
    if not spell_b:
        return spell_a
    
    a_next = spell_a.next
    b_next = spell_b.next

    # Weave current pair
    spell_a.next = spell_b
    spell_b.next = weave_spells(a_next, b_next)

    return spell_a
# Example Usage:

spell_a = Node('A', Node('C', Node('E')))
spell_b = Node('B', Node('D', Node('F')))

print_linked_list(weave_spells(spell_a, spell_b))
# Example Output:

# A -> B -> C -> D -> E -> F