"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
"""

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)
        
s = Solution()
print(s.fib(2)) # 1
print(s.fib(3)) # 2
print(s.fib(4)) # 3
print(s.fib(5)) # 5
print(s.fib(6)) # 8
print(s.fib(7)) # 13   


