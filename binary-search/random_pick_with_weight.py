"""
You are given a 0-indexed array of positive integers w, where w[i] describes the weight of the ith index.

You need to implement the following three methods:

1. PickIndex() -> returns an index (0-indexed) according to the weights.
2. PickIndex() -> returns an index (0-indexed) according to the weights.
3. PickIndex() -> returns an index (0-indexed) according to the weights.
"""

from random import randint
from typing import List
import random

class Solution:
    def __init__(self, w: List[int]):
        # Create cumulative sum array for weighted probability
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        
    def pickIndex(self) -> int:
        # Generate random number and use binary search to find its position
        target = random.random() * self.prefix_sums[-1]
        left, right = 0, len(self.prefix_sums)
        
        while left < right:
            mid = left + (right - left) // 2
            if target > self.prefix_sums[mid]:
                left = mid + 1
            else:
                right = mid
                
        return left
    

solution = Solution([1, 3])
print(solution.pickIndex())
print(solution.pickIndex2())
print(solution.pickIndex3())
