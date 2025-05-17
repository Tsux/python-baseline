# Definition for singly-linked list.
from typing import Optional

# Linked List for python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(result):
    iterator = result
    print('[', end='')
    while iterator:
        print(iter.val, end=',' if iterator.next is not None else '')
        iterator = iterator.next
    print(']')

# Sample data
l1 = create_linked_list([2, 4, 3])  # Represents number 342
l2 = create_linked_list([5, 6, 4])
def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()  # Placeholder node
    cur = dummy
    carry = 0

    while l1 or l2 or carry:
        sum = carry
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next

        carry = sum // 10
        cur.next = ListNode(sum % 10)
        cur = cur.next

    return dummy.next

result = add_two_numbers(create_linked_list([2,4,3]), create_linked_list([5,6,4]))
iter = result