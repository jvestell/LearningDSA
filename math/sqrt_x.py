"""
Implement int sqrt(int x).
Compute and return the square root of x, where x is non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return right

solution = Solution()
print(solution.mySqrt(49))


"""
solved on 2024-11-07
"""
