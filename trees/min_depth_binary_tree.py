"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:     
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


def treeToString(node):
    if not node:
        return "None"
    return f"TreeNode({node.val}, {treeToString(node.left)}, {treeToString(node.right)})"


def testMinDepth():
    solution = Solution()

    # Test case 1
    print("\nTest case 1:")
    root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(f"Tree: {treeToString(root1)}")
    result1 = solution.minDepth(root1)
    print(f"Minimum depth: {result1}")
    assert result1 == 2, "Should return 2 for the given tree"

    # Test case 2
    print("\nTest case 2:")
    root2 = TreeNode(1, TreeNode(2))
    print(f"Tree: {treeToString(root2)}")
    result2 = solution.minDepth(root2)
    print(f"Minimum depth: {result2}")
    assert result2 == 2, "Should return 2 for a tree with only left child"

    # Test case 3
    print("\nTest case 3:")
    root3 = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
    print(f"Tree: {treeToString(root3)}")
    result3 = solution.minDepth(root3)
    print(f"Minimum depth: {result3}")
    assert result3 == 4, "Should return 4 for a tree with only right children"

    # Test case 4
    print("\nTest case 4:")
    root4 = None
    print(f"Tree: {root4}")
    result4 = solution.minDepth(root4)
    print(f"Minimum depth: {result4}")
    assert result4 == 0, "Should return 0 for an empty tree"

    print("\nAll tests passed successfully!")


if __name__ == "__main__":
    testMinDepth()
