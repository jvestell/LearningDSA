"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
            
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        
        # Fill first row
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
            
        # Fill first column    
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        # Fill rest of dp table
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
                
        return dp[m-1][n-1] 

if __name__ == "__main__":
    sol = Solution()
    print(sol.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))

        

