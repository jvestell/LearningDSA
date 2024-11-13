"""
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single equation is invalid, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.
"""
from typing import List
from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Create a graph where each variable is a node and each equation is an edge
        graph = defaultdict(list)
        for (x, y), value in zip(equations, values):
            graph[x].append((y, value))
            graph[y].append((x, 1 / value))
        
        # Function to perform DFS and calculate the result of the query
        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            visited.add(start)
            for neighbor, weight in graph[start]:
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)
                    if result != -1.0:
                        return weight * result
            return -1.0
        
        # Evaluate all queries using DFS
        results = []
        for start, end in queries:
            results.append(dfs(start, end, set()))
        return results
        
def main():
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    print(Solution().calcEquation(equations, values, queries))

if __name__ == "__main__":
    main()

"""
solve on:
11/12/2024
"""

        
