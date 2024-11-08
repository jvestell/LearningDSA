"""
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
"""

from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Initialize hash map with 0:1 to handle subarrays starting from index 0
        prefix_sums = {0: 1}
        curr_sum = 0
        count = 0
        
        for num in nums:
            # Add current number to running sum
            curr_sum += num
            
            # If (curr_sum - k) exists in map, we found subarray(s) summing to k
            if curr_sum - k in prefix_sums:
                count += prefix_sums[curr_sum - k]
            
            # Add current sum to prefix_sums map
            prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
            
        return count

solution = Solution()
print(solution.subarraySum([1,1,1], 2))
print(solution.subarraySum([1,2,3], 3))
print(solution.subarraySum([1,-1,1], 0))
print(solution.subarraySum([-1,-1,1], 0))
print(solution.subarraySum([1,2,3,4,5], 5))

"""
solved on 11/07/2024
"""
