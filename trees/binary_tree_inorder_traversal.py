"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Inorder traversal: left, root, right
"""

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)


def inorder_traversal_iterative(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    stack = []
    result = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.val)
        current = current.right

    return result


def inorder_traversal_morris(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    result = []
    current = root

    while current:
        if not current.left:
            result.append(current.val)
            current = current.right
        else:
            predecessor = current.left
            
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right
            
            if not predecessor.right:
                predecessor.right = current
                current = current.left
            else:
                result.append(current.val)
                predecessor.right = None
                current = current.right

    return result


def test_inorder_traversal():
    root = TreeNode(1, None, TreeNode(2, TreeNode(3, None, None), None))
    assert inorder_traversal(root) == [1, 3, 2]
    assert inorder_traversal_iterative(root) == [1, 3, 2]
    assert inorder_traversal_morris(root) == [1, 3, 2]


if __name__ == "__main__":
    test_inorder_traversal()

