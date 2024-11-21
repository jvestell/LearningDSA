"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.
"""
from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        current_count = 0
        
        for num in nums:
            if num == 1:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0
        return max_count

if __name__ == "__main__":
    sol = Solution()
    print(sol.findMaxConsecutiveOnes([1,1,0,1,1,1]))
    
