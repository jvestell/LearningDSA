"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

def listToString(node):
    if not node:
        return "None"
    return f"ListNode({node.val}, {listToString(node.next)})"

def printLinkedList(node):
    values = []
    while node:
        values.append(str(node.val))
        node = node.next
    return " -> ".join(values)

def test_middle_node():
    s = Solution()
    test_cases = [
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))),
        ListNode(1),
        ListNode(1, ListNode(2)),
        None
    ]
    
    for i, head in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print(f"Input:  {printLinkedList(head)}")
        middle = s.middleNode(head)
        print(f"Middle: {printLinkedList(middle)}")
        print(f"Full result: {listToString(middle)}")

if __name__ == "__main__":
    test_middle_node()
