"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array to handle duplicates and for efficient two-pointer technique
        nums.sort()
        result = []
        
        # Iterate through the array, fixing one number at a time
        for i in range(len(nums)):
            # Skip duplicates for the first number to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Use two pointers technique for the remaining two numbers
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                
                if three_sum > 0:
                    # Sum is too large, decrement right pointer
                    right -= 1
                elif three_sum < 0:
                    # Sum is too small, increment left pointer
                    left += 1
                else:
                    # Found a valid triplet
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    # Skip duplicates for the second number to avoid duplicate triplets
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        
        return result


solution = Solution()
print(solution.threeSum([-1, 0, 1, 2, -1, -4]))

"""
Solved on: 10/22/2024
"""
