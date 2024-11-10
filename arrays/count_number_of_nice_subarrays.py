"""
Given an array of integers nums and an integer k. A subarray is called nice if there are k odd numbers on it.

Return the number of nice subarrays.
"""
from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Map to store count of prefix odd numbers
        prefix_count = {0: 1}  # Initialize with 0 odds seen
        curr_odds = 0
        result = 0
        
        for num in nums:
            # Increment odd count if current number is odd
            curr_odds += num % 2
            
            # If we've seen (curr_odds - k) before, those are valid subarrays
            if curr_odds - k in prefix_count:
                result += prefix_count[curr_odds - k]
            
            
            # Add current odd count to our prefix map
            prefix_count[curr_odds] = prefix_count.get(curr_odds, 0) + 1
            
        return result

solution = Solution()
print(solution.numberOfSubarrays([1,1,2,1,1], 3))

"""
solved on 11/08/2024
"""
