"""
A phrase is a palindrome if, after converting all uppercase letters to lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove all non-alphanumeric characters and convert to lowercase
        cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
        s = cleaned_s

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left = left + 1
                right = right - 1
            else:
                return False
        return True

s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama")) # True
print(s.isPalindrome("race a car")) # False
print(s.isPalindrome(" ")) # True
print(s.isPalindrome("0P")) # False
