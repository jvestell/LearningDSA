"""
Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two that sums up to a multiple of k, or false otherwise.

A subarray is a contiguous part of an array.
"""

from typing import List
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sums = {0: -1}
        curr_sum = 0
        
        for i, num in enumerate(nums):
            curr_sum += num
            if curr_sum % k in prefix_sums:
                return True
            prefix_sums[curr_sum % k] = i
        return False

solution = Solution()
print(solution.checkSubarraySum([23,2,4,6,7], 6))
print(solution.checkSubarraySum([23,2,6,4,7], 6))
print(solution.checkSubarraySum([23,2,6,4,7], 13))

"""
solved on 11/08/2024
"""
