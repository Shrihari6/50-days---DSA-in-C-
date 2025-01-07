

''' Day 2: Linked Lists
**Question**: Reverse a singly linked list.
**Answer**:
'''
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev
'''
# Example usage:
# (1 -> 2 -> 3 -> 4 -> 5) becomes (5 -> 4 -> 3 -> 2 -> 1)
```

'''