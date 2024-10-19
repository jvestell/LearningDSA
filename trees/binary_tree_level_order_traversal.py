"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def level_order_traversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)

        return result

    def level_order_traversal_dfs(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        stack = [(root, 0)]

        while stack:
            node, level = stack.pop()
            if len(result) == level:
                result.append([])
            result[level].append(node.val)
            if node.right:
                stack.append((node.right, level + 1))
            if node.left:
                stack.append((node.left, level + 1))

        return result

    def level_order_traversal_bfs(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)

        return result


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Empty tree
    print("Test case 1: Empty tree")
    print(solution.level_order_traversal(None))
    print(solution.level_order_traversal_dfs(None))
    print(solution.level_order_traversal_bfs(None))
    print()

    # Test case 2: Single node tree
    print("Test case 2: Single node tree")
    root = TreeNode(1)
    print(solution.level_order_traversal(root))
    print(solution.level_order_traversal_dfs(root))
    print(solution.level_order_traversal_bfs(root))
    print()

    # Test case 3: Binary tree with multiple levels
    print("Test case 3: Binary tree with multiple levels")
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(solution.level_order_traversal(root))
    print(solution.level_order_traversal_dfs(root))
    print(solution.level_order_traversal_bfs(root))
    print()

    # Test case 4: Unbalanced binary tree
    print("Test case 4: Unbalanced binary tree")
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    print(solution.level_order_traversal(root))
    print(solution.level_order_traversal_dfs(root))
    print(solution.level_order_traversal_bfs(root))


