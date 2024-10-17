"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def has_path_sum(self, root: Optional[TreeNode], target_sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == target_sum
        return self.has_path_sum(root.left, target_sum - root.val) or self.has_path_sum(root.right, target_sum - root.val)

def tree_to_string(node):
    if not node:
        return "None"
    return f"TreeNode({node.val}, {tree_to_string(node.left)}, {tree_to_string(node.right)})"

def test_has_path_sum():
    solution = Solution()
    
    # Test case 1
    print("\nTest case 1:")
    root1 = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
    target_sum1 = 22
    print(f"Tree: {tree_to_string(root1)}")
    print(f"Target sum: {target_sum1}")
    result1 = solution.has_path_sum(root1, target_sum1)
    print(f"Result: {result1}")
    assert result1 == True, "Should return True for path 5->4->11->2"

    # Test case 2
    print("\nTest case 2:")
    root2 = TreeNode(1, TreeNode(2), TreeNode(3))
    target_sum2 = 5
    print(f"Tree: {tree_to_string(root2)}")
    print(f"Target sum: {target_sum2}")
    result2 = solution.has_path_sum(root2, target_sum2)
    print(f"Result: {result2}")
    assert result2 == False, "Should return False as there's no path with sum 5"

    # Test case 3
    print("\nTest case 3:")
    root3 = None
    target_sum3 = 0
    print(f"Tree: {root3}")
    print(f"Target sum: {target_sum3}")
    result3 = solution.has_path_sum(root3, target_sum3)
    print(f"Result: {result3}")
    assert result3 == False, "Should return False for an empty tree"

    print("\nAll tests passed successfully!")

if __name__ == "__main__":
    test_has_path_sum()
