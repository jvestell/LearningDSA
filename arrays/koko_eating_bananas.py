"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour (batch eating) eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
If the pile has less than k bananas, she eats all of them instead, and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish all the bananas before the guards come back.
return the minimum integer k such that she can eat all the bananas within h hours.
"""

from typing import List
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary search between 1 and max(piles)
        left = 1
        right = max(piles)
        
        def can_eat_all(speed):
            # Calculate total hours needed at this speed
            hours = 0
            for pile in piles:
                # Use ceiling division to round up
                # hours += (pile + speed - 1) // speed
                # time needed to eat the pile
                hours += math.ceil(pile / speed)
            return hours <= h
        
        # Binary search for minimum valid speed
        while left < right:
            mid = (left + right) // 2
            if can_eat_all(mid):
                # If we can eat all bananas at this speed,
                # try a lower speed
                right = mid
            else:
                # If we can't eat all bananas at this speed,
                # we need a higher speed
                left = mid + 1
                
        return left

solution = Solution()
print(solution.minEatingSpeed([3,6,7,11], 8))
print(solution.minEatingSpeed([30,11,23,4,20], 5))
print(solution.minEatingSpeed([30,11,23,4,20], 6))

"""
solved on: 
2024-11-07
2024-11-08

"""

