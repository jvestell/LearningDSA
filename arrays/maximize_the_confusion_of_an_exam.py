"""
You are given a binary string s and an integer k. You can change at most k 0's to 1's in s to maximize the number of consecutive 1's.

Return the maximum number of consecutive 1's in the string after changing at most k 0's.
"""

from typing import List

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def helper(target: str) -> int:
            # Initialize window
            max_size = 0
            left = 0
            count = 0  # count of characters we need to change
            
            # Expand window
            for right in range(len(answerKey)):
                if answerKey[right] != target:
                    count += 1
                
                # Shrink window if too many changes needed
                while count > k:
                    if answerKey[left] != target:
                        count -= 1
                    left += 1
                
                # Update max size
                max_size = max(max_size, right - left + 1)
            
            return max_size
        
        # Return max of making all T's or all F's
        return max(helper('T'), helper('F'))
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxConsecutiveAnswers("TTFTTFTT", 1)) # Output: 5
    print(sol.maxConsecutiveAnswers("TFTFTFTT", 2)) # Output: 6


"""
solved on: 11/20/2024
"""

        