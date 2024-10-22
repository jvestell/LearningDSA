"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in anagrams:
                anagrams[sorted_s].append(s)
            else:
                anagrams[sorted_s] = [s]
        return list(anagrams.values())
    

solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))            
