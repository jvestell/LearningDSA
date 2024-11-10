"""
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Return a deep copy of the list.
"""
from typing import Optional

class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None
            
        # Map to store old node -> new node mapping
        old_to_new = {}
        
        # First pass: create all new nodes
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
            
        # Second pass: connect next and random pointers
        curr = head
        while curr:
            # Connect next pointer
            old_to_new[curr].next = old_to_new.get(curr.next)
            # Connect random pointer
            old_to_new[curr].random = old_to_new.get(curr.random)
            curr = curr.next
            
        return old_to_new[head]

solution = Solution()
print(solution.copyRandomList(Node(1, Node(2), Node(3))))

"""
solved on 11/09/2024
"""

