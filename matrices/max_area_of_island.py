from typing import List

"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical). You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
"""

class Solution: 
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in visited or grid[row][col] == 0:
                return 0
            visited.add((row, col))
            
            area = 1  # Count the current cell
            # Add the areas of adjacent cells
            area += dfs(row + 1, col)
            area += dfs(row - 1, col)
            area += dfs(row, col + 1)
            area += dfs(row, col - 1)
    
            return area

        max_area = 0
        for row in range(rows):
            for col in range(cols):
                max_area = max(max_area, dfs(row,col))
        return max_area

test_cases = [
    [[0,0,1,0,0,0,0,1,0,0,0,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,1,1,0,1,0,0,0,0,0,0,0,0],
     [0,1,0,0,1,1,0,0,1,0,1,0,0],
     [0,1,0,0,1,1,0,0,1,1,1,0,0],
     [0,0,0,0,0,0,0,0,0,0,1,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,0,0,0,0,0,0,1,1,0,0,0,0]]
]

solution = Solution()
for test_case in test_cases:
    print(solution.maxAreaOfIsland(test_case))

"""
Solved on:
10/18/2024
"""
