"""
Problem: Path Sum in Binary Tree

Given a binary tree and a target sum, determine if there exists a root-to-leaf path 
where the sum of all node values along the path equals the target sum.

Example:
Given the following binary tree and target sum = 23:

       10
      /  \
     5    15
    / \     \
   3   7     18

Return True because there exists a path 10 -> 5 -> 8 that sums to 23.

This is a perfect use case for DFS because:
1. We need to explore complete paths from root to leaf
2. We want to track running sums along each path
3. We can backtrack when a path doesn't work
"""
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

print(Solution().hasPathSum(TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18))), 18))


