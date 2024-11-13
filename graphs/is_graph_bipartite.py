"""
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.

"""
from typing import List
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if not graph:
            return True
            
        n = len(graph)
        color_arr = [-1] * n  # -1: uncolored, 0: first color, 1: second color
        
        # Need to check each component of the graph
        for start in range(n):
            if color_arr[start] == -1:  # Only start BFS for uncolored nodes
                # Start BFS from this node
                color_arr[start] = 0
                queue = [start]
                
                while queue:
                    curr = queue.pop(0)
                    
                    # Check all neighbors
                    for neighbor in graph[curr]:
                        if color_arr[neighbor] == -1:
                            # Color it opposite to current node
                            color_arr[neighbor] = 1 - color_arr[curr]
                            queue.append(neighbor)
                        elif color_arr[neighbor] == color_arr[curr]:
                            # Same color neighbors -> not bipartite
                            return False
                            
        return True

def main():
    graph = [[1, 2], [2, 3], [3, 4], [4, 1]]
    sol = Solution()
    print(sol.isBipartite(graph))

if __name__ == "__main__":
    main()  
