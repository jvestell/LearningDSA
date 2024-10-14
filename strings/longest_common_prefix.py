from typing import List

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Use the first string as a reference
        first = strs[0]
        
        for i in range(len(first)):
            # Check if this character is present at the same position in all strings
            if any(i == len(s) or s[i] != first[i] for s in strs):
                return first[:i]
        
        return first

class MySolution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Find the length of the shortest string
        min_length = min(len(s) for s in strs)
        keeper = ""
        
        for i in range(min_length):
            chars = [s[i] for s in strs]
            all_same = all(c == chars[0] for c in chars)
            if all_same:
                keeper += chars[0]
            else:
                break
                
        return keeper

s = ["flower", "flower", "flower", "flower", "flower"]
solution = MySolution()
solution.longestCommonPrefix(s)
print(s)

                
            


