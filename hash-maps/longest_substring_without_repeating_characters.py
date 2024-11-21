"""
Given a string s, find the length of the longest substring without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}
        max_length = 0
        start = 0
        
        for end in range(len(s)):
            if s[end] in char_index_map and char_index_map[s[end]] >= start:
                start = char_index_map[s[end]] + 1
            char_index_map[s[end]] = end
            max_length = max(max_length, end - start + 1)
        return max_length

if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb")) # Output: 3

"""
solved on:
11/20/2024
"""
        
