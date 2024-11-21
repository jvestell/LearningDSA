"""
You are given an array nums consisting of positive integers.

A subarray is called nice if the bitwise AND of every pair of elements that are in different positions in the subarray is 0.

Return the length of the longest nice subarray.
"""

from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        max_length = 1  # Track maximum length seen so far
        current_or = 0  # Track the OR of all numbers in current window
        left = 0       # Left pointer of sliding window
        
        # Iterate through array with right pointer
        for right in range(len(nums)):
            # While current number has bits that overlap with window
            while current_or & nums[right] != 0:
                # Remove leftmost number from window
                current_or ^= nums[left]
                left += 1
                
            # Add current number to window
            current_or |= nums[right]
            max_length = max(max_length, right - left + 1)
        
        return max_length

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestNiceSubarray([1,3,8,48,10])) # Output: 3

"""
solved on: 11/20/2024
"""
