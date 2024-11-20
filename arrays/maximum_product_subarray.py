"""
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated such that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.
"""
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        current_product = 1
        for num in nums:
            current_product *= num
            max_product = max(max_product, current_product)
            if current_product == 0:
                current_product = 1
        return max_product

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProduct([2,3,-2,4]))

