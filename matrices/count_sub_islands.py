"""
You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.
"""
from typing import List
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])
        visited = set()

        def dfs(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols or grid2[row][col] == 0 or (row, col) in visited:
                return True
            visited.add((row, col))
            is_subisland = grid1[row][col] == 1
            is_subisland &= dfs(row + 1, col)
            is_subisland &= dfs(row - 1, col)
            is_subisland &= dfs(row, col + 1)
            is_subisland &= dfs(row, col - 1)
            return is_subisland

        count = 0
        for row in range(rows):
            for col in range(cols):
                if grid2[row][col] == 1 and (row, col) not in visited:
                    if dfs(row, col):
                        count += 1
        return count

test_cases = [
    (
        [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]],
        [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
    ),
    (
        [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]],
        [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
    )
]

solution = Solution()
for grid1, grid2 in test_cases:
    print(solution.countSubIslands(grid1, grid2))

"""
Solved on: 10/19/2024
"""
