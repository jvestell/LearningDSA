"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n  # Initialize answer array with 1s
        
        # Calculate left products
        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]
        
        right_product = 1  # Initialize right product
        
        # Calculate right products and update answer
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product  # Multiply current answer by right product
            right_product *= nums[i]  # Update right product for next iteration
        
        return answer

solution = Solution()
print(solution.productExceptSelf([1,2,3,4]))
print(solution.productExceptSelf([-1,1,0,-3,3]))


"""
Solved on: 10/19/2024
"""
