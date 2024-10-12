from typing import List 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
    
# Example call to the function
solution = Solution()
nums = [22, 7, 11, 15]
target = 33
result = solution.twoSum(nums, target)

# Print final result
print(f"Result: {result}")
