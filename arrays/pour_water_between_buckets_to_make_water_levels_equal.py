"""
You are given an array of integers representing the water levels in buckets. 
You need to pour water between buckets to make the water levels equal. 
Determine the minimum number of pours required to achieve this goal.
"""
from typing import List
class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        # Make a copy of heights to modify
        result = heights.copy()
        
        # Process one unit of water at a time
        for _ in range(volume):
            # Start at position k
            pos = k
            lowest = k
            
            # Check left side
            for i in range(k-1, -1, -1):
                if result[i] < result[lowest]:
                    lowest = i
                elif result[i] > result[lowest]:
                    break
            
            # If we didn't find a lower position on the left,
            # check the right side
            if lowest == k:
                for i in range(k+1, len(result)):
                    if result[i] < result[lowest]:
                        lowest = i
                    elif result[i] > result[lowest]:
                        break
            
            # Add water to the lowest position found
            result[lowest] += 1
        
        return result

solution = Solution()
print(solution.pourWater([2,1,1,2,1,2,2], 4, 3))


