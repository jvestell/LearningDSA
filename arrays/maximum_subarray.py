"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
"""

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        current_sum = 0
        for num in nums:
            current_sum += num
            max_sum = max(max_sum, current_sum)
            if current_sum < 0:
                current_sum = 0
        return max_sum

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

