from typing import List

"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

# Example usage:
s = ["h", "e", "l", "l", "o"]
solution = Solution()
solution.reverseString(s)
print(s)  # Output: ["o", "l", "l", "e", "h"]

s = ["H", "a", "n", "n", "a", "h"]
solution.reverseString(s)
print(s)  # Output: ["h", "a", "n", "n", "a", "H"]


