"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
"""

import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m + n - 2, m - 1)

    def dpUniquePaths(self, m: int, n: int) -> int:
        # Create DP table
        dp = [[1] * n for _ in range(m)]
        print("Initial DP table:")
        for row in dp:
            print(row)
        
        # Fill DP table
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                print(f"\nAfter updating position ({i},{j}):")
                for row in dp:
                    print(row)
        
        return dp[m-1][n-1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.dpUniquePaths(3, 7))

"""
solved on:
11/19/2024
"""

