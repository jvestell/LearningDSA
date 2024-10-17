"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if not p or not q: return False
        if p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

def test_isSameTree():

    sol = Solution()
    print("Creating test trees...")
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    
    print("Tree p:", tree_to_string(p))
    print("Tree q:", tree_to_string(q))
    
    print("Checking if trees are the same...")
    result = sol.isSameTree(p, q)
    
    print(f"Result: {result}")
    assert result == True, "Trees should be the same"
    print("Test passed successfully!")

def tree_to_string(node):
    if not node:
        return "None"
    return f"TreeNode({node.val}, {tree_to_string(node.left)}, {tree_to_string(node.right)})"

if __name__ == "__main__":
    test_isSameTree()
