"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
"""

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        print(f"Input digits: {digits}")
        
        digits = [str(digit) for digit in digits]
        print(f"Digits converted to strings: {digits}")
        
        number_str = "".join(digits)
        print(f"Joined number string: {number_str}")
        
        number = int(number_str) + 1
        print(f"Number after adding 1: {number}")
        
        result = [int(digit) for digit in str(number)]
        print(f"Final result: {result}")
        
        return result

# Test the function
solution = Solution()
print("Testing plusOne([1,2,2,9]):")
print(solution.plusOne([1,2,2,9]))
