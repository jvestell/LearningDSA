"""
You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. 
Implement a function to find the first bad version. You should minimize the number of calls to the API.
"""

from typing import List
class Solution:
    def firstBadVersion(self, n: int) -> int:
        def isBadVersion(version: int) -> bool:
            # This is a mock implementation since the actual API is not available
            # In real usage, this would be provided by the system
            pass
            
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

solution = Solution()
print(solution.firstBadVersion(5))


"""
This is a classic binary search problem. 
We use two pointers, left and right, to narrow down the search range. 
The loop continues until left and right meet, indicating the first bad version.
"""

"""
solved on 2024-11-07
"""

