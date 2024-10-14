"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countS == countT

# Example usage:
s = "anagram"
t = "nagaram"
solution = Solution()
print(solution.isAnagram(s, t))  # Output: True
print(solution.isAnagram("rat", "car"))  # Output: False
print(solution.isAnagram("a", "ab"))  # Output: False
print(solution.isAnagram("ab", "a"))  # Output: False
print(solution.isAnagram("", ""))  # Output: True
