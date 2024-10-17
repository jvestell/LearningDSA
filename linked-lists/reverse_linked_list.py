"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

def listToString(node):
    if not node:
        return "None"
    return f"ListNode({node.val}, {listToString(node.next)})"


s = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(listToString(s.reverseList(head)))  # Output: ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1)))))

head = ListNode(1, ListNode(2))
print(listToString(s.reverseList(head)))  # Output: ListNode(2, ListNode(1))
