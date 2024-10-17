"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    def is_mirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

    return is_mirror(root.left, root.right)


def test_is_symmetric():
    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
    result = is_symmetric(root)
    print(f"Is the tree symmetric? {result}")
    assert result == True

    # You can add more test cases here
    root2 = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
    result2 = is_symmetric(root2)
    print(f"Is the second tree symmetric? {result2}")
    assert result2 == False

if __name__ == "__main__":
    test_is_symmetric()

