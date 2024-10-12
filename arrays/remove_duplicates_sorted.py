from typing import List 

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Initialize the pointer for unique elements
        j = 0
        
        # Iterate through the array
        for i in range(1, len(nums)):
            # If current element is different from the previous unique element
            if nums[i] != nums[j]:
                # Move j forward and update the element
                j += 1
                nums[j] = nums[i]
        
        # Return the count of unique elements (j + 1 because j is zero-indexed)
        return j + 1

# Example call to the function
solution = Solution()
nums = [1, 1, 2, 2, 3, 4, 4, 5]
result = solution.removeDuplicates(nums)
print(f"Result: {result}")

