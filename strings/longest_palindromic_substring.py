"""
Given a string s, return the longest palindromic substring in s. example: "babad" -> "bab" or "aba"
example: "cbbd" -> "bb" example: "a" -> "a" example: "ac" -> "a" example: "" -> ""
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""  # Return empty string if input is empty

        start = 0  # Start index of the longest palindrome
        max_length = 1  # Length of the longest palindrome found so far

        def expand_around_center(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1  # Expand to the left
                right += 1  # Expand to the right
            return right - left - 1  # Return the length of the palindrome

        for i in range(len(s)):
            # Odd length palindromes
            length1 = expand_around_center(i, i)
            # Even length palindromes
            length2 = expand_around_center(i, i + 1)
            
            length = max(length1, length2)  # Get the longer palindrome
            if length > max_length:
                start = i - (length - 1) // 2  # Calculate new start index
                max_length = length  # Update max length

        return s[start:start + max_length]  # Return the longest palindromic substring

solution = Solution()
print(solution.longestPalindrome("anyzarrazboss"))
print(solution.longestPalindrome("anyzarazboss"))
print(solution.longestPalindrome("babad"))
print(solution.longestPalindrome("cbbd"))


"""
Solved on: 10/21/2024
"""
