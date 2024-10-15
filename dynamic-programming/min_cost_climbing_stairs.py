from typing import List

"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.

Example 1:
Input: cost = [10,15,20]
Output: 15
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        # Base cases
        if n == 0:
            return 0
        elif n == 1:
            return cost[0]
        
        # Initialize the dp array
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        # Fill the dp array using the recurrence relation
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        # The minimum cost will be to step beyond the last or second-to-last step
        return min(dp[n-1], dp[n-2])
        
s = Solution()
print(s.minCostClimbingStairs([10,15,20]))
print(s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))

