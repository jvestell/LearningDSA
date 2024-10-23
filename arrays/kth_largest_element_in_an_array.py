"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.
"""

from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]

solution = Solution()
print(solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))

"""
Solved on: 10/22/2024
"""
