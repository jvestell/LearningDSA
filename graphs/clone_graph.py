
"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.
"""
from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        # Map to store old node to new node mapping
        old_to_new = {}
        
        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]
            
            copy = Node(node.val)
            old_to_new[node] = copy
            
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
                
            return copy
            
        return dfs(node)

solution = Solution()
print(solution.cloneGraph(Node(1, [Node(2), Node(3)])))
print(solution.cloneGraph(None))


"""
solved on 11/08/2024
"""

