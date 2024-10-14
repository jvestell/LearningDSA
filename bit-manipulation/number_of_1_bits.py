"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count

s = Solution()
print(s.hammingWeight(0b00000000000000000000000000001011))
print(s.hammingWeight(0b00000000000000000000000010000000))
print(s.hammingWeight(0b11111111111111111111111111111101))

